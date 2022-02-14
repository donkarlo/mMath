from mMath.trajectory.gen.ParamLinePointGenerator import *

from mMath.trajectory.ParamShapeLine import ParamShapeLine
from mMath.trajectory.gen.ParamShapePointGeneratorComposit import ParamShapePointGeneratorComposit


class Square30TurnInside5ParamShapePointGenerator(ParamShapePointGeneratorComposit):
    def __init__(self, distanceInterval):
        super().__init__()
        print("new points")

        l1 = ParamShapeLine([1, 0, 0], [-15, 15, 5])
        l1pg = ParamLinePointGenerator(l1, distanceInterval, 0, 30)
        l1pg.echoPoints()

        print("new points")
        #Go down 10 units
        l2First = ParamShapeLine([0, -1, 0], [15, 15, 5])
        l2FirstPg = ParamLinePointGenerator(l2First, distanceInterval, 0, 10)
        l2FirstPg.echoPoints()

        #Turn left
        l2Second = ParamShapeLine([-1, 0, 0], [15, 5, 5])
        l2SecondPg = ParamLinePointGenerator(l2Second, distanceInterval, 0, 5)
        l2SecondPg.echoPoints()

        #Go down in
        l2Third = ParamShapeLine([0, -1, 0], [10, 5, 5])
        l2ThirdPg = ParamLinePointGenerator(l2Third, distanceInterval, 0, 10)
        l2ThirdPg.echoPoints()

        #Turn right
        l2Forth = ParamShapeLine([1, 0, 0], [10, -5, 5])
        l2ForthPg = ParamLinePointGenerator(l2Forth, distanceInterval, 0, 5)
        l2ForthPg.echoPoints()

        #Continue to go down 13 units
        l2Fifth = ParamShapeLine([0, -1, 0], [15, -5, 5])
        l2FifthPg = ParamLinePointGenerator(l2Fifth, distanceInterval, 0, 10)
        l2FifthPg.echoPoints()

        print("new points")

        l3 = ParamShapeLine([-1, 0, 0], [15, -15, 5])
        l3pg = ParamLinePointGenerator(l3, distanceInterval, 0, 30)
        l3pg.echoPoints()

        print("new points")

        l4 = ParamShapeLine([0, 1, 0], [-15, -15, 5])
        l4pg = ParamLinePointGenerator(l4, distanceInterval, 0, 30)
        l4pg.echoPoints()

        self \
            .add(l1pg) \
            .add(l2FirstPg) \
            .add(l2SecondPg) \
            .add(l2ThirdPg) \
            .add(l2ForthPg) \
            .add(l2FifthPg) \
            .add(l3pg) \
            .add(l4pg)

if __name__ == '__main__':
    tspsg = Square30TurnInside5ParamShapePointGenerator(0.5)
    tspsg.plot3DPoints()
    tspsg.getPoints().addDim(0)
    tspsg.getPoints().echoFile("/home/donkarlo/Dropbox/projs/research/data/self-aware-drones/trajectory-points/square-30-turn-left-5-pcs-0-5.txt", " ")
