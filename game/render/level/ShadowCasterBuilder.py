from game.gl.vbo.VBOBuilderFactory import VBOBuilderFactory


class ShadowCasterBuilder:

    def __init__(self, vboBuilderFactory: VBOBuilderFactory):
        self.vboBuilderFactory = vboBuilderFactory

    def buildForLevelSegment(self, levelSegment):
        # TODO не работают тени от персонажей, оружия и паверапов
        shadowCasters = [item for item in levelSegment.getAllVisibleItems() if item.canCastShadow]
        if len(shadowCasters) > 0:
            vboBuilder = self.vboBuilderFactory.makeVBOBuilder()
            for item in shadowCasters:
                self.addVertices(vboBuilder, item)
            vbo = vboBuilder.build(withAdjacency=True)

            return vbo
        else:
            return None

    def addVertices(self, vboBuilder, item):
        vertexCount = vboBuilder.getVertexCount()

        vboBuilder.addVertex(item.frontDownLeft)
        vboBuilder.addVertex(item.frontUpLeft)
        vboBuilder.addVertex(item.frontDownRight)
        vboBuilder.addVertex(item.frontUpRight)

        vboBuilder.addNormal(item.frontNormal)
        vboBuilder.addNormal(item.frontNormal)
        vboBuilder.addNormal(item.frontNormal)
        vboBuilder.addNormal(item.frontNormal)

        vboBuilder.addFace(vertexCount, vertexCount + 3, vertexCount + 1)
        vboBuilder.addFace(vertexCount, vertexCount + 2, vertexCount + 3)
