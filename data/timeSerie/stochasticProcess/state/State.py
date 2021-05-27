import uuid


class State:
    """"""

    def __init__(self):
        '''
        :param refVec:
        '''
        self.__id = uuid.uuid1()

    def getId(self)->uuid.UUID:
        return self.__id
