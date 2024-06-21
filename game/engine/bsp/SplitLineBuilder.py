from game.anx.Constants import Constants
from game.calc.Vector3 import Vector3
from game.engine.bsp.SplitLine import SplitLine
from game.model.level.Orientation import Orientation


class SplitLineBuilder:

    def getSplitLines(self, level):
        result = []
        self.makeFromFloors(level, result)
        self.makeFromWalls(level, result)

        return result

    def makeFromFloors(self, level, result):
        z = 0
        for floor in level.floors:
            s = SplitLine()
            s.priority = 0
            s.startPoint = Vector3(0, 0, z)
            s.endPoint = Vector3(0, 0, z)
            s.frontNormal = Constants.up
            s.orientation = Orientation.horizontal
            s.orientationCanChange = False
            s.sortOrder = z
            result.append(s)
            z += floor.height

    def makeFromWalls(self, level, result):
        for floor in level.floors:
            for wall in floor.walls:
                s = SplitLine()
                s.priority = 1
                s.startPoint = wall.startPoint
                s.endPoint = wall.endPoint
                s.frontNormal = wall.frontNormal
                s.orientation = wall.orientation
                s.orientationCanChange = True
                s.sortOrder = wall.startPoint.x if wall.orientation == Orientation.vertical else wall.startPoint.y
                result.append(s)


def makeSplitLineBuilder(resolver):
    return SplitLineBuilder()
