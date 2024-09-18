from game.calc.Vector3 import Vector3
from game.lib.Math import Math
from game.model.level.Orientation import Orientation


class WallVBOBuilder:

    def build(self, wall, vboBuilder):
        stepLength = 10
        if wall.orientation == Orientation.diagonal:
            stepLength /= Math.sqrt(2)
        points = Vector3.splitFromStartToEnd(wall.startPoint, wall.endPoint, stepLength)
        isCounterclockwise = self.isCounterclockwise(wall)
        for i in range(1, len(points)):
            self.addVertices(vboBuilder, wall, points[i - 1], points[i], isCounterclockwise)

    def addVertices(self, vboBuilder, wall, prevPoint, currentPoint, isCounterclockwise):
        vertexCount = vboBuilder.getVertexCount()

        prevUpPoint = prevPoint.copy()
        prevUpPoint.z += wall.height
        currentUpPoint = currentPoint.copy()
        currentUpPoint.z += wall.height

        vboBuilder.addVertex(prevPoint)
        vboBuilder.addVertex(prevUpPoint)
        vboBuilder.addVertex(currentPoint)
        vboBuilder.addVertex(currentUpPoint)

        vboBuilder.addNormal(wall.frontNormal)
        vboBuilder.addNormal(wall.frontNormal)
        vboBuilder.addNormal(wall.frontNormal)
        vboBuilder.addNormal(wall.frontNormal)

        vboBuilder.addTexCoord(0, 0)
        vboBuilder.addTexCoord(0, 1)
        vboBuilder.addTexCoord(1, 0)
        vboBuilder.addTexCoord(1, 1)

        if isCounterclockwise:
            vboBuilder.addFace(vertexCount, vertexCount + 3, vertexCount + 1)
            vboBuilder.addFace(vertexCount, vertexCount + 2, vertexCount + 3)
        else:
            vboBuilder.addFace(vertexCount, vertexCount + 1, vertexCount + 3)
            vboBuilder.addFace(vertexCount, vertexCount + 3, vertexCount + 2)

    def isCounterclockwise(self, wall):
        v = wall.frontNormal.copy()
        v.vectorProduct(wall.direction)

        return v.z > 0


def makeWallVBOBuilder(resolver):
    return WallVBOBuilder()
