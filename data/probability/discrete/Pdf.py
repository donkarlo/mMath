from mMath.data.probability.Pdf import Pdf
from mMath.data.probability.Population import Population
from mMath.data.probability.event.Event import Event


class Pdf(Pdf):
    ''''''
    def __init__(self, population:Population):
        '''@todo is sample sub of population'''
        self.__population = population

    def getValueByEvent(self,event:Event):
        ''''''
        return len(event)/len(self.__population)