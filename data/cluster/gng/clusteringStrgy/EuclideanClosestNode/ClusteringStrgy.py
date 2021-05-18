from typing import List

from mMath.data.cluster.gng.clusteringStrgy.ClusteringStrgy import ClusteringStrgy as GngClusteringStrgy
from mMath.data.cluster.gng.clusteringStrgy.EuclideanClosestNode.CLuster import Cluster
from mMath.graph.Node import Node
from mMath.linearAlgebra.Vector import Vector


class ClusteringStrgy(GngClusteringStrgy):
    def __init__(self):
        pass

    def _doSetClusters(self):
        '''
        It returns a dictionary so that the keys are node ids
        :return:dict a ditionary of clusters whose keys are nodes' ids
        '''
        closestNodesClusters:List[Cluster] = {}
        for loopingInpRow in self._inpDataRowsMatrix.getNpRows():
            loopingInpRowVec: Vector = Vector(loopingInpRow)
            nodeWithMinDsitance: Node = self._graph.getNodes()[0]
            for loopingNode in self._graph.getNodes():
                if loopingInpRowVec.getDistanceFrom(loopingNode.getRefVec()) < loopingInpRowVec.getDistanceFrom(nodeWithMinDsitance.getRefVec()):
                    nodeWithMinDsitance = loopingNode
            if nodeWithMinDsitance.getId() not in  closestNodesClusters:
                closestNodesClusters[nodeWithMinDsitance.getId()] = Cluster(nodeWithMinDsitance)
            closestNodesClusters[nodeWithMinDsitance.getId()].appendVector(loopingInpRowVec)
        self._clusters = closestNodesClusters
