import abc
class Kernel(abc.ABCMeta):
    def __init__(self):
        pass
    @abc.abstractmethod
    def getValue(self)->float:
        pass
