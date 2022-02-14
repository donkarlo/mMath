from mMath.trajectory.ParamShape import ParamShape


class ParamShapeLine(ParamShape):
    def __init__(self, normalVector, startPoint):
        # todo check the length of nVec is equal to length of cVec

        self._normalVector = normalVector if normalVector is not None else []
        self._startPoint = startPoint if startPoint is not None else []
        super().__init__("line")

    def getNormalVector(self):
        return self._normalVector

    def getStartPoint(self):
        return self._startPoint

    def getDim(self) -> int:
        return len(self._normalVector)
