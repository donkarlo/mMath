import abc
class Region():
    def __init__(self,boundries):
        self._boundries = boundries

    @abc.abstractmethod
    def getBoundries(self):
        pass