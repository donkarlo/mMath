import uuid
from mMath.linearalgebra.Vector import Vector


class State:
    """"""

    def __init__(self,  refVec:Vector):
        """"""
        self.__id = uuid.uuid1()
        self.__refVec = refVec

    def getId(self)->uuid.UUID:
        return self.__id
