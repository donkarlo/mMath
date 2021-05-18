from mMath.data.cluster.Cluster import Cluster as MainCluster
from mMath.data.cluster.gng.graph.Graph import Graph
from mMath.data.cluster.gng.clusteringStrgy.EuclideanClosestNode.ClusteringStrgy import ClusteringStrgy
from mMath.data.cluster.gng.Gng import Gng
from mMath.data.cluster.gng.PlotBuilder import PlotBuilder as GngGraphPLotBuilder
from mMath.data.cluster.gng.examples.trajectory.ThreeDPosVelFile import ThreeDPosVelFile
from mMath.linearAlgebra.matrix.Matrix import Matrix

class TrajectoryExample:
    ''''''
    def run(self):
        # Positional data
        fileDataBank = "/home/donkarlo/Dropbox/projs/research/data/self-aware-drones/ctumrs/two-step/manip/pos-vel-measurement-from-gps.txt"
        t3dposVel = ThreeDPosVelFile(fileDataBank)
        inputNpMatrix = Matrix(t3dposVel.getNpArr(5000,1))

        # A GNG object with maximum 20 nodes and maximum 200 Iterations
        gng = Gng(inputNpMatrix, maxNodesNum=50,maxIterationsNum=200)
        # By graph Object you have acess to nodes, edges etc
        graph:Graph = gng.getGraph()
        # what are nodes reference vectors and how many nodes and edges exist
        graph.report()

        # Clustering input data points to groups, here Euclidean distance is used
        cluterStrgy = ClusteringStrgy()
        clusters = gng.getClusters(cluterStrgy)

        #Graph with each cluster having a unique color
        gngGraphPlotBuilder = GngGraphPLotBuilder(gng.getInpRowsMatrix(), gng.getGraph())
        gngGraphPlotBuilder.showAll3D(clusters)


te = TrajectoryExample()
te.run()
