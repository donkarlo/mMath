from mMath.data.cluster.Cluster import Cluster as MainCluster
from mMath.linearAlgebra.Vector import Vector


class Cluster(MainCluster):
    def __init__(self):
        super().__init__()

    def getMeanVector(self):
        componentWiseSum = {}
        for vectorCounter,vector in enumerate(self.getVectors()):
            for componentCounter,component in enumerate(vector):
                if componentWiseSum[componentCounter] is None:
                    componentWiseSum[componentCounter]=0
                else:
                    componentWiseSum[componentCounter]+=component[0]

        meanVectorArray = []
        for componentCounter,componentWiseSum in enumerate(componentWiseSum):
            meanVectorArray.append([componentWiseSum/len(self.getVectors())])

        return Vector(meanVectorArray)

    def getMedian(self):
        pass

    def getStd(self):
        pass
