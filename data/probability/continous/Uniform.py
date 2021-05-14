from mMath.data.pdf.Pdf import Pdf

from mMath.data.probability.Event import Event


class Uniform(Pdf):
    def __init__(self,lowerBand:float,higherBand:float,sampleDimention:int,samplesNum:int=1):
        ''''''
        self.__lowerBand = lowerBand
        self.__higherBand = higherBand
        self.__sampleDimention = sampleDimention
        self.__samplesNum = samplesNum

    def getSample(self):
        pass

    def getValueByEvent(self, e:Event):
        pass