from typing import Tuple

from mMath.data.probability.event.Event import Event as MainEvent
class Event(MainEvent):
    def __init__(self,members:Tuple):
        self.__members:Tuple= None