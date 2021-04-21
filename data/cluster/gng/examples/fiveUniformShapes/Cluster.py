from data.cluster.gng.Gng import Gng
from data.cluster.gng.PlotBuilder import PlotBuilder
from data.cluster.gng.examples.fiveUniformShapes.Builder import Builder
from linearalgebra.Matrix import Matrix

#All points can be
shapeBuilder = Builder()
allPoints = shapeBuilder.getAllPoints()
inpRowsMatrix = Matrix(allPoints)
gng = Gng(inpRowsMatrix,maxNodesNum=100)
gng.getClusters()
gng.getGraph().report()
plotter = PlotBuilder(gng.getInpRowsMatrix(),gng.getGraph())
plotter.showAll2D()
