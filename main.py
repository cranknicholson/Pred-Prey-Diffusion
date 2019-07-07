# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 14:36:21 2019
Predator Prey Diff
@author: Henrik
"""

import matplotlib.pyplot as plt
import evaluateTimeLoop
import evaluateModel 
import calculateTimeStep
import numpy as np

from scipy import sparse
import time

start = time.time()
start_proc = time.process_time()

result = []

x0=1.0
T=500
n=100
kappa=0.001
N=4*(n**2)*kappa*T
b = n

dm= np.zeros((n, n))

    # build the diffusionmatrix dm 
for i in range(0,n):
    for j in range(0,n):
        if i==j and (i==0 or i==n-1):
            dm[i][j]=-1
        elif i == j and (j != 0 or j != n-1):
            dm[i][j]=-2
        elif i == j-1 or i == j+1:
            dm[i][j]=1
dm= (kappa*(n**2) *dm )          
        
            

dmcsr=sparse.csr_matrix(dm) 
 
 

result=evaluateTimeLoop.calc(n,T,N,evaluateModel.calc,calculateTimeStep.calc,dm,dmcsr)

ende = time.time()
ende_proc = time.process_time()
print('Gesamtzeit: {:5.3f}s'.format(ende-start))
print('Systemzeit: {:5.3f}s'.format(ende_proc-start_proc))

predator=result[0]
prey=result[1]
#plot
m = np.arange(0, len(result[0]), 1)  # Start, Stop, Step
plt.plot(m,predator, color='blue', linewidth=1.0, linestyle='-',label=r'predator')
plt.plot(m,prey, color='red', linewidth=1.0, linestyle='-',label=r'prey')

plt.legend(loc='upper left', frameon=True)
plt.grid(True)
plt.show


