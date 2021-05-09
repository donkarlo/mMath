from mmath.data.cluster.gng.graph.Graph import Graph
from mmath.data.cluster.gng.clusteringStrgy.EuclideanClosestNodeClusteringStrgy import EuclideanClosestNodeClusteringStrgy
from mmath.data.cluster.gng.Gng import Gng
from mmath.data.cluster.gng.PlotBuilder import PlotBuilder as GngGraphPLotBuilder
from mmath.data.cluster.gng.examples.trajectory.ThreeDPosVelFile import ThreeDPosVelFile
from mmath.linearalgebra.Matrix import Matrix

class TrajectoryExample:
    def run(self):
        # Positional data
        fileDataBank = "/home/donkarlo/Dropbox/projs/research/data/self-aware-drones/ctumrs/two-step/manip/pos-vel-obs-from-gps.txt"
        t3dposVel = ThreeDPosVelFile(fileDataBank)
        inputNpMatrix = Matrix(t3dposVel.getNpArr(5000,1))

        # A GNG object with maximum 20 nodes and maximum 200 Iterations
        gng = Gng(inputNpMatrix, maxNodesNum=20,maxIterationsNum=200)
        # By graph Object you have acess to nodes, edges etc
        graph:Graph = gng.getGraph()
        # what are nodes reference vectors and how many nodes and edges exist
        graph.report()

        # Clustering input data points to groups, here Euclidean distance is used
        cluterStrgy = EuclideanClosestNodeClusteringStrgy()
        clusters = gng.getClusters(cluterStrgy)

        #Graph with each cluster having a unique color
        gngGraphPlotBuilder = GngGraphPLotBuilder(gng.getInpRowsMatrix(), gng.getGraph())
        gngGraphPlotBuilder.showAll3D(clusters)

te = TrajectoryExample()
te.run()
