import numpy as np
import pandas as pd



#* 1: Brownian Motion:
#* 1.a 

n = 10
dt = 1/n
Z = np.random.normal(0.0,1.0,[n])
A = np.zeros([n,n])
T = np.ones([n])
T = T*dt

for ix,x in enumerate(A):
    for iy,y in enumerate(x):
        if ix >= iy:
            A[ix,iy] = dt

path_value = np.matmul(A,Z)
