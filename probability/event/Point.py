from mMath.probability.event.Vector import Vector
from mMath.linearAlgebra.Vector import Vector


class PointEvent(Vector):
    def __init__(self,point:Vector):
        self._delegate:Vector = point
