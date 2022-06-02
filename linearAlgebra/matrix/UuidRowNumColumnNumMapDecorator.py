from typing import List

from mMath.linearAlgebra.matrix.Decorator import Decorator
from mMath.linearAlgebra.matrix.Matrix import Matrix
from mMath.linearAlgebra.matrix.UuidRowNumColumnNumMapper import UuidRowNumColumnNumMapper


class UuidRowNumColumnNumMapDecorator(Decorator):
    def __init__(self, matrix:Matrix, uuidRowNumColumnNumMappper:List[UuidRowNumColumnNumMapper]):
        '''

        :param matrix:
        :param uuidRowNumColumnNumMappper:
        '''
        super().__init__(matrix)
        self.__uuidRowNumColumnNumMapppers:List[UuidRowNumColumnNumMapper] = uuidRowNumColumnNumMappper
