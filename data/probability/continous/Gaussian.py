import math
from typing import List

from mMath.data.probability.Event import Event
from mMath.data.probability.Pdf import Pdf
from mMath.linearalgebra.Matrix import Matrix
from mMath.linearalgebra.Vector import Vector


class Gaussian(Pdf):
    ''''''
    def __init__(self, mean: Vector, covariance: Matrix):
        ''''''
        self.__mean = mean
        self.__covariance = covariance

    def getValueByEvent(self, event: Event)->float:
        '''
        :param event:
        :return:
        '''
        # @todo if event not instance of interval and a one dimentional vector(scalar)
        y = (1 / (self.__covariance * math.sqrt(2 * math.pi))) * math.e ** (
                -(event - self.__mean) ** 2 / (2 * self.__covariance ** 2))
        return y
