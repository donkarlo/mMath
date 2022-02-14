from typing import List


class Population:
    def __init__(self, memebers: List=None):
        self._memebers: List = [] if memebers is None else memebers

    def getSize(self)->int:
        '''
        
        :return:
        '''
        return len(self._memebers)

    def addMember(self, member):
        #check uniqueness
        self._memebers.append(member)

    def getMembers(self)->List:
        return self._memebers
