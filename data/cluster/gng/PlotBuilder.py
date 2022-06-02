import random as rand

from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D

from mMath.data.cluster.gng.graph.Graph import Graph
from mMath.data.cluster.gng.graph.PlotBuilder import PlotBuilder as GraphPlotBuilder
from mMath.linearAlgebra.matrix.Matrix import Matrix


class PlotBuilder(GraphPlotBuilder):
    def __init__(self, inpRowsMatrix: Matrix, graph: Graph):
        ''''''
        super().__init__(graph)
        self.__inpRowsMatrix: Matrix = inpRowsMatrix

    def add2DInpRowsMatrixScatter(self):
        ''''''
        xInpVecs = self.__inpRowsMatrix.getNpColByIndex(0)
        yInpVecs = self.__inpRowsMatrix.getNpColByIndex(1)
        self.getPlot().scatter(xInpVecs, yInpVecs, marker='.', c='lightblue')

    def showAll2D(self):
        ''''''
        self.add2DInpRowsMatrixScatter()
        self.add2DNodes()
        self.add2DEdges()
        self.getPlot().show()

    def showAll3D(self,clusters:dict):
        '''

        :param clusters:dict
        :return:
        '''
        fig = pyplot.figure()
        ax = Axes3D(fig)

        # Raw Data
        # xInpVecs = self.__inpRowsMatrix.getNpColByIndex(0)
        # yInpVecs = self.__inpRowsMatrix.getNpColByIndex(1)
        # zInpVecs = self.__inpRowsMatrix.getNpColByIndex(2)
        # ax.scatter(xInpVecs, yInpVecs, zInpVecs, c='lightblue', marker='.', alpha=0.04, linewidth=5)

        for clusterId in clusters:
            clusterMatrix:Matrix = Matrix(clusters[clusterId].getVectors().getVectorsList())
            xClusterInpVecs = clusterMatrix.getNpColByIndex(0)
            yClusterInpVecs = clusterMatrix.getNpColByIndex(1)
            zClusterInpVecs = clusterMatrix.getNpColByIndex(2)
            # @todo un/comment this line for 3d
            ax.scatter(xClusterInpVecs, yClusterInpVecs, zClusterInpVecs, color=self.__getRandomColor(), marker='.', alpha=0.04, linewidth=5)
            #@todo un/comment this line for 2d
            # ax.scatter(xClusterInpVecs, yClusterInpVecs, color=self.__getRandomColor(), marker='.', alpha=0.04, linewidth=5)

        #nodes
        xNodes = self.__graph.getNpNodesComponentsByIndex(0)
        yNodes = self.__graph.getNpNodesComponentsByIndex(1)
        zNodes = self.__graph.getNpNodesComponentsByIndex(2)
        ax.scatter(xNodes, yNodes, zNodes,facecolors='orange', edgecolors='r', s=100)

        #Edges
        for edge in self.__graph.getEdges():
            edgeNode1 = edge.getNode1()
            edgeNode2 = edge.getNode2()
            xVals = [edgeNode1.getRefVec().getComponentByIndex(0), edgeNode2.getRefVec().getComponentByIndex(0)]
            yVals = [edgeNode1.getRefVec().getComponentByIndex(1), edgeNode2.getRefVec().getComponentByIndex(1)]
            zVals = [edgeNode1.getRefVec().getComponentByIndex(2), edgeNode2.getRefVec().getComponentByIndex(2)]
            ax.plot(xVals, yVals,zVals, linewidth=3,c="orange")


        pyplot.show()

    def __getRandomColor(self):
        return [rand.uniform(0, 1.0) for i in [1, 2, 3]]
