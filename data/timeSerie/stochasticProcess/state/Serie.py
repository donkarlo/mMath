from typing import List

from mMath.data.timeSerie.stochasticProcess.state.State import State


class Serie:
    ''''''
    def __init__(self, stateSequence:List[State]):
        self.__stateSequence:List[State] = stateSequence

    def getStates(self)->List[State]:
        return self.__stateSequence

    def getLastState(self) -> State:
        ''''''
        return self.__stateSequence[self.getLastStateIndex()]

    def getLastStateIndex(self):
        return len(self.__stateSequence) - 1

    def getStateByIndex(self, index:int):
        return self.__stateSequence[index]

    def getLength(self):
        return len(self.__stateSequence)
