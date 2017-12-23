#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 19:58:59 2017

@author: davi
"""
import os
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append('../cost_functions')
from benchmark import ContinuousFunction

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

if __name__ == "__main__":
   
    function = ContinuousFunction()
    optimizer = GradientDescent(function.venkataraman)
    X0 = np.array([.5,.5]) #initial guess
    optimizer_results = optimizer.search(X0,.33,10)
   
    #PLOTTING
    x1 = np.linspace(-5, 5, 100)
    x2 = np.linspace(-5, 5, 100)
    X = np.array(np.meshgrid(x1, x2))
    z = function.venkataraman(X)
   
    plt.contour(x1,x2,z,np.arange(-3.3, 3.5, .25).tolist(),cmap='jet')
   
    for i,solution in enumerate(optimizer_results['solution']):
        plt.figure()
        plt.contour(x1,x2,z,np.arange(-3.3, 3.5, .25).tolist(),cmap='jet')
        plt.scatter(solution[0],solution[1],c=[0,0,0],zorder=1e+3)
        plt.savefig('iteration'+str(i)+'.jpg')
   
    #Create .gif
    os.system('convert -delay 20 -loop 0 *.jpg descent.gif')
    os.system('rm *.jpg')