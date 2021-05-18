from mMath.linearAlgebra.matrix.Matrix import Matrix


class Decorator(Matrix):
    def __init__(self,matrix:Matrix):
        self._matrix=matrix

