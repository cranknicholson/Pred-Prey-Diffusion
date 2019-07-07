# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 14:47:06 2019

@author: Henrik
"""
import numpy as np
import scypi
from scipy.sparse import csr_matrix
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve


def calc(n,T,N,evaluateModel,calculateTimeStep,dm,dmcsr):

    dt=T/N
    y=[] 
    x=[]
    a=[] #resultarray
    xneu=np.zeros(n)
    yneu=np.zeros(n)
    y=np.random.rand(n)
    x=np.zeros(n)
    
    
    for k in range(0,n):
        a=calculateTimeStep(1,y[k],dt,evaluateModel)
        xneu[k]=a[0]
        yneu[k]=a[1]
    y=yneu+dt*np.matmul(dm,y)
    x=xneu+dt*np.matmul(dm,x)
    #First loop over N time 
    for i in range(2,int(N+1)):
        #second loop over n boxes 
        for k in range(0,n):
                   #calculate the values for next timeintervall 
                   a=calculateTimeStep(x[k],y[k],dt,evaluateModel)
                   xneu[k]=a[0]
                   yneu[k]=a[1]
        #multiply the vector of all  x or y values of the period i with the diffusion Matrix dm           
        #y=yneu+dt*np.matmul(dm,y)
        #x=xneu+dt*np.matmul(dm,x)
        
        y=yneu+dt*dmcsr.dot(y)
        x=xneu+dt*dmcsr.dot(x)
        
        
    return (x,y)
        