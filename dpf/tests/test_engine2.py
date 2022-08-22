from dpf.engine import AnalyticalVanilla
import numpy as np

'''
This is used to test implied volatility function
'''

#? Test 1: Dan Stefanica's example
type1 = "CALL"
type2 = "PUT"
S0 = 80
K = 100
sigma = 0.2
t = 0.0
T = 1.0
r = 0.05
observed_price = 7


#Put_object = BSVanilla.BlackScholes(type2,S0,K,sigma,t,T,r)
# implied_volatility = BSVanilla.BlackScholes.newton_raphson_iv(Call_object, observed_price, max_counter=10)
#implied_volatility2 = BSVanilla.BlackScholes.newton_raphson_iv(Put_object, observed_price, max_counter=10)

# implied_volatility['NewIV']
#implied_volatility2['NewIV']


