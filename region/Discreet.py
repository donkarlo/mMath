from typing import List, Set

from mMath.linearAlgebra.Vector import Vector
from mMath.region.Region import Region


class Discreet(Region):
    def __init__(self,points:List[Vector]=None):
        self._points:List[Vector] = points if points is not None else []
    def getPoints(self):
        return self._points
    def addPoint(self,point:Vector):
        #@todo not repapitive
        self._points.append(point)
