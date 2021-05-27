import abc
class Population(abc.ABCMeta):
    def __init__(self):
        pass

    @abc.abstractmethod
    def getMean(self):
        pass

    @abc.abstractmethod
    def getStandardVariation(self):
        pass