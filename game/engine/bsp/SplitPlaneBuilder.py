from game.anx.CommonConstants import CommonConstants
from game.calc.Vector3 import Vector3
from game.engine.bsp.SplitPlane import SplitPlane
from game.model.level.FlatFloor import FlatFloor


class SplitLineBuilder:

    def getForCollisions(self, level):
        result = []
        self.makeFromFlatFloors(level, result)
        self.makeFromWalls(level, result)
        self.makeFromFloors(level, result)

        return result

    def makeFromFlatFloors(self, level, result):
        zlist = list(set([f.z if isinstance(f, FlatFloor) else 0 for f in level.floors]))
        for z in zlist:
            s = SplitPlane()
            s.priority = 0
            s.basePoint = Vector3(0, 0, z)
            s.frontNormal = CommonConstants.up
            result.append(s)

        s = SplitPlane()
        s.priority = 0
        s.basePoint = Vector3(0, 0, CommonConstants.maxLevelSize)
        s.frontNormal = CommonConstants.down
        result.append(s)

    def makeFromWalls(self, level, result):
        for wall in level.walls:
            s = SplitPlane()
            s.priority = 1
            s.basePoint = wall.startPoint
            s.frontNormal = wall.frontNormal
            result.append(s)

    def makeFromFloors(self, level, result):
        for floor in level.floors:
            s = SplitPlane()
            s.priority = 2
            s.basePoint = floor.downLeft
            s.frontNormal = floor.downFrontNormal
            result.append(s)

            s = SplitPlane()
            s.priority = 2
            s.basePoint = floor.downLeft
            s.frontNormal = floor.leftFrontNormal
            result.append(s)

            s = SplitPlane()
            s.priority = 2
            s.basePoint = floor.upRight
            s.frontNormal = floor.upFrontNormal
            result.append(s)

            s = SplitPlane()
            s.priority = 2
            s.basePoint = floor.upRight
            s.frontNormal = floor.rightFrontNormal
            result.append(s)


def makeSplitLineBuilder(resolver):
    return SplitLineBuilder()
