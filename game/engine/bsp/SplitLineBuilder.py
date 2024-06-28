from game.anx.Constants import Constants
from game.calc.Vector3 import Vector3
from game.engine.bsp.SplitLine import SplitLine
from game.model.level.FlatFloor import FlatFloor
from game.model.level.Orientation import Orientation


class SplitLineBuilder:

    def getForCollisions(self, level):
        result = []
        self.makeFromFlatFloors(level, result)
        self.makeFromWalls(level, result)
        self.makeFromFloors(level, result)

        return result

    def getForVisibility(self, level):
        result = []
        self.makeFromFlatFloors(level, result)
        self.makeFromWalls(level, result)

        return result

    def makeFromFlatFloors(self, level, result):
        zlist = set([f.z if isinstance(f, FlatFloor) else 0 for f in level.floors])
        for z in zlist:
            s = SplitLine()
            s.priority = 0
            s.startPoint = Vector3(0, 0, z)
            s.endPoint = Vector3(0, 0, z)
            s.frontNormal = Constants.up
            s.orientation = Orientation.horizontal
            s.orientationCanChange = False
            s.sortOrder = z
            result.append(s)

        s = SplitLine()
        s.priority = 0
        s.startPoint = Vector3(0, 0, Constants.maxLevelSize)
        s.endPoint = Vector3(0, 0, Constants.maxLevelSize)
        s.frontNormal = Constants.down
        s.orientation = Orientation.horizontal
        s.orientationCanChange = False
        s.sortOrder = Constants.maxLevelSize
        result.append(s)

    def makeFromWalls(self, level, result):
        for wall in level.walls:
            if wall.orientation == Orientation.horizontal or wall.orientation == Orientation.vertical:
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
