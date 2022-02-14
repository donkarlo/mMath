from mMath.data.cluster.gng.Cluster import Cluster as GngMainCluster
from mMath.data.cluster.gng.graph.Node import Node

class Cluster(GngMainCluster):
    '''This cluster has needs a node thats why a new class was needed'''
    def __init__(self,node:Node):
        '''

        :param node:
        '''
        super().__init__()
        #prototype
        self._node:Node = node

    def getNode(self)->Node:
        ''''''
        return self._node
