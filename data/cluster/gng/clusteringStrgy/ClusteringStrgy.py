from typing import List

from mMath.data.cluster.ClusteringStrgy import ClusteringStrgy as MainClusteringStrgy
from mMath.data.cluster.gng.graph.Graph import Graph
from mMath.linearalgebra.Matrix import Matrix


class ClusteringStrgy(MainClusteringStrgy):
    def __init__(self):
        pass

    def getClusters(self, inpDataRowsMatrix: Matrix, graph: Graph) -> List:
        self._graph: Graph = graph
        self._inpDataRowsMatrix = inpDataRowsMatrix
        self._doSetClusters()
        return self._clusters