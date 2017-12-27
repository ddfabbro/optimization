#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 00:36:46 2017

@author: davi
"""
import numpy as np

class ContinuousFunction():
    def sphere(self,X):
        return np.sum(X**2)
   
    def venkataraman(self,X):
        """
        Source: Venkataraman, P. (2009). Applied optimization with MATLAB programming.
        """
        return 3*(np.sin(0.5+0.25*X[0]*X[1]))*np.cos(X[0])
   
    def branin(self,X):
        """      
        Source: https://www.sfu.ca/~ssurjano/branin.html
        """
        a=1.; b=5.1/(4.*np.pi**2.); c=5./np.pi
        r=6.; s=10.; t=1./(8.*np.pi)
        return a*(X[1]-b*X[0]**2+c*X[0]-r)**2+s*(1-t)*np.cos(X[0])+s