from mMath.data.timeSerie.stochasticProcess.StochasticProcess import StochasticProcess
from mMath.data.timeSerie.stochasticProcess.state.transitionMatrix.TransitionMatrix import TransitionMatrix
from mMath.data.timeSerie.stochasticProcess.state.StateSpace import StateSpace


class MarkovChain(StochasticProcess):
    ''''''
    def __init__(self, statesSet:StateSpace, transitionMatrix:TransitionMatrix):
        self.__statesSet = statesSet
        self.transitionMatrix = transitionMatrix