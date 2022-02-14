import uuid
from random import sample
from typing import Set

from mMath.data.probability.discrete.Pdf import Pdf
from mMath.data.timeSerie.stochasticProcess.state.State import State
from mMath.data.timeSerie.stochasticProcess.state.StateSpace import StateSpace


class DiscreteStateSpace(StateSpace):
    def __init__(self, stateSpaceSet:Set=None):
        super().__init__()
        self._stateSpaceSet = stateSpaceSet if stateSpaceSet is not None else set()

    def addState(self,state:State):
        self._stateSpaceSet.add(state)

    def getLength(self)->int:
        return len(self._stateSpaceSet)

    def getStateSpaceSet(self)->Set:
        return self._stateSpaceSet

    def getStateByStateId(self,stateId:uuid.UUID):
        loopingState:State
        for loopingState in self._stateSpaceSet:
            if loopingState.getId()==stateId:
                return loopingState

    def getASample(self, pdf:Pdf=None):
        return sample(self._stateSpaceSet, 1)

    def getSample(self,sampleSize:int, pdf:Pdf=None):
        '''
        When pdf is not given then pdf is uniform
        :param sampleSize:
        :param pdf:
        :return:
        '''
        return sample(self._stateSpaceSet, sampleSize)
