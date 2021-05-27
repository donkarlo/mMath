from mMath.data.probability.event.Event import Event
import abc

from mMath.linearAlgebra.matrix.Matrix import Matrix


class Pdf(abc.ABCMeta):
    '''Distributes 1 between all possible outcomes of a random variable such that the summation is 0'''
    def __init__(self):
        ''''''
        self._mean = None
        self._standardDeviation = None

    @abc.abstractmethod
    def getValueByEvent(self,event:Event)->float:
        ''''''
        pass

    @abc.abstractmethod
    def getSamples(self,samplesNum:int)->Matrix:
        pass

    @abc.abstractmethod
    def getMean(self):
        pass

    @abc.abstractmethod
    def getStandardDeviation(self):
        pass