from mDynamicSystem.state.State import State
from mMath.data.timeSerie.stochasticProcess.markov.state.Serie import Serie as StateSerie


class TransitionMatrixFromStatesSerieBuilder:
    def __init__(self,stateSerie:StateSerie):
        self.__stateSerie = stateSerie

    def getTransitionDictionary(self):
        self.__dict = {}
        loopingSTate: State
        curState: State = self.__stateSerie.getStateEventByIndex(0)
        prevState: State = self.__stateSerie.getStateEventByIndex(0)
        for stateCounter, loopingSTate in enumerate(self.__stateSerie.getStateEventSequence()):
            prevState = curState
            curState = loopingSTate
            try:
                self.__dict[prevState.getId()][curState.getId()]
            except:
                self.__dict.update({prevState.getId(): {curState.getId(): 0}})
            self.__dict[prevState.getId()][curState.getId()] += 1
        return self.__dict
