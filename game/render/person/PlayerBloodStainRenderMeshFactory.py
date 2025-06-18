from game.calc.Vector3 import Vector3
from game.gl.model3d.RenderModel3d import RenderMesh
from game.gl.vbo.VBOBuilderFactory import VBOBuilderFactory
from game.render.common.TextureCollection import TextureCollection


class PlayerBloodStainRenderMeshFactory:

    def __init__(
        self,
        vboBuilderFactory: VBOBuilderFactory,
        textureCollection: TextureCollection,
    ):
        self.vboBuilderFactory = vboBuilderFactory
        self.textureCollection = textureCollection

    def make(self):
        return RenderMesh(self.makeQuadVBO(300), self.textureCollection.bloodStain1, None)

    def makeQuadVBO(self, size):
        vboBuilder = self.vboBuilderFactory.makeVBOBuilder()

        vboBuilder.addVertex(Vector3(-size, -size, 0))
        vboBuilder.addVertex(Vector3(size, -size, 0))
        vboBuilder.addVertex(Vector3(size, size, 0))
        vboBuilder.addVertex(Vector3(-size, size, 0))

        vboBuilder.addTexCoord(0, 0)
        vboBuilder.addTexCoord(1, 0)
        vboBuilder.addTexCoord(1, 1)
        vboBuilder.addTexCoord(0, 1)

        vboBuilder.addFace(0, 1, 2)
        vboBuilder.addFace(0, 2, 3)

        vbo = vboBuilder.build()

        return vbo
