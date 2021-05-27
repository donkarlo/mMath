import uuid

from mDynamicSystem.state.State import State

from mMath.linearAlgebra.matrix.Matrix import Matrix


class TransitionMatrix(Matrix):
    def __init__(self, dictRows: dict):
        self.__dictRows:dict = dictRows

    def getNextMostProbableStateIdByStateId(self, stateId:State)->uuid.UUID:
        ''''''
        maxStateId = list(self.__dictRows[stateId].keys())[0]
        for stateId in self.__dictRows[stateId]:
            if self.__dictRows[stateId][stateId]>self.__dictRows[stateId][maxStateId]:
                maxStateId = stateId
        return maxStateId