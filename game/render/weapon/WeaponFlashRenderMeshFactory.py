from game.anx.CommonConstants import CommonConstants
from game.calc.Ellipse import Ellipse
from game.gl.RenderModel3d import RenderMesh
from game.gl.VBOBuilderFactory import VBOBuilderFactory
from game.lib.Math import Math
from game.model.Material import Material
from game.render.common.TextureCollection import TextureCollection


class WeaponFlashRenderMeshFactory:

    def __init__(self, vboBuilderFactory, textureCollection):
        self.vboBuilderFactory = vboBuilderFactory
        self.textureCollection = textureCollection

    def makeRifleFlash(self):
        vboBuilder = self.vboBuilderFactory.makeVBOBuilder()

        ellipse = self.makeEllipse()
        ellipse.swapYZ()
        self.fillByEllipse(vboBuilder, ellipse)

        ellipse = self.makeEllipse()
        ellipse.rotateTo(Math.piHalf)
        ellipse.swapYZ()
        self.fillByEllipse(vboBuilder, ellipse)

        vbo = vboBuilder.build()

        return RenderMesh(vbo, self.textureCollection.rifleFlash, Material.weaponFlash)

    def makeEllipse(self):
        a = 0.1
        b = a / 6

        return Ellipse(a, b, 0, 0, a / 20)

    def fillByEllipse(self, vboBuilder, ellipse):
        leftX = -ellipse.a
        xlength = 2 * ellipse.a
        vertexCount = vboBuilder.getVertexCount()
        vboBuilder.addVertex(ellipse.center)
        vboBuilder.addNormal(CommonConstants.yAxis)
        vboBuilder.addTexCoord(0.5, 0.5)
        for point in ellipse.points:
            vboBuilder.addVertex(point)
            vboBuilder.addNormal(CommonConstants.yAxis)
            tx = (point.x - leftX) / xlength
            ty = 1 if point.y >= 0 else 0
            vboBuilder.addTexCoord(tx, ty)
        for i in range(1, len(ellipse.points)):
            vboBuilder.addFace(vertexCount, vertexCount + i, vertexCount + i + 1)


def makeWeaponFlashRenderMeshFactory(resolver):
    return WeaponFlashRenderMeshFactory(resolver.resolve(VBOBuilderFactory), resolver.resolve(TextureCollection))
