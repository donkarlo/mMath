from mMath.trajectory.gen.ParamLinePointGenerator import *

from mMath.trajectory.ParamShapeLine import ParamShapeLine
from mMath.trajectory.gen.ParamShapePointGeneratorComposit import ParamShapePointGeneratorComposit


class RectangleTurnLeftParamShapePointGenerator(ParamShapePointGeneratorComposit):
    def __init__(self, distanceInterval):
        super().__init__()
        print("new points")

        l1 = ParamShapeLine([1, 0, 0], [0, 0, 10])
        l1pg = ParamLinePointGenerator(l1, distanceInterval, 0, 3.33)
        l1pg.echoPoints()

        print("new points")

        l2 = ParamShapeLine([0, 1, 0], [3.33, 0, 10])
        l2pg = ParamLinePointGenerator(l2, distanceInterval, 0, 3.33)
        l2pg.echoPoints()

        print("new points")

        l3 = ParamShapeLine([1, 0, 0], [3.33, 3.33, 10])
        l3pg = ParamLinePointGenerator(l3, distanceInterval, 0, 3.33)
        l3pg.echoPoints()

        print("new points")

        l4 = ParamShapeLine([0, -1, 0], [6.66, 3.33, 10])
        l4pg = ParamLinePointGenerator(l4, distanceInterval, 0, 3.33)
        l4pg.echoPoints()

        print("new points")

        l5 = ParamShapeLine([1, 0, 0], [6.66, 0, 10])
        l5pg = ParamLinePointGenerator(l5, distanceInterval, 0, 3.33)
        l5pg.echoPoints()


        #############
        print("new points")

        l6 = ParamShapeLine([0, 1, 0], [10, 0, 10])
        l6pg = ParamLinePointGenerator(l6, distanceInterval, 0, 10)
        l6pg.echoPoints()

        print("new points")

        l7 = ParamShapeLine([-1, 0, 0], [10, 10, 10])
        l7pg = ParamLinePointGenerator(l7, distanceInterval, 0, 10)
        l7pg.echoPoints()

        print("new points")

        l8 = ParamShapeLine([0, -1, 0], [0, 10, 10])
        l8pg = ParamLinePointGenerator(l8, distanceInterval, 0, 10)
        l8pg.echoPoints()

        self \
            .add(l1pg) \
            .add(l2pg) \
            .add(l3pg) \
            .add(l4pg) \
            .add(l5pg) \
            .add(l6pg) \
            .add(l7pg) \
            .add(l8pg) \

if __name__ == '__main__':
    tspsg = RectangleTurnLeftParamShapePointGenerator(0.5)
    tspsg.plot3DPoints()
    tspsg.getPoints().addDim(0)
    tspsg.getPoints().echoFile("/home/donkarlo/mrs_workspace/src/trajectory_loader/sample_trajectory/my-rect-0-5-turn-left.txt", " ")
