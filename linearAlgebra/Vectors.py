from typing import List
import numpy as np
from mMath.linearAlgebra.Vector import Vector
from mMath.linearAlgebra.matrix.Matrix import Matrix


class Vectors:
    def __init__(self,vectors:List[Vector]=None):
        self._vectorsList:List[Vector] = vectors if vectors is not None else []

    def append(self,vector:Vector):
        self._vectorsList.append(vector)

    def getMeanVector(self)->Vector:
        '''
        Certainly the order is the same as the order of the given vectors
        :return: Vector of means for each component
        '''
        componentWiseSum:dict = {}
        vector:Vector
        for vectorCounter, vector in enumerate(self._vectorsList):
            for componentCounter, component in enumerate(vector.getNpRows()):
                if componentCounter not in componentWiseSum:
                    componentWiseSum[componentCounter] = 0
                componentWiseSum[componentCounter] += component[0]

        meanVectorArray = []
        for componentWiseSumKey in componentWiseSum:
            meanVectorArray.append(componentWiseSum[componentWiseSumKey] / len(self.getVectorsList()))

        return Vector(meanVectorArray)

    def getCovarianceMatrix(self)->Matrix:
        '''
        Certainly the order is the same as the order of the given vectors
        :return:
        '''
        npRowFormVectors = self.getListRowsFormVectors()
        covMatrix = Matrix(np.cov(npRowFormVectors))
        return covMatrix

    def getCovMatrix(self)->Matrix:
        npRowFormVectors = np.asarray(self.getListRowsFormVectors()).T
        covMatrix = Matrix(np.cov(npRowFormVectors))
        return covMatrix

    def getVarianceVector(self)->Vector:
        '''

        :return: Vector
        '''
        return Vector(np.diag(self.getCovMatrix().getNpRows()))

    def getListRowsFormVectors(self)->List[np.ndarray]:
        '''

        :return:
        '''
        vector: Vector
        listRowFormVectors = []
        for vector in self._vectorsList:
                listRowFormVectors.append(vector.getNpRow().tolist())
        return np.asarray(listRowFormVectors)

    def getVectorsList(self):
        '''

        :return:
        '''
        return self._vectorsList

    def isInMeanCenterVarianceRadiusSphere(self, givenVector:Vector, varianceCoefficient):
        '''

        :param givenVector:
        :param varianceCoefficient:
        :return:
        '''
        if givenVector.getDistanceFrom(self.getMeanVector()) <= varianceCoefficient*self.getVarianceVector().getNorm():
            return True
        else:
            return False