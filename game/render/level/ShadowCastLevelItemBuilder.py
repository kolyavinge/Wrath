from game.gl.VBOBuilderFactory import VBOBuilderFactory
from game.model.FaceDirection import FaceDirection


class ShadowCastLevelItemBuilder:

    def __init__(self, vboBuilderFactory):
        self.vboBuilderFactory = vboBuilderFactory

    def buildForLevelSegment(self, levelSegment):
        vboBuilder = self.vboBuilderFactory.makeVBOBuilder()
        shadowCasters = [item for item in levelSegment.getAllItems() if item.canCastShadow]
        for item in shadowCasters:
            self.addVertices(vboBuilder, item)
        vbo = vboBuilder.build(withAdjacency=True)

        return vbo

    def addVertices(self, vboBuilder, item):
        vertexCount = vboBuilder.getVertexCount()

        vboBuilder.addVertex(item.downLeft)
        vboBuilder.addVertex(item.upLeft)
        vboBuilder.addVertex(item.downRight)
        vboBuilder.addVertex(item.upRight)

        vboBuilder.addNormal(item.frontNormal)
        vboBuilder.addNormal(item.frontNormal)
        vboBuilder.addNormal(item.frontNormal)
        vboBuilder.addNormal(item.frontNormal)

        if item.faceDirection == FaceDirection.counterClockwise:
            vboBuilder.addFace(vertexCount, vertexCount + 3, vertexCount + 1)
            vboBuilder.addFace(vertexCount, vertexCount + 2, vertexCount + 3)
        else:
            vboBuilder.addFace(vertexCount, vertexCount + 1, vertexCount + 3)
            vboBuilder.addFace(vertexCount, vertexCount + 3, vertexCount + 2)


def makeShadowCastLevelItemBuilder(resolver):
    return ShadowCastLevelItemBuilder(resolver.resolve(VBOBuilderFactory))
