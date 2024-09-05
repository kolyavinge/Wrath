from game.calc.Vector3Utils import Vector3Utils
from game.lib.Math import Math
from game.model.level.Orientation import Orientation


class WallVBOBuilder:

    def build(self, wall, vboBuilder):
        stepLength = 10
        if wall.orientation == Orientation.diagonal:
            stepLength /= Math.sqrt(2)
        points = Vector3Utils.splitFromStartToEnd(wall.startPoint, wall.endPoint, stepLength)
        for i in range(1, len(points)):
            self.addVertices(vboBuilder, wall, points[i - 1], points[i])

    def addVertices(self, vboBuilder, wall, prevPoint, currentPoint):
        vertexCount = vboBuilder.getVertexCount()

        prevUpPoint = prevPoint.copy()
        prevUpPoint.z += wall.height
        currentUpPoint = currentPoint.copy()
        currentUpPoint.z += wall.height

        vboBuilder.addVertex(prevPoint)
        vboBuilder.addVertex(prevUpPoint)
        vboBuilder.addVertex(currentUpPoint)
        vboBuilder.addVertex(currentPoint)

        vboBuilder.addNormal(wall.frontNormal)
        vboBuilder.addNormal(wall.frontNormal)
        vboBuilder.addNormal(wall.frontNormal)
        vboBuilder.addNormal(wall.frontNormal)

        vboBuilder.addTexCoord(0, 0)
        vboBuilder.addTexCoord(0, 1)
        vboBuilder.addTexCoord(1, 1)
        vboBuilder.addTexCoord(1, 0)

        vboBuilder.addFace(vertexCount, vertexCount + 1, vertexCount + 2)
        vboBuilder.addFace(vertexCount, vertexCount + 2, vertexCount + 3)


def makeWallVBOBuilder(resolver):
    return WallVBOBuilder()
