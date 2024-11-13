from OpenGL.GL import *

from game.gl.VBORenderer import VBORenderer
from game.render.weapon.WeaponFlashRenderCollection import WeaponFlashRenderCollection


class WeaponFlashRenderer:

    def __init__(self, renderCollection, vboRenderer):
        self.renderCollection = renderCollection
        self.vboRenderer = vboRenderer

    def render(self, shader, levelSegment):
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnable(GL_BLEND)
        glEnable(GL_ALPHA_TEST)

        for flash in levelSegment.weaponFlashes:
            mesh = self.renderCollection.getRenderMesh(flash.weaponType)
            shader.setModelMatrix(flash.getModelMatrix())
            shader.setMaterial(mesh.material)
            # shader.setAlpha(flash.alpha)
            # mesh.texture.bind(GL_TEXTURE0)
            self.vboRenderer.render(mesh.vbo)

        glDisable(GL_ALPHA_TEST)
        glDisable(GL_BLEND)


def makeWeaponFlashRenderer(resolver):
    return WeaponFlashRenderer(resolver.resolve(WeaponFlashRenderCollection), resolver.resolve(VBORenderer))
