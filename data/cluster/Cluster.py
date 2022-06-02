from typing import List
from mMath.linearAlgebra.Vector import Vector
from mMath.linearAlgebra.Vectors import Vectors
import uuid

class Cluster:
    def __init__(self, vectors = None):
        '''
        :param vectors:
        '''
        self.__id = uuid.uuid1()
        if vectors is None:
            self._vectors = Vectors()
        elif type(vectors) is List:
            vectorsObject = Vectors()
            for vector in vectors:
                vectorsObject.append(vector)
            self._vectors=vectorsObject
        elif type(vectors) is Vectors:
            self._vectors = vectors

    def appendVector(self, vector: Vector):
        '''
        :param vector:
        :return:
        '''
        self._vectors.append(vector)

    def getVectors(self)->Vectors:
        '''
        :return:
        '''
        return self._vectors
