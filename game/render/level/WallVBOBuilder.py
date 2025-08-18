from game.calc.Vector3 import Vector3
from game.lib.Math import Math
from game.model.Orientation import Orientation
from game.render.level.ConstructionVBOBuilder import ConstructionVBOBuilder


class WallVBOBuilder(ConstructionVBOBuilder):

    def buildSplitted(self, wall, vboBuilder):
        stepLength = wall.visualSize
        if wall.orientation == Orientation.diagonal:
            stepLength /= Math.sqrt(2.0)
        stepLength = Math.min(stepLength, wall.direction.getLength())
        downPoints = list(Vector3.fromStartToEnd(wall.frontDownLeft, wall.frontDownRight, stepLength))
        upPoints = list(Vector3.fromStartToEnd(wall.frontUpLeft, wall.frontUpRight, stepLength))
        for i in range(1, len(downPoints)):
            downLeft = downPoints[i - 1]
            downRight = downPoints[i]
            upLeft = upPoints[i - 1]
            upRight = upPoints[i]
            self.addVertices(vboBuilder, wall, downLeft, downRight, upLeft, upRight)
