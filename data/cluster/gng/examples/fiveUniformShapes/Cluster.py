from mMath.data.cluster.gng.clusteringStrgy.EuclideanClosestNodeClusteringStrgy import EuclideanClosestNodeClusteringStrgy
from mMath.data.cluster.gng.Gng import Gng
from mMath.data.cluster.gng.PlotBuilder import PlotBuilder
from mMath.data.cluster.gng.examples.fiveUniformShapes.Builder import Builder
from mMath.linearalgebra.Matrix import Matrix

#All points can be
shapeBuilder = Builder()
allPoints = shapeBuilder.getAllPoints()
inpRowsMatrix = Matrix(allPoints)
gng = Gng(inpRowsMatrix,maxNodesNum=30,maxIterationsNum=50)
gng.getGraph().report()
plotter = PlotBuilder(gng.getInpRowsMatrix(),gng.getGraph())

cluterStrgy = EuclideanClosestNodeClusteringStrgy()
plotter.showAll2D()
