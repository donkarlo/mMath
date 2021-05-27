from typing import List

from mMath.region.Region import Region


class HyperCube(Region):
    def __init__(self,boundries:List[float]):
        super().__init__(boundries)