import numpy as np
class ThreeDPosVelFile:
    def __init__(self, filePath: str):
        self.__filePath = filePath

    def getNpArr(self, maxRowsNum=None,velocityCoefficient=1,start:int=0):
        file = open(self.__filePath, "r")
        arr = np.empty((0, 6), np.float64)
        npRowListFloat64= None
        for lineCounter, curLine in enumerate(file):
            if maxRowsNum is not None and lineCounter > start+maxRowsNum:
                break
            if lineCounter>=start:
                npRowListStr = np.asarray([r for r in curLine.split(",")])
                npRowListFloat64 = npRowListStr.astype(np.float64)
                for componentCounter in [0,1,2,3,4,5]:
                    npRowListFloat64[componentCounter] = npRowListFloat64[componentCounter]
                    if componentCounter>=3:
                        npRowListFloat64[componentCounter] = velocityCoefficient*npRowListFloat64[componentCounter]
                arr = np.append(arr, [npRowListFloat64], axis=0)
        file.close()
        return np.asarray(arr)