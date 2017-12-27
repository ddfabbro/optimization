#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 20:02:48 2017

@author: davi
"""
import os
import numpy as np
import matplotlib.pyplot as plt
import sys; sys.path.append('../')
from pyooopt import EvolutionaryAlgorithm
from pyooopt.cost_functions import ContinuousFunction
   
np.random.seed(0)
   
function = ContinuousFunction()
ecosystem = EvolutionaryAlgorithm('min',function.venkataraman,20,2,[-5,5])
optimizer_results =ecosystem.evolve(.8,.1,10)
   
###PLOTTING
x1 = np.linspace(-5, 5, 100)
x2 = np.linspace(-5, 5, 100)
X = np.array(np.meshgrid(x1, x2))
z = function.venkataraman(X)
   
for i, generation in enumerate(optimizer_results['solutions']):
    plt.figure()
    plt.contour(x1,x2,z,np.arange(-3.3, 3.5, .25).tolist(),cmap='jet')
    plt.scatter(generation[:,0],generation[:,1],c=[0,0,0],zorder=1e+3)
    plt.savefig('generation'+str(i)+'.jpg')
   
#Create .gif
os.system('convert -delay 20 -loop 0 *.jpg evolution.gif')
os.system('rm *.jpg')