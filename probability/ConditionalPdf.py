from typing import List, Callable

from mMath.probability.Pdf import Pdf

class ConditionalPdf(Pdf):
    def __init__(self, conditions:List[Callable]):
        pass