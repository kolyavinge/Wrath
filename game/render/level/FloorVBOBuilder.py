class FloorVBOBuilder:

    def build(self, floor, vboBuilder):
        vertexCount = vboBuilder.getVertexCount()

        vboBuilder.addVertex(floor.downLeft)
        vboBuilder.addVertex(floor.upLeft)
        vboBuilder.addVertex(floor.upRight)
        vboBuilder.addVertex(floor.downRight)

        vboBuilder.addNormal(floor.upNormal)
        vboBuilder.addNormal(floor.upNormal)
        vboBuilder.addNormal(floor.upNormal)
        vboBuilder.addNormal(floor.upNormal)

        vboBuilder.addTexCoord(0, 0)
        vboBuilder.addTexCoord(0, 1)
        vboBuilder.addTexCoord(1, 1)
        vboBuilder.addTexCoord(1, 0)

        vboBuilder.addFace(vertexCount, vertexCount + 1, vertexCount + 2)
        vboBuilder.addFace(vertexCount, vertexCount + 2, vertexCount + 3)


def makeFloorVBOBuilder(resolver):
    return FloorVBOBuilder()
