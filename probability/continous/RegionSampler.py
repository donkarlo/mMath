from mMath.probability.discrete.Pdf import Pdf
from mMath.region.Region import Region


class RegionSampler():
    def __init__(self,pdf:Pdf,region:Region):
        self._pdf:Pdf = pdf
        self._region:Region = region

    def getSamples(self,sampleNum:int):
        return self._pdf.getSamples(sampleNum)