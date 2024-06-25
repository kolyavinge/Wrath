from game.anx.Constants import Constants
from game.calc.Vector3 import Vector3
from game.engine.bsp.SplitLine import SplitLine
from game.model.level.Orientation import Orientation


class SplitLineBuilder:

    def getSplitLines(self, level):
        result = []
        self.makeFromWalls(level, result)
        self.makeFromFloors(level, result)

        return result

    def makeFromWalls(self, level, result):
        for wall in level.walls:
            s = SplitLine()
            s.priority = 1
            s.startPoint = wall.startPoint
            s.endPoint = wall.endPoint
            s.frontNormal = wall.frontNormal
            s.orientation = wall.orientation
            s.orientationCanChange = True
            s.sortOrder = wall.startPoint.x if wall.orientation == Orientation.vertical else wall.startPoint.y
            result.append(s)

    def makeFromFloors(self, level, result):
        for floor in level.floors:
            s = SplitLine()
            s.priority = 2
            s.startPoint = floor.downLeft
            s.endPoint = floor.downRight
            s.frontNormal = floor.downFrontNormal
            s.orientation = Orientation.horizontal
            s.orientationCanChange = True
            s.sortOrder = floor.downLeft.y
            result.append(s)

            s = SplitLine()
            s.priority = 2
            s.startPoint = floor.upLeft
            s.endPoint = floor.upRight
            s.frontNormal = floor.upFrontNormal
            s.orientation = Orientation.horizontal
            s.orientationCanChange = True
            s.sortOrder = floor.upLeft.y
            result.append(s)

            s = SplitLine()
            s.priority = 2
            s.startPoint = floor.downLeft
            s.endPoint = floor.upLeft
            s.frontNormal = floor.leftFrontNormal
            s.orientation = Orientation.vertical
            s.orientationCanChange = True
            s.sortOrder = floor.downLeft.x
            result.append(s)

            s = SplitLine()
            s.priority = 2
            s.startPoint = floor.downRight
            s.endPoint = floor.upRight
            s.frontNormal = floor.rightFrontNormal
            s.orientation = Orientation.vertical
            s.orientationCanChange = True
            s.sortOrder = floor.downRight.x
            result.append(s)


def makeSplitLineBuilder(resolver):
    return SplitLineBuilder()
