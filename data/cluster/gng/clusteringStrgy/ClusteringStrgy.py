from typing import List

from mMath.data.cluster.ClusteringStrgy import ClusteringStrgy as MainClusteringStrgy
from mMath.data.cluster.gng.Cluster import Cluster
from mMath.data.cluster.gng.graph.Graph import Graph
from mMath.linearAlgebra.Vector import Vector
from mMath.linearAlgebra.matrix.Matrix import Matrix


class ClusteringStrgy(MainClusteringStrgy):
    def __init__(self):
        pass

    def getClusters(self, inpDataRowsMatrix: Matrix, graph: Graph) -> List[Cluster]:
        self._graph: Graph = graph
        self._inpDataRowsMatrix = inpDataRowsMatrix
        self._doSetClusters()
        return self._clusters