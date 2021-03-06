from typing import List

import numpy as np

from mMath.data.cluster.gng.Cluster import Cluster
from mMath.data.cluster.ClusteringStrgy import ClusteringStrgy as MainClusteringStrgy
from mMath.data.cluster.gng.clusteringStrgy.ClusteringStrgy import ClusteringStrgy as GngClusteringStrgy
from mMath.data.cluster.gng.AdaptationPhase import AdaptationPhase
from mMath.data.cluster.gng.GrowingPhase import GrowingPhase
from mMath.algorithm.PhasableInterface import PhasableInterface
from mMath.data.cluster.gng.graph.Edge import Edge
from mMath.data.cluster.gng.graph.Graph import Graph
from mMath.data.cluster.gng.graph.Node import Node
from mMath.linearAlgebra.matrix.Matrix import Matrix
from mMath.linearAlgebra.Vector import Vector
from sklearn import preprocessing


class Gng(PhasableInterface,MainClusteringStrgy):
    '''Find how GNG works in AdaptationPhase and GrowingPhase'''

    def __init__(self,
                 inpRowsMatrix:Matrix,
                 maxNodesNum: int = 100,
                 maxAge: int = 100,
                 maxIterationsNum: int = 300,  # landa
                 localErrorDecayRate: float = 0.5,  # alpha
                 globalErrorDecayRate: float = 0.0005,  # beta
                 closestNodeMovementRateTowardCurInpVec: float = 0.05,  # eW
                 connectedNodesToClosestNodeMovementRateTowardCurInpVec: float = 0.0006  # eN
                 ):
        '''
        Parameters
        ----------
        inpRowsMatrix:np.array
        maxIterationsNum:int
        maxAge:int
        maxNodesNum:int
        alpha:
            local error decay rate.
        beta:
            global error decay rate.
        eW:
            winner node movement rate. normal valu =e is 0.05 and values greater than 0.3 are small and nodes in
            unstable graph.(e is abbr for epsilon)
        eN:
            neigbours of winner node movement rate, it must be much smaller than eW. should be one to tow orders of
            magnitude smaller than 0.0006
        '''
        # super().__init__(rawInputData)

        #it will be later converted to matrix
        self.__inpRowsMatrix: Matrix = inpRowsMatrix
        self.__closestNodeMovementRateTowardCurInpVec: float = closestNodeMovementRateTowardCurInpVec
        self.__neighborNodesOfClosestNodeMovementRateTowardCurInpVec: float = connectedNodesToClosestNodeMovementRateTowardCurInpVec
        self.__maxAge: int = maxAge
        self.__maxIterationsNum: int = maxIterationsNum
        self.__maxNodesStepNum: int = maxNodesNum
        self.__iterationCounter: int = 0
        self.__localErrorDecayRate: float = localErrorDecayRate
        self.__globalErrorDecayRate: float = globalErrorDecayRate
        self._clusters = None
        self.__graph: Graph = None
        self.__adaptationPhase = None
        self.__growingPhase = None
        #Will be set in getClusters
        self.__gngClusteringStrgy:GngClusteringStrgy = None

    def getClusters(self, gngClusteringStrgy:GngClusteringStrgy)->List[Cluster]:
        if type(self.__gngClusteringStrgy) == None or type(self.__gngClusteringStrgy) != type(gngClusteringStrgy):
            self.__gngClusteringStrgy = gngClusteringStrgy
            self._doSetClusters()
        return self._clusters

    def _doSetClusters(self):
        self._clusters = self.__gngClusteringStrgy.getClusters(self.getInpRowsMatrix(), self.getGraph())

    def _formGraph(self) -> None:
        ''''''
        print("Finding the graph's nodes and edges. Please wait ....")
        self.__prepareData()
        self.__initializePhases()
        self._initializeTheFirstTwoNodes()
        self._runPhases()

    def __prepareData(self) -> None:
        ''''''
        np.random.shuffle(self.__inpRowsMatrix.getNpRows())
        self.__normalizeInpRows()

    def __initializePhases(self) -> None:
        ''''''
        self.__adaptationPhase: AdaptationPhase = AdaptationPhase(self.__inpRowsMatrix
                                                                  , self.__graph
                                                                  , self.__closestNodeMovementRateTowardCurInpVec
                                                                  ,
                                                                  self.__neighborNodesOfClosestNodeMovementRateTowardCurInpVec
                                                                  , self.__maxAge)
        self.__growingPhase: GrowingPhase = GrowingPhase(self.__graph
                                                         , self.__localErrorDecayRate
                                                         , self.__globalErrorDecayRate)

    def _initializeTheFirstTwoNodes(self) -> None:
        '''Create two randomly positioned nodes, name them s(the winner node which is closer to bar(x)) and r '''
        node1RefVec: Vector = Vector(np.random.rand(self.__inpRowsMatrix.getColsNum(), 1))
        node1 = Node(node1RefVec, 0)
        self.__graph.addNode(node1)

        node2RefVec: Vector = Vector(np.random.rand(self.__inpRowsMatrix.getColsNum(), 1))
        node2 = Node(node2RefVec, 0)
        self.__graph.addNode(node2)

        edgeNode1Node2: Edge = Edge(node1, node2, 0)
        self.__graph.addEdge(edgeNode1Node2)

    def _runPhases(self) -> None:
        ''''''
        while self.__graph.getNodesNum() < self.__maxNodesStepNum:
            self.__adaptationPhase.run()
            if (self.__iterationCounter / self.__maxIterationsNum) == 1:
                self.__growingPhase.run()
                self.__iterationCounter = 0
            self.__iterationCounter += 1

    def __normalizeInpRows(self) -> None:
        '''Normalization of the input data'''
        # Extract minimum of each row
        minOfRowsArr = np.min(self.__inpRowsMatrix.getNpRows(), axis=0)
        # Construct an array by repeating A the number of times given by reps.
        # shape[0] gives the number of rows
        # tile: repeat array of minimums of each row one time along columns (axe1) and number of rows times of minOfRowsArr along rows(axe0)
        dataNorm = self.__inpRowsMatrix.getNpRows() - np.tile(minOfRowsArr, (self.__inpRowsMatrix.getNpRows().shape[0], 1))
        maxDataNorm = np.max(dataNorm, axis=0)
        self.__inpRowsMatrix.updateRows(dataNorm / np.tile(maxDataNorm, (self.__inpRowsMatrix.getNpRows().shape[0], 1)))
        #
        # min = np.amin(self.__inpRowsMatrix.getNpRows())
        # max = np.amax(self.__inpRowsMatrix.getNpRows())
        # npRowNorm = (self.__inpRowsMatrix.getNpRows()-min)/(max-min)
        # self.__inpRowsMatrix.updateRows(npRowNorm)



    def getInpRowsMatrix(self) -> Matrix:
        ''''''
        return self.__inpRowsMatrix

    def getGraph(self) -> Graph:
        ''''''
        if self.__graph is None:
            self.__graph = Graph()
            self._formGraph()
        return self.__graph
