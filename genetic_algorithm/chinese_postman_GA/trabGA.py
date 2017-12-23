# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 13:13:07 2016

@author: davi
"""
import time
from ChinesePostman import population, evolve, best
import matplotlib.pyplot as plt
import numpy as np

def grafico(bests,q,label):
    bests = np.array(bests)
    means=np.zeros(bests.shape[1])
    for i in range(0,means.shape[0]):
        means[i]=np.mean(bests[:,i])
    plt.grid(True)
    plt.title("%s solutions (time = %s s x %s samples)" % (q,round((time.clock()-st)/samples,3),samples))
    plt.xlabel('Epoch')
    plt.ylabel('Optimal solution average')
    y = 12
    plt.ylim(7.9,y) #(7.9,12)(12,100)
    plt.text(.78*epoch, .642*y+2.796, "Elitism = %s%% \nDiversity = %s%%\nCrossover = %s%%\nMutation = %s%%" % (round(elitismo*100),
        round(betas*100),round(crossover*100),round(mutate*100)), bbox={'facecolor':'white', 'alpha':.75, 'pad':10})
    return plt.plot(means,label=label,linewidth=2) #(55,10.5)(157,67)

elitismo=.15
betas=0.15
crossover=.8
mutate=0.08

epoch = 70
samples = 20
q = [20,50,100,150]
bests = [[0 for x in range(epoch)] for y in range(samples)]

for k in range(1,5):
  st = time.clock()
  for j in range(samples):
      pop = population(q[k-1])
      bests[j][0] = best(pop)[0]
      for i in range(1,epoch):
          pop = evolve(pop, elitismo, betas, crossover, mutate)
          bests[j][i]=best(pop)[0]
  plt.style.use('classic')
  plt.subplot(int(str(22)+str(k)))
  grafico(bests,q[k-1],"GA")
  plt.legend(loc='best')
  
  #Brute Force
  for j in range(samples):
      pop = population(q[k-1])
      bests[j][0] = best(pop)[0]
      for i in range(1,epoch):
          pop = population(q[k-1])
          if best(pop)[0] < bests[j][i-1]:
              bests[j][i]=best(pop)[0]
          else:
              bests[j][i] = bests[j][i-1]
  grafico(bests,q[k-1],"Brute")
  plt.legend(loc='best')