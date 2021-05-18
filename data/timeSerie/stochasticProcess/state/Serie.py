from typing import List

from mMath.data.timeSerie.stochasticProcess.state import State


class Serie:
    ''''''
    def __init__(self, stateEventSequence:List[State]):
        self.__stateEventSequence:List[State] = stateEventSequence

    def getStateEventSequence(self) -> List[State]:
        return self.__stateEventSequence

    def getLastStateInStateEventSequence(self) -> State:
        ''''''
        return self.__stateEventSequence[self.getLastStateEventIndex()]

    def getLastStateEventIndex(self):
        return len(self.__stateEventSequence) - 1

    def getStateEventByIndex(self,index:int):
        return self.__stateEventSequence[0]