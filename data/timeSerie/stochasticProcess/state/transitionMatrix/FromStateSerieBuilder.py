from mDynamicSystem.state.State import State
from mMath.data.timeSerie.stochasticProcess.state.Serie import Serie as StateSerie
import numpy as np

from mMath.linearAlgebra.matrix.Matrix import Matrix


class FromStateSerieBuilder:
    ''''''
    def __init__(self,stateSerie:StateSerie):
        '''
        :param stateSerie:
        '''
        self.__stateSerie:StateSerie = stateSerie
        self.__dict = None

    def getTransitionNpMatrix(self):
        '''
        :return:
        '''
        self.__dict:dict = {}

        for thisState in self.__stateSerie.getStates():
            if thisState.getId() not in self.__dict:
                self.__dict[thisState.getId()] = {}
            for thatState in self.__stateSerie.getStates():
                if thatState.getId() not in self.__dict[thisState.getId()]:
                    self.__dict[thisState.getId()][thatState.getId()]=0

        loopingState: State
        for stateCounter, loopingState in enumerate(self.__stateSerie.getStates()):
            if stateCounter == 1:
                prevState: State = self.__stateSerie.getStateByIndex(0)
                curState: State = self.__stateSerie.getStateByIndex(1)

            if stateCounter >= 2:
                prevState:State = curState
                curState = loopingState

            if stateCounter >= 1:
                if prevState.getId() not in self.__dict:
                    self.__dict[prevState.getId()] = {}
                if curState.getId() not in self.__dict[prevState.getId()]:
                    self.__dict[prevState.getId()][curState.getId()] = 0
                self.__dict[prevState.getId()][curState.getId()] += 1

        for rowKey in self.__dict:
            for colKey in self.__dict[rowKey]:
                self.__dict[rowKey][colKey] = (self.__dict[rowKey][colKey])/(self.__stateSerie.getLength()-1)
        return self.__dict
