from game.calc.Vector3 import Vector3


class WallVBOBuilder:

    def build(self, wall, vboBuilder):
        vertexCount = vboBuilder.getVertexCount()

        vboBuilder.addVertex(wall.startPoint)
        vboBuilder.addVertex(wall.upStartPoint)
        vboBuilder.addVertex(wall.upEndPoint)
        vboBuilder.addVertex(wall.endPoint)

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