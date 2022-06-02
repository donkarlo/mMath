from mMath.trajectory.gen.ParamLinePointGenerator import *

from mMath.trajectory.ParamShapeLine import ParamShapeLine
from mMath.trajectory.gen.ParamShapePointGeneratorComposit import ParamShapePointGeneratorComposit


class RectangleParamShapePointGenerator(ParamShapePointGeneratorComposit):
    def __init__(self, distanceInterval):
        super().__init__()
        print("new points")

        l1 = ParamShapeLine([1, 0, 0], [0, 0, 5])
        l1pg = ParamLinePointGenerator(l1, distanceInterval, 0, 10)
        l1pg.echoPoints()

        print("new points")

        l2 = ParamShapeLine([0, 1, 0], [10, 0, 5])
        l2pg = ParamLinePointGenerator(l2, distanceInterval, 0, 10)
        l2pg.echoPoints()

        print("new points")

        l3 = ParamShapeLine([-1, 0, 0], [10, 10, 5])
        l3pg = ParamLinePointGenerator(l3, distanceInterval, 0, 10)
        l3pg.echoPoints()

        print("new points")

        l4 = ParamShapeLine([0, -1, 0], [0, 10, 5])
        l4pg = ParamLinePointGenerator(l4, distanceInterval, 0, 10)
        l4pg.echoPoints()

        self \
            .add(l1pg) \
            .add(l2pg) \
            .add(l3pg) \
            .add(l4pg)

if __name__ == '__main__':
    tspsg = RectangleParamShapePointGenerator(0.5)
    tspsg.plot3DPoints()
    tspsg.getPoints().addDim(0)
    tspsg.getPoints().echoFile("/home/donkarlo/mrs_workspace/src/trajectory_loader/sample_trajectories/rect-side-10-step-0-5.txt", " ")
