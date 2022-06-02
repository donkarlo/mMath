from typing import List

from mMath.data.timeSerie.stochasticProcess.state.State import State
from mMath.data.timeSerie.stochasticProcess.state.StateSpace import StateSpace


class Serie:
    ''''''
    def __init__(self, stateList:List[State] = None, stateSpace:StateSpace=None):
        self._stateList:List[State] = stateList if stateList is not None else []
        self._stateSpace = stateSpace

    def getStates(self)->List[State]:
        return self._stateList

    def getLastState(self) -> State:
        ''''''
        return self._stateList[self.getLastStateIndex()]

    def getLastStateIndex(self):
        return len(self._stateList) - 1

    def getStateListUntilLastState(self)->List[State]:
        return self._stateList[1:self.getLastStateIndex()-1]

    def getStateByIndex(self, index:int):
        return self._stateList[index]

    def getLength(self):
        return len(self._stateList)

    def appendState(self, state: State):
        '''
        @todo check if it exists in States set
        :param state:
        :return:
        '''
        self._stateList.append(state)
