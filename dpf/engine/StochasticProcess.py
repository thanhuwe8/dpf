from abc import ABC, abstractmethod
import numpy as np
import scipy.stats as st


#? Base abstract class for any StochasticProcess
class StochasticProcess(ABC):
    def __init__(self, paths,steps,T,mu,sigma,x0):
        self.paths = paths
        self.steps = steps
        self.T = T
        self.mu = mu
        self.sigma = sigma
        self.s0 = x0
        self.dt = self.T/float(self.steps)


    def update_dt(self):
        self.dt = self.T/float(self.steps)
    
    @abstractmethod
    def generate_path(self):
        pass
    
    @abstractmethod
    def return_drift(self):
        pass
    
    @abstractmethod
    def return_variance(self):
        pass



class GBMprocess(StochasticProcess):
    def __init__(self, paths, steps, T, mu, sigma, s0):
        super().__init__(paths, steps, T, mu, sigma, s0)
    
    
    #? generate paths for GBM process
    def generate_path(self):
        Z = np.random.normal(0.0,1.0,[self.paths, self.steps])
        X = np.zeros([self.paths, self.steps+1])
        X[:,0] = np.log(self.s0)
        W = np.zeros([self.paths, self.steps+1])
        time = np.zeros([self.steps+1])
        
        for i in range(self.steps):
            if self.paths > 1:
                Z[:,1] = (Z[:,i] - np.mean(Z[:,i]))/np.std(Z[:,i])
            W[:,i+1] = W[:,i] + np.power(self.dt, 0.5)*Z[:,i]
            X[:,i+1] = X[:,i] + (self.mu - 0.5*self.sigma*self.sigma)*self.dt + self.sigma*(W[:,i+1] - W[:,i])
            time[i+1] = time[i] + self.dt
        
        S = np.exp(X)
        generated_path = {"time":time, "value":S}
        return(generated_path)
    
    #? 
    def return_drift(self):
        drift_value = self.mu * self.dt
        return(drift_value)
    
    #?
    def return_variance(self):
        diffusion_value = self.sigma * self.sigma * self.dt
        return(diffusion_value)