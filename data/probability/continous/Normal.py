import math
from typing import List

from mMath.data.probability.Event import Event
from mMath.data.probability.Pdf import Pdf
from mMath.data.probability.continous.Gaussian import Gaussian
from mMath.linearAlgebra.Vector import Vector


class Normal(Gaussian):
    def __init__(self, mean: float, standardDeviation: float):
        ''''''
        mean:Vector = Vector(mean)
        standardDeviation:Vector = Vector(standardDeviation)
        super.__init__(mean,standardDeviation)

    def getValueByEvent(self, input:float)->float:
        ''''''
        event:Event= Event(Vector(input))
        y = super().getValueByEvent(event)
        return y
