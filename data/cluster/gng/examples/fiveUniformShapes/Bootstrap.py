from mMath.data.cluster.gng.clusteringStrgy.EuclideanClosestNode.ClusteringStrgy import ClusteringStrgy
from mMath.data.cluster.gng.Gng import Gng
from mMath.data.cluster.gng.PlotBuilder import PlotBuilder
from mMath.data.cluster.gng.examples.fiveUniformShapes.Builder import Builder
from mMath.linearAlgebra.matrix.Matrix import Matrix

#All points can be
shapeBuilder = Builder()
allPoints = shapeBuilder.getAllPoints()
inpRowsMatrix = Matrix(allPoints)
gng = Gng(inpRowsMatrix,maxNodesNum=150,maxIterationsNum=300)
gng.getGraph().report()
plotter = PlotBuilder(gng.getInpRowsMatrix(),gng.getGraph())
plotter.showAll2D()
