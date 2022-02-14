from mMath.trajectory.gen.ParamLinePointGenerator import *

from mMath.trajectory.ParamShapeLine import ParamShapeLine
from mMath.trajectory.gen.ParamShapePointGeneratorComposit import ParamShapePointGeneratorComposit


class RectangleParamShapePointGenerator(ParamShapePointGeneratorComposit):
    def __init__(self, distanceInterval):
        super().__init__()

        l1 = ParamShapeLine([1, 0, 0], [0, 0, 10])
        l1pg = ParamLinePointGenerator(l1, distanceInterval, 0, 10)

        l2 = ParamShapeLine([0, 1, 0], [10, 0, 10])
        l2pg = ParamLinePointGenerator(l2, distanceInterval, 0, 3.33)

        l3 = ParamShapeLine([-1, 0, 0], [10, 3.33, 10])
        l3pg = ParamLinePointGenerator(l3, distanceInterval, 0, 3.33)

        l4 = ParamShapeLine([0, -1, 0], [6.66, 3.33, 10])
        l4pg = ParamLinePointGenerator(l4, distanceInterval, 0, 3.33)

        l5 = ParamShapeLine([-1, 0, 0], [6.66, 0, 10])
        l5pg = ParamLinePointGenerator(l5, distanceInterval, 0, 6.66)

        l6 = ParamShapeLine([0, 1, 0], [0, 0, 10])
        l6pg = ParamLinePointGenerator(l6, distanceInterval, 0, 10)

        l7 = ParamShapeLine([1, 0, 0], [0, 10, 10])
        l7pg = ParamLinePointGenerator(l7, distanceInterval, 0, 10)

        l8 = ParamShapeLine([0, -1, 0], [10, 10, 10])
        l8pg = ParamLinePointGenerator(l8, distanceInterval, 0, 3.33)

        l9 = ParamShapeLine([-1, 0, 0], [10, 6.66, 10])
        l9pg = ParamLinePointGenerator(l9, distanceInterval, 0, 3.33)

        l10 = ParamShapeLine([0, 1, 0], [6.66, 6.66, 10])
        l10pg = ParamLinePointGenerator(l10, distanceInterval, 0, 3.33)

        l11 = ParamShapeLine([-1, 0, 0], [6.66, 10, 10])
        l11pg = ParamLinePointGenerator(l11, distanceInterval, 0, 6.66)

        l12 = ParamShapeLine([0, -1, 0], [0, 10, 10])
        l12pg = ParamLinePointGenerator(l12, distanceInterval, 0, 10)

        self \
            .add(l1pg) \
            .add(l2pg) \
            .add(l3pg) \
            .add(l4pg) \
            .add(l5pg) \
            .add(l6pg) \
            .add(l7pg) \
            .add(l8pg) \
            .add(l9pg) \
            .add(l10pg) \
            .add(l11pg) \
            .add(l12pg) \

if __name__ == '__main__':
    tspsg = RectangleParamShapePointGenerator(0.5)
    tspsg.plot3DPoints()
    tspsg.getPoints().addDim(0)
    tspsg.getPoints().echoFile("/home/donkarlo/mrs_workspace/src/trajectory_loader/sample_trajectory/uturn-0-5.txt", " ")
