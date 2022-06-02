from typing import List

import numpy as np

from smt.sampling_methods import LHS

from mMath.data.probability.continous.uniform.Uniform import Uniform
from mMath.linearAlgebra.matrix.Matrix import Matrix


class HyperCube(Uniform):
    def getSamples(self,samplesNum:int,limits:List)->Matrix:
        xlimits = np.array(limits)
        sampling = LHS(xlimits=xlimits)
        samples = sampling(samplesNum)
        return Matrix(samples)