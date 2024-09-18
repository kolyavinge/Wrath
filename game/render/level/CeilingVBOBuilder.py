from game.render.level.FloorVBOBuilder import FloorVBOBuilder


class CeilingVBOBuilder(FloorVBOBuilder):

    def addVertices(self, vboBuilder, ceiling, downLeft, downRight, upLeft, upRight):
        vertexCount = vboBuilder.getVertexCount()

        vboBuilder.addVertex(downLeft)
        vboBuilder.addVertex(upLeft)
        vboBuilder.addVertex(downRight)
        vboBuilder.addVertex(upRight)

        vboBuilder.addNormal(ceiling.frontNormal)
        vboBuilder.addNormal(ceiling.frontNormal)
        vboBuilder.addNormal(ceiling.frontNormal)
        vboBuilder.addNormal(ceiling.frontNormal)

        vboBuilder.addTexCoord(0, 0)
        vboBuilder.addTexCoord(0, 1)
        vboBuilder.addTexCoord(1, 0)
        vboBuilder.addTexCoord(1, 1)

        vboBuilder.addFace(vertexCount, vertexCount + 1, vertexCount + 3)
        vboBuilder.addFace(vertexCount, vertexCount + 3, vertexCount + 2)


def makeCeilingVBOBuilder(resolver):
    return CeilingVBOBuilder()
