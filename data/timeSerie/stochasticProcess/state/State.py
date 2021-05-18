import uuid
from mMath.linearAlgebra.Vector import Vector


class State:
    """"""

    def __init__(self):
        '''
        :param refVec:
        '''
        self.__id = uuid.uuid1()

    def getId(self)->uuid.UUID:
        return self.__id
