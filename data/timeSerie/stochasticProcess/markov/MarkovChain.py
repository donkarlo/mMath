from mmath.data.timeSerie.stochasticProcess.StochasticProcess import StochasticProcess
from mmath.data.timeSerie.stochasticProcess.markov.SatesSet import StatesSet


class MarkovChain(StochasticProcess):
    ''''''
    def __init__(self,statesSet:StatesSet):
        self.__statesSet = statesSet
    def isMarkov(self,tolerance:float)->bool:
        pass
    def testMarkov(self)->float:
        '''How much the current state depends on previous state only'''
        pass