import uuid

from mDynamicSystem.state.State import State
from mMath.data.timeSerie.stochasticProcess.state.Serie import Serie
from mMath.data.timeSerie.stochasticProcess.state.StateSpace import StateSpace

from mMath.linearAlgebra.matrix.Matrix import Matrix


class TransitionMatrix(Matrix):
    '''
    '''
    def __init__(self, transitionDictionary: dict, stateSerie:Serie, stateSpace:StateSpace):
        '''

        :param transitionDictionary:
        :param stateSpace:
        '''
        self._transitionDictionary:dict = transitionDictionary
        self._stateSerie = stateSerie
        self._stateSpace = stateSpace

    def getNextMostProbableStateIdByStateId(self, stateId:State)->uuid.UUID:
        '''

        :param stateId:
        :return:
        '''
        maxStateId = list(self._transitionDictionary[stateId].keys())[0]
        for stateId in self._transitionDictionary[stateId]:
            if self._transitionDictionary[stateId][stateId]>self._transitionDictionary[stateId][maxStateId]:
                maxStateId = stateId
        return maxStateId

    def getTransitionDictionary(self)->dict:
        return self._transitionDictionary

    def getStateSpace(self):
        return self._stateSpace
