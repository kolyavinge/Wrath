from OpenGL.GL import *

from game.engine.GameData import GameData
from game.gl.VBORenderer import VBORenderer
from game.render.common.ShaderProgramCollection import ShaderProgramCollection
from game.render.weapon.WeaponFlashRenderCollection import WeaponFlashRenderCollection


class WeaponFlashRenderer:

    def __init__(self, gameData, renderCollection, shaderProgramCollection, vboRenderer):
        self.gameData = gameData
        self.renderCollection = renderCollection
        self.shaderProgramCollection = shaderProgramCollection
        self.vboRenderer = vboRenderer

    def render(self):
        shader = self.shaderProgramCollection.texture
        shader.use()
        shader.setViewMatrix(self.gameData.camera.viewMatrix)
        shader.setProjectionMatrix(self.gameData.camera.projectionMatrix)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnable(GL_BLEND)
        glEnable(GL_ALPHA_TEST)
        glEnable(GL_DEPTH_TEST)

        for levelSegment in self.gameData.visibleLevelSegments:
            for flash in levelSegment.weaponFlashes:
                mesh = self.renderCollection.getRenderMesh(flash.weaponType)
                shader.setModelMatrix(flash.getModelMatrix())
                shader.setAlpha(flash.alpha)
                mesh.texture.bind(GL_TEXTURE0)
                self.vboRenderer.render(mesh.vbo)

        glDisable(GL_DEPTH_TEST)
        glDisable(GL_ALPHA_TEST)
        glDisable(GL_BLEND)
        shader.unuse()


def makeWeaponFlashRenderer(resolver):
    return WeaponFlashRenderer(
        resolver.resolve(GameData),
        resolver.resolve(WeaponFlashRenderCollection),
        resolver.resolve(ShaderProgramCollection),
        resolver.resolve(VBORenderer),
    )
