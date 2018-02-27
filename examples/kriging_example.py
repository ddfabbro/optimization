# -*- coding: utf-8 -*-
import os
import numpy as np
import matplotlib.pyplot as plt 
from pyKriging.krige import kriging  
from pyDOE import lhs
import sys; sys.path.append('../')
from pyooopt.cost_functions import ContinuousFunction

class MyKriging(kriging):
    def __init__(self,*args,**kwargs):
        kriging.__init__(self,*args,**kwargs)
    def kdata(self):
        plotgrid = 61
        x = np.linspace(0, 1, num=plotgrid)
        y = np.linspace(0, 1, num=plotgrid)
        X, Y = np.meshgrid(x, y)
        
        zs = np.array([self.predict([x,y]) for x,y in zip(np.ravel(X), np.ravel(Y))])
        Z = zs.reshape(X.shape)
        
        spx = (self.X[:,0] * (self.normRange[0][1] - self.normRange[0][0])) + self.normRange[0][0]
        spy = (self.X[:,1] * (self.normRange[1][1] - self.normRange[1][0])) + self.normRange[1][0] 
        
        return X,Y,Z,spx,spy

def kriging_plot(i,k):
    X,Y,Z,spx,spy=k.kdata()
    plt.figure()
    plt.contour(X,Y,Z,np.arange(-3.3, 3.5, .25).tolist(), cmap='jet')
    plt.scatter(spx[11+i],spy[11+i],c='black',edgecolors='white',s=75,zorder=1000)
    plt.xlim(0,1)
    plt.ylim(0,1)
    plt.savefig('iteration'+str(i)+'.jpg')

def testfun(f,X):
    try:
        X.shape[1]
    except:
        X = np.array([X])
    
    Xs = 10*X-5
    z = []
    for x in Xs:
        z.append(f(x))
    return np.array(z)

np.random.seed(20)
X = lhs(2,samples=11)

function = ContinuousFunction()
y = testfun(function.venkataraman,X)

k = MyKriging(X, y, testfunction=testfun, name='simple')  
k.train()

numiter = 10
for i in range(numiter/2):
    print 'Infill iteration {0} of {1}....'.format(2*i + 1, numiter)
    newpoints = k.infill(1)
    for point in newpoints:
        k.addPoint(point, testfun(function.venkataraman,point))
    k.train()
    kriging_plot(2*i,k)
        
    print 'Infill iteration {0} of {1}....'.format(2*i+1 + 1, numiter)
    newpoints = k.infill(1, method='ei')
    for point in newpoints:
        k.addPoint(point, testfun(function.venkataraman,point))
    k.train()
    kriging_plot(2*i+1,k)
    
os.system('convert -delay 20 -loop 0 *.jpg images/kriging.gif')
os.system('rm *.jpg')