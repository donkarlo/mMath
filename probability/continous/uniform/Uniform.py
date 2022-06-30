from mMath.probability.discrete.Pdf import Pdf
from mMath.linearAlgebra.Vector import Vector


class Uniform(Pdf):
    def __init__(self,intrestedRegion):
        ''''''
        self._intrestedRegion = intrestedRegion

    def getSamples(self):
        ''''''
        pass

    def getValueByEvent(self, e:Vector):
        ''''''
        pass