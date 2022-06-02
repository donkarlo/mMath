from mDynamicSystem.state.State import State
from mMath.data.timeSerie.stochasticProcess.state.Serie import Serie as StateSerie
import numpy as np

from mMath.data.timeSerie.stochasticProcess.state.StateSpace import StateSpace
from mMath.data.timeSerie.stochasticProcess.state.transitionMatrix.TransitionMatrix import TransitionMatrix
from mMath.linearAlgebra.matrix.Matrix import Matrix


class FromStateSerieBuilder:
    ''''''
    def __init__(self, stateSerie:StateSerie, stateSet:StateSpace):
        '''
        :param stateSerie:
        '''
        self._stateSerie:StateSerie = stateSerie
        self._stateSet = stateSet
        self._dict = None

    def getTransitionMatrix(self):
        '''
        :return:
        '''
        self._dict:dict = {}

        for thisState in self._stateSerie.getStates():
            if thisState.getId() not in self._dict:
                self._dict[thisState.getId()] = {}
            for thatState in self._stateSerie.getStates():
                if thatState.getId() not in self._dict[thisState.getId()]:
                    self._dict[thisState.getId()][thatState.getId()]=0

        loopingState: State
        for stateCounter, loopingState in enumerate(self._stateSerie.getStates()):
            if stateCounter == 1:
                prevState: State = self._stateSerie.getStateByIndex(0)
                curState: State = self._stateSerie.getStateByIndex(1)

            if stateCounter >= 2:
                prevState:State = curState
                curState = loopingState

            if stateCounter >= 1:
                if prevState.getId() not in self._dict:
                    self._dict[prevState.getId()] = {}
                if curState.getId() not in self._dict[prevState.getId()]:
                    self._dict[prevState.getId()][curState.getId()] = 0
                self._dict[prevState.getId()][curState.getId()] += 1

        for rowKey in self._dict:
            for colKey in self._dict[rowKey]:
                self._dict[rowKey][colKey] = (self._dict[rowKey][colKey]) / (self._stateSerie.getLength() - 1)
        transitionMatrix = TransitionMatrix(self._dict,self._stateSerie,self._stateSet)
        return transitionMatrix
