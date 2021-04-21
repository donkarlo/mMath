import unittest
from unittest import TestCase

from data.cluster.gng.Gng import Gng
from data.cluster.gng.examples.trajectory.ThreeDPosVelFile import ThreeDPosVelFile
from linearalgebra.Matrix import Matrix


class TestGng(TestCase):
    # shared with all TestGng
    fileDataBank = "/home/donkarlo/Dropbox/projs/research/data/self-aware-drones/ctumrs/two-step/manip/pos-vel-obs-from-gps.txt"
    t3dposVel = ThreeDPosVelFile(fileDataBank)
    npInpRows = t3dposVel.getNpArr(1000)
    npInpRowsMatrix = Matrix(npInpRows)
    gng = Gng(npInpRowsMatrix, maxNodesNum=30)
    gng.getClusters()
    graph = gng.getGraph()

    def test_noEdglessNodesLeft(self):
        ''''''
        self.assertTrue(self.gng.getGraph().getEdgelessNodes() is None)

    def test_nodelessEdges(self):
        ''''''
        for edge in self.graph.getEdges():
            self.assertTrue(edge.getNode1() is not None and edge.getNode2() is not None)


if __name__ == '__main__':
    unittest.main()
