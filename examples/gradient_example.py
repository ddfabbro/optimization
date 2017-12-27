#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 20:02:49 2017

@author: davi
"""
import os
import numpy as np
import matplotlib.pyplot as plt
import sys; sys.path.append('../')
from pyooopt import GradientDescent
from pyooopt.cost_functions import ContinuousFunction
   
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
os.system('convert -delay 20 -loop 0 *.jpg images/descent.gif')
os.system('rm *.jpg')