from OpenGL.GL import *

from game.calc.TransformMatrix4 import TransformMatrix4
from game.engine.GameData import GameData
from game.gl.ext import glGetViewportSize
from game.gl.TextRenderer import TextRenderer
from game.render.common.ShaderProgramCollection import ShaderProgramCollection


class DashboardRenderer:

    def __init__(self, gameData, shaderProgramCollection, textRenderer):
        self.gameData = gameData
        self.shaderProgramCollection = shaderProgramCollection
        self.textRenderer = textRenderer

    def render(self):
        viewportWidth, viewportHeight = glGetViewportSize()
        projection = TransformMatrix4()
        projection.ortho(0, viewportWidth, 0, viewportHeight, -1, 1)
        shader = self.shaderProgramCollection.mesh
        shader.use()
        shader.setModelMatrix(TransformMatrix4.identity)
        shader.setViewMatrix(TransformMatrix4.identity)
        shader.setProjectionMatrix(projection)
        shader.setAlpha(1.0)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnable(GL_BLEND)
        glEnable(GL_ALPHA_TEST)
        # self.textRenderer.render([("0123456789", 10, 100), ("qwertyuiopasdfghjklzxcvbnm", 10, 200), ("!@#$%^&*()+-*/[]{}<>", 10, 300)], shader)

        self.renderInfo(viewportWidth, viewportHeight)

        glDisable(GL_ALPHA_TEST)
        glDisable(GL_BLEND)
        shader.unuse()

    def renderInfo(self, viewportWidth, viewportHeight):
        textItems = []

        health = self.gameData.player.health
        textItems.append((str(health), 10, 10))

        vest = self.gameData.playerItems.vest
        textItems.append((str(vest), 200, 10))

        bulletsCount = self.gameData.playerItems.rightHandWeapon.bulletsCount
        if self.gameData.playerItems.leftHandWeapon is not None:
            bulletsCount += self.gameData.playerItems.leftHandWeapon.bulletsCount
        textItems.append((str(bulletsCount), viewportWidth - 110, 10))

        self.textRenderer.render(textItems)


def makeDashboardRenderer(resolver):
    return DashboardRenderer(resolver.resolve(GameData), resolver.resolve(ShaderProgramCollection), resolver.resolve(TextRenderer))
