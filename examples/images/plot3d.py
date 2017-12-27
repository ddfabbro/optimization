#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 01:03:24 2017

@author: davi
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sys; sys.path.append('../../')
from pyooopt.cost_functions import ContinuousFunction

function = ContinuousFunction()

fig = plt.figure()
ax = Axes3D(fig, azim = -120, elev = 40)

x1 = np.linspace(-5, 5, 100)
x2 = np.linspace(-5, 5, 100)
X = np.array(np.meshgrid(x1, x2))
Z = function.venkataraman(X)

ax.plot_surface(X[0], X[1], Z, cmap='jet', linewidth=.2, edgecolor='black')
ax.set_xlim([-5, 5])                                                       
ax.set_ylim([-5, 5])

plt.savefig('3dplot.jpg')