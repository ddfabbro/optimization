#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 19:58:59 2017

@author: davi
"""
import numpy as np

class GradientDescent():
   
    def __init__(self,function):
        self.function = function
   
    def gradient(self,X):
        """
        In: numpy.array([x1,x2,...,xn])
        Out: numpy.array([dx1,dx2,...,dxn])
        """
        h = 1e-5
        derivative_array = np.empty(X.shape[0])
        for i in range(X.shape[0]):
            X_upper = np.copy(X).astype(np.float); X_upper[i]+=h
            X_lower = np.copy(X).astype(np.float); X_lower[i]-=h
            derivative_array[i] = (self.function(X_upper)-self.function(X_lower))/(2*h)
        return derivative_array
   
    def search(self,X,a,N):
        """
        In: numpy.array([x1_0,x2_0,...,xn_0]), float(learning_rate), int(iterations)
        Out: {'solution': [X_0,X_1,...,X_n], 'output': [f(X_0),f(X_1),...,f(X_n)]}
        """
        optimization_process = {'solution': [], 'output': []}
        for i in range(N):
            optimization_process['solution'].append(X)
            optimization_process['output'].append(self.function(X))
            X1 = X - a*self.gradient(X)
            X = np.copy(X1)
        return optimization_process