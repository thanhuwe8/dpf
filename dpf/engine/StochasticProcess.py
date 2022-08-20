from abc import ABC, abstractmethod
import numpy as np
import scipy.stats as st


#? Base abstract class for any StochasticProcess
class StochasticProcess(ABC)
    def __init__(self, paths,steps,T,mu,sigma,x0):
        self.paths = paths
        self.steps = steps
        self.T = T
        self.mu = mu
        self.sigma = sigma
        self.x0 = x0
        self.dt = T/float(steps)
        
        # #? Container for simulated values
        # self.X = np.zeros([self.paths, self.steps+1])
        # self.W = np.zeros([self.paths, self.steps+1])  
        
    @abstractmethod
    def generate_path(self):
        pass
    
    
    @abstractmethod
    def return_drift(self):
        pass
    
    
    @abstractmethod
    def return_diffusion(self):
        pass
    


class GBMprocess(StochasticProcess):
    def __init__(self, paths, steps, T, mu, sigma, x0):
        super().__init__(paths, steps, T, mu, sigma, x0)
    
    
    #? generate 
    def generate_path(self):
        Z = np.random.normal(0.0,1.0,[self.path, self.steps])
        X = np.zeros([self.paths, self.steps+1])
        W = np.zeros([self.paths, self.steps+1])  
        
        for i in range(self.steps):
            if self.paths > 1:
                Z[:,1] = (Z[:,i] - np.mean(Z[:,i]))/np.std(Z[:,i])
            W[:,i+1] = W[:,i] + (r - 0.5*self.sigma*self.sigma)*self.dt + self.sigma
        