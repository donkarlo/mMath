from mMath.trajectory.gen.ParamLinePointGenerator import *

from mMath.trajectory.ParamShapeLine import ParamShapeLine
from mMath.trajectory.gen.ParamShapePointGeneratorComposit import ParamShapePointGeneratorComposit


class LineFromX0ToStep05ReturnParamShapePointGenerator(ParamShapePointGeneratorComposit):
    def __init__(self, distanceInterval):
        super().__init__()
        print("new points")

        l1 = ParamShapeLine([1, 0, 0], [0, 0, 5])
        l1pg = ParamLinePointGenerator(l1, distanceInterval, 0, 20)
        l1pg.echoPoints()

        l2 = ParamShapeLine([-1, 0, 0], [20, 0, 5])
        l2pg = ParamLinePointGenerator(l2, distanceInterval, 0, 20)
        l2pg.echoPoints()



        self \
            .add(l1pg) \
            .add(l2pg)

if __name__ == '__main__':
    tspsg = LineFromX0ToStep05ReturnParamShapePointGenerator(0.5)
    tspsg.plot3DPoints()
    tspsg.getPoints().addDim(0)
    tspsg.getPoints().echoFile("/home/donkarlo/mrs_workspace/src/trajectory_loader/sample_trajectories/LineFromX0ToStep05Return.txt", " ")
