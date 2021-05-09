from mmath.data.cluster.gng.clusteringStrgy.ClusteringStrgy import ClusteringStrgy as GngClusteringStrgy
from mmath.graph.Node import Node
from mmath.linearalgebra.Vector import Vector


class EuclideanClosestNodeClusteringStrgy(GngClusteringStrgy):
    def __init__(self):
        pass

    def _doSetClusters(self):
        closestNodesClusters = {}
        for loopingInpRow in self._inpDataRowsMatrix.getNpRows():
            loopingInpRowVec: Vector = Vector(loopingInpRow)
            nodeWithWithMinDsitance: Node = self._graph.getNodes()[0]
            for loopingNode in self._graph.getNodes():
                if loopingInpRowVec.getDistanceFrom(loopingNode.getRefVec()) < loopingInpRowVec.getDistanceFrom(nodeWithWithMinDsitance.getRefVec()):
                    nodeWithWithMinDsitance = loopingNode
            if nodeWithWithMinDsitance.getId() not in  closestNodesClusters:
                closestNodesClusters[nodeWithWithMinDsitance.getId()] = []
            closestNodesClusters[nodeWithWithMinDsitance.getId()].append(loopingInpRowVec)
        self._clusters = closestNodesClusters