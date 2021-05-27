from mMath.data.probability.event.Event import Event
from mMath.linearAlgebra.Vector import Vector


class PointEvent(Event):
    def __init__(self,point:Vector):
        self._delegate:Vector = point
