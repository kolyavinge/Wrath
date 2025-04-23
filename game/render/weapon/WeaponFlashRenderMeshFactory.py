from game.anx.CommonConstants import CommonConstants
from game.calc.Vector3 import Vector3
from game.gl.model3d.RenderModel3d import RenderMesh
from game.gl.vbo.VBOBuilderFactory import VBOBuilderFactory
from game.render.common.TextureCollection import TextureCollection


class WeaponFlashRenderMeshFactory:

    def __init__(self, vboBuilderFactory, textureCollection):
        self.vboBuilderFactory = vboBuilderFactory
        self.textureCollection = textureCollection

    def makePistolFlash(self):
        return RenderMesh(self.makeQuadVBO(0.12), self.textureCollection.pistolFlash, None)

    def makeRifleFlash(self):
        return RenderMesh(self.makeQuadVBO(0.15), self.textureCollection.rifleFlash, None)

    def makeSniperFlash(self):
        return RenderMesh(self.makeQuadVBO(0.25), self.textureCollection.sniperFlash, None)

    def makeQuadVBO(self, size):
        vboBuilder = self.vboBuilderFactory.makeVBOBuilder()

        vboBuilder.addVertex(Vector3(-size, 0, -size))
        vboBuilder.addVertex(Vector3(size, 0, -size))
        vboBuilder.addVertex(Vector3(size, 0, size))
        vboBuilder.addVertex(Vector3(-size, 0, size))

        vboBuilder.addTexCoord(0, 0)
        vboBuilder.addTexCoord(1, 0)
        vboBuilder.addTexCoord(1, 1)
        vboBuilder.addTexCoord(0, 1)

        vboBuilder.addFace(0, 1, 2)
        vboBuilder.addFace(0, 2, 3)

        vbo = vboBuilder.build()

        return vbo


def makeWeaponFlashRenderMeshFactory(resolver):
    return WeaponFlashRenderMeshFactory(resolver.resolve(VBOBuilderFactory), resolver.resolve(TextureCollection))
