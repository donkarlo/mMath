from typing import List

from mMath.data.probability.event.Vector import Vector
from mMath.data.probability.Pdf import Pdf
from mMath.data.probability.event.Point import PointEvent
from mMath.linearAlgebra.matrix.Matrix import Matrix
from mMath.linearAlgebra.Vector import Vector
from scipy.stats import multivariate_normal
import numpy as np


class Gaussian(Pdf):
    ''''''
    def __init__(self, mean: Vector, covariance: Matrix):
        ''''''
        self.__mean:Vector = mean
        self.__covariance:Matrix = covariance

    def getValueAt(self, event: Vector)->float:
        '''
        :param event:
        :return:
        '''
        # @todo if event not instance of interval and a one dimentional vector(scalar)
        # @todo for 1 d
        # @todo mean should be a list like [1,2]
        # @todo cov like [[1,3],[2,2]]
        if type(event) is PointEvent:
            event:PointEvent
            var = multivariate_normal(mean=self.__mean, cov=self.__covariance)
            return var.pdf(event)



    def getASample(self)->Vector:
        sampleVec:Vector = self.getSamples(1)[0]
        return sampleVec

    def getSamples(self,sampleSize:int)->Matrix:
        samplesList: List = np.random.multivariate_normal(self.getMean()
                                                          , self.getCovariance()
                                                          , sampleSize)
        sampleVecs:List[Vector] = []
        for sample in samplesList:
            sampleVecs.append(Vector(sample))
        matrix = Matrix(sampleVecs)
        return sampleVecs

    def getASampleValue(self):
        return self.getValueAt(self.getASample())

    def getMean(self)->Vector:
        return self.__mean

    def getCovariance(self)->Matrix:
        return self.__covariance
