from mMath.data.timeSerie.stochasticProcess.StochasticProcess import StochasticProcess
from mMath.data.timeSerie.stochasticProcess.state.transitionMatrix.TransitionMatrix import TransitionMatrix
from mMath.data.timeSerie.stochasticProcess.state.Set import Set


class MarkovChain(StochasticProcess):
    ''''''
    def __init__(self, statesSet:Set, transitionMatrix:TransitionMatrix):
        self.__statesSet = statesSet
        self.transitionMatrix = transitionMatrix