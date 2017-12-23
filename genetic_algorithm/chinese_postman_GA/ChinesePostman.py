# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 18:49:36 2016

@author: Davi

Credits: https://lethain.com/genetic-algorithms-cool-name-damn-simple/
"""
import random
from params import cidades, caminhos

def individual():
  """    
  Generate random solution
  """
  return random.sample(range(cidades), cidades)
    
def population(qtde):
  """
  Generate population of solutions
  
  qtde: quantity of solutions for population
  """
  return [individual() for x in range(qtde)]

def fitness(path):
  """
  Calculates fitness for solution
  
  path: evaluated solution
  """
  cost = []
  for x in range(cidades-1):
      cost.append(caminhos[str(path[x])+str(path[x+1])])
  fit = sum(cost)
  return fit

def cruzamento(male, female):
    """
    Crossover between two solutions
    
    male: solution 1
    female: solution 2
    """
    zygote = [-1 for x in range(cidades)]
    i = random.randint(0,int(len(male)/2))
    sperm = male[i:i+int(len(male)/2)]
    egg = female
    for j in sperm: egg=[k for k in egg if k != j]
    zygote[i:i+int(len(male)/2)] = sperm
    for j in egg:
        for k in range(len(zygote)):
            if zygote[k] == -1:
                zygote[k] = j
                break   
    return zygote
    
def mutacao(ind):
    """
    Mutates solution
    
    ind: Mutated solution
    """
    pos1 = random.randint(0, len(ind)-1)
    pos2 = random.randint(0, len(ind)-1)
    while pos1 == pos2:
        pos2 = random.randint(0, len(ind)-1)
    ind[pos1], ind[pos2] = ind[pos2], ind[pos1]
    return ind

def evolve(pop,retain, random_select, crossover, mutate):
    """
    Evolving process
    
    pop: population to be evolved
    retain: elistism rate
    random_select: random selection probability
    crossover: crossover probability
    mutate: mutation probability
    """
    graded = [ (fitness(x), x) for x in pop]
    graded = [ x[1] for x in sorted(graded)]
    retain_length = int(len(graded)*retain)
    parents = graded[:retain_length]
    
    # randomly add other individuals to promote genetic diversity
    for individual in graded[retain_length:]:
        if random_select > random.random():
            parents.append(individual)
            
    # crossover parents to create children
    parents_length = len(parents)
    desired_length = len(pop) - parents_length
    children = []
    while len(children) < desired_length:
        male = random.randint(0, parents_length-1)
        female = random.randint(0, parents_length-1)
        if male != female:
            male = parents[male]
            female = parents[female]
            if crossover > random.random():
              child = cruzamento(male,female)
              children.append(child)
            else:
              children.append(female)
    parents.extend(children)
    
    # mutate some individuals
    for individual in parents:
        if mutate > random.random():
            mutacao(individual)
    return parents

def best(pop):
    """
    Find best fitness for a population.
    """
    fitPop = [fitness(pop[x]) for x in range(len(pop))]
    return min(fitPop), pop[min(range(len(fitPop)),key=fitPop.__getitem__)]