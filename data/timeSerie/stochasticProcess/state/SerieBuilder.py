from typing import List

from mMath.data.timeSerie.stochasticProcess.state.Serie import Serie
from mMath.data.timeSerie.stochasticProcess.state.Set import Set
from mMath.data.timeSerie.stochasticProcess.state.State import State


class SerieBuilder:
    ''''''
    def __init__(self,stateSet:Set=None):
        self.__stateSequence: List[State] = []
        self.__stateSet:Set = stateSet

    def appendState(self, state: State):
        '''
        @todo check if it exists in States set
        :param state:
        :return:
        '''
        self.__stateSequence.append(state)

    def getSerie(self):
        return Serie(self.__stateSequence)
