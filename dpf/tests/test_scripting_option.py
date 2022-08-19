from dpf.scripting import AnalyticalVanilla


#? 1. TESTING dataset form Dan Stefanica 
type1 = "CALL"
type2 = "PUT"
S0 = 100.0
K = 100.0
sigma = 0.2
t = 0.01
T = 1.0
r = 0.0

Call_object = AnalyticalVanilla.BlackScholes(type1,S0,K,sigma,t,T,r)
Put_object = AnalyticalVanilla.BlackScholes(type2,S0,K,sigma,t,T,r)


# Call_object.calculate_all()
Call_object.value
Call_object.d1
Call_object.d2
Call_object.delta_value
Call_object.gamma_value
Call_object.vega_value

# Put_object.calculate_all()
Call_object.value
Call_object.d1
Call_object.d2
Call_object.delta_value
Call_object.gamma_value
Call_object.vega_value


#? 2. Testing with GRID numpy

Call_object = AnalyticalVanilla.BlackScholes(type1,S0,K,sigma,t,T,r)
Put_object = AnalyticalVanilla.BlackScholes(type2,S0,K,sigma,t,T,r)

#?
K = np.linspace(80, 120, 20)
call_grid = np.zeros(shape=len(K))
put_grid = np.zeros(shape=len(K))
d1_grid = np.zeros(shape=len(K))
d2_grid = np.zeros(shape=len(K))

for index, strike in enumerate(K):
    #? get the object 
    call_option = AnalyticalVanilla.BlackScholes(type1,S0,strike,sigma,t,T,r)
    put_option = AnalyticalVanilla.BlackScholes(type2,S0,strike,sigma,t,T,r)

    #? store the data
    call_grid[index] = call_option.value
    put_grid[index] = put_option.value
    d1_grid[index] = call_option.d1
    d2_grid[index] = call_option.d2
    
print(d1_grid)
print(d2_grid)
print(call_grid)
print(put_grid)
