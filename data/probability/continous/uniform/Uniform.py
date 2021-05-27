from mMath.data.probability.discrete.Pdf import Pdf
from mMath.data.probability.event.Event import Event
from mMath.linearAlgebra.Vector import Vector


class Uniform(Pdf):
    def __init__(self,intrestedRegion):
        ''''''
        self._intrestedRegion = intrestedRegion

    def getSamples(self):
        ''''''
        pass

    def getValueByEvent(self, e:Event):
        ''''''
        pass