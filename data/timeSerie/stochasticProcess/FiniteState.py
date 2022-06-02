from typing import List

from mDynamicSystem.state.State import State


class FiniteState:
    def __init__(self,states:List[State]):
        self.__states = states
