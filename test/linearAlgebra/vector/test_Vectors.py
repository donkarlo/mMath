import unittest
from unittest import TestCase

from mMath.linearAlgebra.Vector import Vector
from mMath.linearAlgebra.Vectors import Vectors


class TestVectors(TestCase):
    def test_getMeanVector(self):
        vec1 = Vector([1,2,3])
        vec2 = Vector([2,3,4])
        vec3 = Vector([3,4,5])
        vectors = Vectors([vec1,vec2,vec3])
        meanVector = vectors.getMeanVector()
        self.assertEqual(meanVector[0],2.0)
        self.assertEqual(meanVector[1], 3.0)


if __name__ == '__main__':
    unittest.main()