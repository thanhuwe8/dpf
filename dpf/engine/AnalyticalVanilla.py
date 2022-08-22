import numpy as np
import scipy.stats as st
from copy import deepcopy

#todo: Incorporate datetime into the class (t and T will be 2 datetime object)
class BlackScholes:
    def __init__(self,type,S0,K,sigma,t,T,r):
        self.type = type
        self.S0 = S0
        self.K = K
        self.sigma = sigma
        self.t = t 
        self.T = T
        self.r = r
        self.DeltaT = float(T-t)
        
        #? Analytical info and Greek sensitivities
        self.delta_value = 0
        self.gamma_value = 0
        self.vega_value = 0
        self.d1 = 0
        self.d2 = 0
        self.value = 0

        #? Calculate all analytical info and Greek sensitivities
        self.refresh()

    def __str__(self):
        pass


    def __copy__(self):
        cls = self.__class__
        result = cls.__new__(cls)
        result.__dict__.update(self.__dict__)
        return result


    def diff_t(self):
        a = self.T - self.t 
        return(a)


    def deeone(self):
        d1 = (np.log(self.S0 / self.K) + (self.r + 0.5 * np.power(self.sigma,2.0))*(self.DeltaT)) / (self.sigma * np.sqrt(self.DeltaT))
        return(d1)


    def deetwo(self):
        d1 = self.deeone()
        d2 = d1 - self.sigma*np.sqrt(self.DeltaT)
        return(d2)


    def pricing(self):
        if self.type == "CALL":
            value = st.norm.cdf(self.d1)*self.S0 - st.norm.cdf(self.d2)*self.K*np.exp(-self.r*(self.DeltaT))
        elif self.type == "PUT":
            value = st.norm.cdf(-1*self.d2)*self.K - st.norm.cdf(-1*self.d1)*self.S0*np.exp(-self.r*(self.DeltaT))
        else:
            value = None
            print("Type should be 'CALL' or 'PUT'")
        return(value)


    #? this method is used to modify the attribute "value" based on newly updated option info
    def price_calculation(self):
        self.value = self.pricing()

    #? This method is used to re-calculate Greek sensitivities after we use 'repricing'
    def greek_recalculate(self):
        self.delta_value = self.delta()
        self.gamma_value = self.gamma()
        self.vega_value = self.vega()

    #? This method is used to calculate delta for an option object
    def delta(self):
        if self.type == "CALL":
            value = st.norm.cdf(self.deeone())
        elif self.type == "PUT":
            value = st.norm.cdf(self.deeone()) -1
        else: 
            value = None
            print("Type should be 'CALL' or 'PUT'")
        return(value)

    def gamma(self):
        value = st.norm.pdf(self.deeone())/(self.S0*self.sigma*np.sqrt(self.DeltaT))
        return(value)

    def vega(self):
        value = self.S0*st.norm.pdf(self.deeone())*np.sqrt(self.DeltaT)
        return(value)

    #! Used to update all derived attributes for option positions
    def update_dt(self):
        self.DeltaT = self.diff_t()
    
    def update_d1(self):
        self.d1 = self.deeone()
    
    def update_d2(self):
        self.d2 = self.deetwo()

    def update_greeks(self):
        self.delta_value = self.delta()
        self.gamma_value = self.gamma()
        self.vega_value = self.vega()
    
    def update_price(self):
        self.value = self.pricing()

    def refresh(self):
        self.update_dt()
        self.update_d1()
        self.update_d2()
        self.update_greeks()
        self.update_price()


    @staticmethod
    def newton_raphson_iv(option_object, observed_price, max_counter = 10000):
        
        #todo: override "copy() method to copy object"
        clone_object = deepcopy(option_object)

        starting_iv = 0.25
        new_iv = starting_iv

        counter = 0
        tole = 1e-7
        diff_price = 1

        while(abs(diff_price) >= tole and counter <= max_counter):
            if counter == 0:
                new_iv = starting_iv

            #? set new iv for clone object
            clone_object.sigma = new_iv
            
            #print("new implied volatility is: {}".format(clone_object.sigma))

            #? recalculate option value
            setattr(clone_object, "sigma", new_iv)
            clone_object.refresh()

            #print("clone value is {}".format(clone_object.value))
            diff_price = clone_object.value - observed_price #? when this one is minimized, the implied volatility is found

            #? recalculate option vega
            clone_object.vega_value = clone_object.vega()
            der_diff_price = clone_object.vega_value

            # print("new vega is: {}".format(der_diff_price))
            # print("difference between 2 price is: {}".format(diff_price))
            # print("clone value is {}".format(clone_object.value))
            #? new implied volatility 
            new_iv = new_iv - diff_price/der_diff_price
            counter += 1
        print(new_iv)
        result = {"NewIV":new_iv, "NewOption":clone_object}
        return(result)


