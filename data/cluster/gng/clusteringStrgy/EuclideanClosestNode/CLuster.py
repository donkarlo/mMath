from mMath.data.cluster.gng.Cluster import Cluster as GngMainCluster
from mMath.data.cluster.gng.graph.Node import Node


class Cluster(GngMainCluster):
    ''''''
    def __init__(self,node:Node):
        '''

        :param node:
        '''
        super().__init__()
        self.__node:Node = node

    def getNode(self)->Node:
        ''''''
        return self.__node