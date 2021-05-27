from mMath.data.probability.continous.uniform.Uniform import Uniform
from mMath.linearAlgebra.matrix.Matrix import Matrix
import random

class PointedIntrestedRegionPdf(Uniform):
    def __init__(self,intrestedRegion:Matrix):
        '''

        :param intrestedRegion:
        '''
        self._intrestedRegion = intrestedRegion

    def getSamples(self)->Matrix:
        num = self._intrestedRegion.getRowsNum()

        randomNpRows = []
        for i in range(0, 5):
            index = random.randint(1, num)
            randomNpRows.append(self._intrestedRegion.getNpRowByIndex(index))
        randomMatrix:Matrix = Matrix(randomNpRows)
        return randomMatrix

