from typing import List

from mMath.data.probability.event.Vector import Vector as MainEvent


class Event(MainEvent):
    def __init__(self,members:List):
        self.__members:List = members