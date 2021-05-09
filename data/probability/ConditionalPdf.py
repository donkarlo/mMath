from typing import List, Callable

from mmath.data.probability.Pdf import Pdf

class ConditionalPdf(Pdf):
    def __init__(self, conditions:List[Callable]):
        pass