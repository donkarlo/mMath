from typing import List

from mMath.data.timeSerie.stochasticProcess.markov.state.Serie import Serie
from mMath.data.timeSerie.stochasticProcess.markov.state.Set import Set
from mMath.data.timeSerie.stochasticProcess.markov.state.State import State


class Builder:
    ''''''
    def __init__(self,stateSet:Set):
        self.__stateEventSequence: List[State] = None
        self.__stateSet:Set = stateSet

    def appendStateEvent(self, state: State):
        '''
        @todo check if it exists in States set
        :param state:
        :return:
        '''
        self.__stateEventSequence.append(state)

    def getSerie(self):
        return Serie(self.__stateEventSequence)
