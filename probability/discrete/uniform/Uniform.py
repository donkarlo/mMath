from random import random
from typing import List

from mMath.probability.discrete.Population import Population as DiscreetPopulation

class Uniform():
    def __init__(self,population:DiscreetPopulation):
        self._population:DiscreetPopulation = population

    def getSamples(self,sampleSize:int=1)->List:
        random.sample(self._population.getMembers(),sampleSize)
