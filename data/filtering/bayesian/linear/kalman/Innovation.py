from linearalgebra import Matrix, Vector
from pgm.dag.dbn.tstbn.mjpf.abnormality.StrategyInterface import StrategyInterface as AbnormalityStrategy
from state import State
from state import Observation


class Innovation(AbnormalityStrategy):
    '''y^{~}_{k} = z_k-Hx^{^-}_{k}

    Parameters
    ----------

    Returns
    _______

    '''

    def __init__(self
                 , processMatrix: Matrix
                 , currentObservation: Observation
                 , priorCurrentEstimatedState: State):
        self._processMatrix = processMatrix
        self.__currentObservation = currentObservation
        self.__priorCurrentEstimatedState = priorCurrentEstimatedState

    def getInnovation(self) -> Vector:
        yK = self.__currentObservation - self.__processMatrix * self._priorCurrentEstimatedState
        return yK

