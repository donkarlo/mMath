from mmath.data.probability.Pdf import Pdf
from mmath.data.probability.Population import Population
from mmath.data.probability.Event import Event


class Pdf(Pdf):
    def __init__(self, sample:Event, population:Population):
        '''@todo is sample sub of population'''
        self.__sample = sample
        self.__population = population

    def getProbability(self):
        return len(self.__sample)/len(self.__population)