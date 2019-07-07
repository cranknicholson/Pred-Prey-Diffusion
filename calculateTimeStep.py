# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 14:50:14 2019

@author: Henrik
"""



def calc(x,y,dt,evaluateModel):

    #result=evaluateModel(x,y)
    return x+dt*evaluateModel(x,y)[0],y+dt*evaluateModel(x,y)[1]
    