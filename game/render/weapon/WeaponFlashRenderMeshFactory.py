from game.anx.CommonConstants import CommonConstants
from game.calc.Vector3 import Vector3
from game.gl.RenderModel3d import RenderMesh
from game.gl.VBOBuilderFactory import VBOBuilderFactory
from game.render.common.TextureCollection import TextureCollection


class WeaponFlashRenderMeshFactory:

    def __init__(self, vboBuilderFactory, textureCollection):
        self.vboBuilderFactory = vboBuilderFactory
        self.textureCollection = textureCollection

    def makeRifleFlash(self):
        vboBuilder = self.vboBuilderFactory.makeVBOBuilder()

        a = 0.1

        vboBuilder.addVertex(Vector3(-a, 0, -a))
        vboBuilder.addVertex(Vector3(a, 0, -a))
        vboBuilder.addVertex(Vector3(a, 0, a))
        vboBuilder.addVertex(Vector3(-a, 0, a))

        vboBuilder.addNormal(CommonConstants.yAxis)
        vboBuilder.addNormal(CommonConstants.yAxis)
        vboBuilder.addNormal(CommonConstants.yAxis)
        vboBuilder.addNormal(CommonConstants.yAxis)

        vboBuilder.addTexCoord(0, 0)
        vboBuilder.addTexCoord(1, 0)
        vboBuilder.addTexCoord(1, 1)
        vboBuilder.addTexCoord(0, 1)

        vboBuilder.addFace(0, 1, 2)
        vboBuilder.addFace(0, 2, 3)

        vbo = vboBuilder.build()

        return RenderMesh(vbo, self.textureCollection.rifleFlash, None)


def makeWeaponFlashRenderMeshFactory(resolver):
    return WeaponFlashRenderMeshFactory(resolver.resolve(VBOBuilderFactory), resolver.resolve(TextureCollection))
