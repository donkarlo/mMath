from typing import List

from mMath.data.cluster.Cluster import Cluster as MainCluster
from mMath.data.cluster.gng.graph.Graph import Graph
from mMath.data.cluster.gng.clusteringStrgy.EuclideanClosestNode.ClusteringStrgy import ClusteringStrgy
from mMath.data.cluster.gng.Gng import Gng
from mMath.data.cluster.gng.PlotBuilder import PlotBuilder as GngGraphPLotBuilder
from mMath.data.cluster.gng.examples.trajectory.ThreeDPosVelFile import ThreeDPosVelFile
from mMath.linearAlgebra.matrix.Matrix import Matrix

class Trajectory:
    def __init__(self,dataSourceRowsNum):
        # Positional data
        # fileDataBank = "/home/donkarlo/Dropbox/projs/research/data/self-aware-drones/ctumrs/two-step/manip/pos-vel-obs-from-gps.txt"
        fileDataBank = "/home/donkarlo/Dropbox/projs/research/data/self-aware-drones/ctumrs/rect-10-0-5/manip-gps-3-d-pos-vel.txt"
        t3dposVel = ThreeDPosVelFile(fileDataBank)

        # coefficient 20 for velocities
        inputNpMatrix = Matrix(t3dposVel.getNpArr(dataSourceRowsNum, 1))

        # A GNG object with maximum 20 nodes and maximum 200 Iterations
        self.__gng = Gng(inputNpMatrix, maxNodesNum=20, maxIterationsNum=100)

    def getClusters(self):
        ''''''
        # By graph Object you have acess to nodes, edges etc
        graph:Graph = self.__gng.getGraph()
        # what are nodes reference vectors and how many nodes and edges exist
        graph.report()

        # Clustering input data points to groups, here Euclidean distance is used
        cluterStrgy = ClusteringStrgy()
        clusters:List[MainCluster] = self.__gng.getClusters(cluterStrgy)
        return clusters

    def plot(self):
        clusters = self.getClusters()
        #Graph with each cluster having a unique color
        gngGraphPlotBuilder = GngGraphPLotBuilder(self.__gng.getInpRowsMatrix(), self.__gng.getGraph())
        gngGraphPlotBuilder.showAll3D(clusters)

if __name__=="__main__":
    te = Trajectory(40000)
    te.plot()
