from typing import List

from mMath.linearAlgebra.Vector import Vector


class Cluster:
    def __init__(self, vectors: List[Vector] = None):
        self._vectors = vectors if vectors is not None else []

    def appendVector(self, vector: Vector):
        self._vectors.append(vector)

    def getVectors(self)->List[Vector]:
        return self._vectors