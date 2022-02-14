from typing import List
from mMath.data.probability.event.Vector import Vector
import abc

from mMath.linearAlgebra.Vector import Vector
from mMath.linearAlgebra.matrix.Matrix import Matrix
from mMath.region.Region import Region


class Pdf(metaclass=abc.ABCMeta):
    '''Distributes 1 between all possible outcomes of a random variable such that the summation is 0'''
    def __init__(self):
        ''''''
        self._mean = None
        self._standardDeviation = None

    @abc.abstractmethod
    def getValueAt(self, point:Vector)->float:
        ''''''
        pass

    @abc.abstractmethod
    def getSamples(self, samplesSize:int, intrestedRegion:Region)->List:
        pass

    @abc.abstractmethod
    def getMean(self)->float:
        pass

    @abc.abstractmethod
    def getCovarianceMatrix(self)->Matrix:
        pass

    def getASample(self)->Vector:
        return  self.getSamples(1)[0]