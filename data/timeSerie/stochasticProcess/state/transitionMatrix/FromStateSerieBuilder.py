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
        self.__stateSerie = stateSerie
        self.__dict = None

    def getTransitionNpMatrix(self):
        '''
        :return:
        '''
        self.__dict = {}
        loopingState: State
        curState: State = self.__stateSerie.getStateEventByIndex(0)
        prevState: State = self.__stateSerie.getStateEventByIndex(0)
        for stateCounter, loopingState in enumerate(self.__stateSerie.getStateEventSequence()):
            prevState = curState
            curState = loopingState
            try:
                self.__dict[prevState.getId()][curState.getId()]
            except:
                self.__dict.update({prevState.getId(): {curState.getId(): 0}})
            self.__dict[prevState.getId()][curState.getId()] += 1
        return Matrix(np.array(self.__dict))
