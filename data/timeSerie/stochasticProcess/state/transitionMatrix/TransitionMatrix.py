from mDynamicSystem.state.State import State

from mMath.linearAlgebra.matrix.Matrix import Matrix


class TransitionMatrix(Matrix):
    def __init__(self, dictRows: dict):
        self.__dictRows = dictRows

    def getNextMostProbableStateByState(self, state:State):
        ''''''
        maxInColsOfARowState = max(self.__dictRows[state.getId()])
        return maxInColsOfARowState