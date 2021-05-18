from typing import List

import UuidRowNumColumnNumMapper
class UuidRowNumColumnNumMapBuilder:
    def __init__(self):
        self.__uuidRowNumColNumMapppers:List[UuidRowNumColumnNumMapper] = None

    def addMapper(self, uuidRowNumColumnNumMapper:UuidRowNumColumnNumMapper):
        '''
        :param uuidRowNumColumnNumMapper:
        :return:
        '''
        self.__uuidRowNumColNumMapppers.append(uuidRowNumColumnNumMapper)

    def getMapper(self):
        return UuidRowNumColumnNumMapper(self.__uuidRowNumColNumMapppers)
