import numpy as np
import pandas as pd
import scipy.stats as st
import enum

from dpf.engine import AnalyticalVanilla
from dpf.engine import StochasticProcess

#! set seed
np.random.seed(1)

paths = 10
steps = 100
t = 0
T = 1.0
mu = 0.1
r = 0.1
sigma = 0.2
s0 = 1.0
K = 0.95
type = "CALL"

#? generate path
Simulation = StochasticProcess.GBMprocess(paths, steps, T, mu, sigma, s0)
result = Simulation.generate_path()
# stock_paths = result['value']
stock_paths = Paths['S']
time = result['time']
dt = Simulation.dt

BSobject = AnalyticalVanilla.BlackScholes(type, s0, K, sigma, t, T, r)
BSobject.value

PNL = np.zeros([paths, steps+1])
starting_delta = BSobject.delta()

PNL[:,0] = BSobject.value - starting_delta * s0

#? Container for PnL and delta and call value
Call = np.zeros([paths, steps+1])
Call[:,0] = BSobject.value

Delta = np.zeros([paths, steps+1])
Delta[:,0] = starting_delta

for i in range(1, steps+1):
    #? Update BS object
    new_t = time[i]
    BSobject.t = new_t
    for j in range(0, paths):
        
        BSobject.S0 = stock_paths[j,i]
        BSobject.refresh()
        
        delta_old = Delta[j,i-1]
        delta_new = BSobject.delta()
        
        PNL[j,i] = PNL[j,i-1]*np.exp(r*dt) - (delta_new - delta_old)*BSobject.S0
        Call[j,i] = BSobject.value
        Delta[j,i] = delta_new
        
        if j == 0 and i <= 10:
            print(delta_new)
            print(delta_old)
            print(BSobject.DeltaT)
            print(dt)
            print(r)
            print(BSobject.S0)
            print(PNL[j,i])
            print("__")

for j in range(0, paths):
    PNL[j,-1] = PNL[j,-1] - np.maximum(stock_paths[j,-1]-K, 0) + Delta[j,-1]*stock_paths[j,-1]


pd_paths = pd.DataFrame(stock_paths)
pd_delta = pd.DataFrame(Delta)
pd_PNL = pd.DataFrame(PNL)
pd_call = pd.DataFrame(Call)

new_t



writer = pd.ExcelWriter('test.xlsx', engine='xlsxwriter')
pd_paths.to_excel(writer, sheet_name="paths")
pd_delta.to_excel(writer, sheet_name="delta")
pd_PNL.to_excel(writer, sheet_name="PNL")
pd_call.to_excel(writer, sheet_name="call")
writer.save()






#! Old functions

class OptionType(enum.Enum):
    CALL = 1.0
    PUT = -1.0

def GeneratePathsGBM(NoOfPaths,NoOfSteps,T,r,sigma,S_0):    
    Z = np.random.normal(0.0,1.0,[NoOfPaths,NoOfSteps])
    X = np.zeros([NoOfPaths, NoOfSteps+1])
    W = np.zeros([NoOfPaths, NoOfSteps+1])
    time = np.zeros([NoOfSteps+1])
        
    X[:,0] = np.log(S_0)
    
    dt = T / float(NoOfSteps)
    for i in range(0,NoOfSteps):

    # Making sure that samples from the normal distribution have mean 0 and variance 1

        if NoOfPaths > 1:
            Z[:,i] = (Z[:,i] - np.mean(Z[:,i])) / np.std(Z[:,i])
        W[:,i+1] = W[:,i] + np.power(dt, 0.5)*Z[:,i]
        X[:,i+1] = X[:,i] + (r - 0.5 * sigma * sigma) * dt + sigma * (W[:,i+1]-W[:,i])
        time[i+1] = time[i] +dt
        
    # Compute exponent of ABM

    S = np.exp(X)
    paths = {"time":time,"S":S}
    return paths

# Black-Scholes call option price

def BS_Call_Put_Option_Price(CP,S_0,K,sigma,t,T,r):
    K = np.array(K).reshape([len(K),1])
    d1    = (np.log(S_0 / K) + (r + 0.5 * np.power(sigma,2.0)) 
    * (T-t)) / (sigma * np.sqrt(T-t))
    d2    = d1 - sigma * np.sqrt(T-t)
    if CP == OptionType.CALL:
        value = st.norm.cdf(d1) * S_0 - st.norm.cdf(d2) * K * np.exp(-r * (T-t))
    elif CP == OptionType.PUT:
        value = st.norm.cdf(-d2) * K * np.exp(-r * (T-t)) - st.norm.cdf(-d1)*S_0
    return value

def BS_Delta(CP,S_0,K,sigma,t,T,r):
    # When defining a time grid it may happen that the last grid point 
    # lies slightly a bit behind the maturity time

    if t-T>10e-20 and T-t<10e-7:
        t=T
    K = np.array(K).reshape([len(K),1])
    d1    = (np.log(S_0 / K) + (r + 0.5 * np.power(sigma,2.0)) * \
             (T-t)) / (sigma * np.sqrt(T-t))
    if CP == OptionType.CALL:
        value = st.norm.cdf(d1)
    elif CP == OptionType.PUT:
       value = st.norm.cdf(d1)-1.0
    return value


np.random.seed(1)
NoOfPaths = 1000
NoOfSteps = 200
T         = 1.0
r         = 0.1
sigma     = 0.2
s0        = 1.0
K         = [0.95]
CP        = OptionType.CALL

np.random.seed(1)
Paths = GeneratePathsGBM(NoOfPaths,NoOfSteps,T,r,sigma,s0)
time  = Paths["time"]
S     = Paths["S"]

# Setting up some handy lambda values

C = lambda t,K,S0: BS_Call_Put_Option_Price(CP,S0,K,sigma,t,T,r)
Delta = lambda t,K,S0: BS_Delta(CP,S0,K,sigma,t,T,r)

# Setting up the initial portfolio
PnL = np.zeros([NoOfPaths,NoOfSteps+1])
delta_init= Delta(0.0,K,s0)
PnL[:,0] = C(0.0,K,s0) - delta_init * s0
        
CallM      = np.zeros([NoOfPaths,NoOfSteps+1])
CallM[:,0] = C(0.0,K,s0)
DeltaM     = np.zeros([NoOfPaths,NoOfSteps+1])
DeltaM[:,0] = Delta(0,K,s0)

for i in range(1,NoOfSteps+1):
    dt = time[i] - time[i-1]
    
    delta_old  = Delta(time[i-1],K,S[:,i-1])
    delta_curr = Delta(time[i],K,S[:,i])
    
    PnL[:,i]    =  PnL[:,i-1]*np.exp(r*dt) - (delta_curr-delta_old)*S[:,i] # PnL
    CallM[:,i]  = C(time[i],K,S[:,i])
    DeltaM[:,i] = delta_curr

# Final transaction, payment of the option (if in the money) and selling the hedge
PnL[:,-1] = PnL[:,-1] -np.maximum(S[:,-1]-K,0) +  DeltaM[:,-1]*S[:,-1]
