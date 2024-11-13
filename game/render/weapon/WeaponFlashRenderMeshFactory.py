from game.calc.Ellipse import Ellipse
from game.gl.RenderModel3d import RenderMesh
from game.gl.VBOBuilderFactory import VBOBuilderFactory
from game.lib.Math import Math
from game.model.Material import Material


class WeaponFlashRenderMeshFactory:

    def __init__(self, vboBuilderFactory):
        self.vboBuilderFactory = vboBuilderFactory

    def makeRifleFlash(self):
        vboBuilder = self.vboBuilderFactory.makeVBOBuilder()

        ellipse = self.makeEllipse()
        ellipse.swapYZ()
        self.fillByEllipse(vboBuilder, ellipse)

        ellipse = self.makeEllipse()
        ellipse.rotateTo(Math.piHalf)
        ellipse.swapYZ()
        self.fillByEllipse(vboBuilder, ellipse)

        # ellipse = self.makeEllipse()
        # ellipse.rotateTo(Math.pi)
        # ellipse.swapYZ()
        # self.fillByEllipse(vboBuilder, ellipse)

        # ellipse = self.makeEllipse()
        # ellipse.rotateTo(Math.threePiHalf)
        # ellipse.swapYZ()
        # self.fillByEllipse(vboBuilder, ellipse)

        vbo = vboBuilder.build()

        return RenderMesh(vbo, None, Material.weaponFlash)

    def makeEllipse(self):
        a = 0.1
        b = a / 5

        return Ellipse(a, b, 0, 0, 0.01)

    def fillByEllipse(self, vboBuilder, ellipse):
        vertexCount = vboBuilder.getVertexCount()
        vboBuilder.addVertex(ellipse.center)
        vboBuilder.addNormal(ellipse.center)
        vboBuilder.addTexCoord(0, 0)
        for point in ellipse.points:
            vboBuilder.addVertex(point)
            vboBuilder.addNormal(point)
            vboBuilder.addTexCoord(0, 0)
        for i in range(1, len(ellipse.points) - 1):
            vboBuilder.addFace(vertexCount, vertexCount + i, vertexCount + i + 1)


def makeWeaponFlashRenderMeshFactory(resolver):
    return WeaponFlashRenderMeshFactory(resolver.resolve(VBOBuilderFactory))
