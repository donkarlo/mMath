from mMath.data.probability.discrete.Event import Event


class Event:
    def __init__(self,deligate):
        self._deligate = deligate
    def getDeligate(self):
        return self._deligate
    def conditionedOn(self, event:Event):
        pass