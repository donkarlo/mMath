from mMath.probability.Pdf import Pdf
from mMath.probability.Population import Population
from mMath.probability.event.Vector import Vector


class Pdf(Pdf):
    '''
    '''
    def __init__(self, population:Population):
        '''@todo is sample sub of population'''
        self._population = population

    def setPopulation(self):
        '''
        The mechanisim of assigning probability to population matters
        :return:
        '''
    def getValueByEvent(self, event:Vector):
        '''
        :param event:
        :return:
        '''
        return len(event)/len(self._population)