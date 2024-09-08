from game.anx.CommonConstants import CommonConstants


class StairVBOBuilder:

    def build(self, stair, vboBuilder):
        vertexCount = vboBuilder.getVertexCount()

        vboBuilder.addVertex(stair.downLeft)
        vboBuilder.addVertex(stair.upLeft)
        vboBuilder.addVertex(stair.downRight)
        vboBuilder.addVertex(stair.upRight)

        vboBuilder.addNormal(CommonConstants.up)
        vboBuilder.addNormal(CommonConstants.up)
        vboBuilder.addNormal(CommonConstants.up)
        vboBuilder.addNormal(CommonConstants.up)

        vboBuilder.addTexCoord(0, 0)
        vboBuilder.addTexCoord(0, 1)
        vboBuilder.addTexCoord(1, 0)
        vboBuilder.addTexCoord(1, 1)

        vboBuilder.addFace(vertexCount, vertexCount + 3, vertexCount + 1)
        vboBuilder.addFace(vertexCount, vertexCount + 2, vertexCount + 3)


def makeStairVBOBuilder(resolver):
    return StairVBOBuilder()
