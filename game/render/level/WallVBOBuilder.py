from game.calc.Vector3 import Vector3
from game.lib.Math import Math
from game.model.Orientation import Orientation
from game.render.level.ConstructionVBOBuilder import ConstructionVBOBuilder


class WallVBOBuilder(ConstructionVBOBuilder):

    def build(self, wall, vboBuilder):
        stepLength = self.getStepLength(wall)
        if wall.orientation == Orientation.diagonal:
            stepLength /= Math.sqrt(2.0)
        stepLength = Math.min(stepLength, wall.direction.getLength())
        points = Vector3.splitFromStartToEnd(wall.startPoint, wall.endPoint, stepLength)
        for i in range(1, len(points)):
            downLeft = points[i - 1]
            downRight = points[i]
            upLeft = downLeft.copy()
            upLeft.z += wall.height
            upRight = downRight.copy()
            upRight.z += wall.height
            self.addVertices(vboBuilder, wall, downLeft, downRight, upLeft, upRight)


def makeWallVBOBuilder(resolver):
    return WallVBOBuilder()
