from mMath.data.probability.Event import Event
import abc

class Pdf:
    def __init__(self):
        ''''''
        pass

    @abc.abstractmethod
    def getValueByEvent(self,event:Event)->float:
        ''''''
        pass