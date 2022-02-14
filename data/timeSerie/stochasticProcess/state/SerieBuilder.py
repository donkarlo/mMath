from typing import List

from mMath.data.timeSerie.stochasticProcess.state.Serie import Serie
from mMath.data.timeSerie.stochasticProcess.state.StateSpace import StateSpace
from mMath.data.timeSerie.stochasticProcess.state.State import State


class SerieBuilder:
    ''''''
    def __init__(self, stateSpace:StateSpace):
        self._stateList: List[State] = []
        self._stateSpace:StateSpace = stateSpace

    def appendState(self, state: State):
        '''
        @todo check if it exists in States set
        :param state:
        :return:
        '''
        self._stateList.append(state)

    def getSerie(self)->Serie:
        return Serie(self._stateList, self._stateSpace)
