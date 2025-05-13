from OpenGL.GL import *

from game.calc.TransformMatrix4 import TransformMatrix4
from game.engine.GameData import GameData
from game.gl.ext import glGetViewportSize
from game.gl.TextRenderer import TextRenderer
from game.render.common.ShaderProgramCollection import ShaderProgramCollection


class DashboardRenderer:

    def __init__(
        self,
        gameData: GameData,
        shaderProgramCollection: ShaderProgramCollection,
        textRenderer: TextRenderer,
    ):
        self.gameData = gameData
        self.shaderProgramCollection = shaderProgramCollection
        self.textRenderer = textRenderer

    def render(self):
        viewportWidth, viewportHeight = glGetViewportSize()
        model = TransformMatrix4()
        model.scale(0.8, 1.0, 1.0)
        projection = TransformMatrix4()
        projection.ortho(0, viewportWidth, 0, viewportHeight, -1, 1)
        shader = self.shaderProgramCollection.mesh
        shader.use()
        shader.setModelMatrix(model)
        shader.setViewMatrix(TransformMatrix4.identity)
        shader.setProjectionMatrix(projection)
        shader.setAlpha(1.0)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnable(GL_BLEND)
        glEnable(GL_ALPHA_TEST)

        self.renderInfo(viewportWidth, viewportHeight)

        glDisable(GL_ALPHA_TEST)
        glDisable(GL_BLEND)
        shader.unuse()

    def renderInfo(self, viewportWidth, viewportHeight):
        textItems = []

        textItems.append((self.getAlignedNumber(self.gameData.player.health), 10, 10))
        textItems.append((self.getAlignedNumber(self.gameData.playerItems.vest), 200, 10))

        bulletsCount = self.gameData.playerItems.rightHandWeapon.bulletsCount
        maxBulletsCount = self.gameData.playerItems.rightHandWeapon.maxBulletsCount
        if self.gameData.playerItems.leftHandWeapon is not None:
            bulletsCount += self.gameData.playerItems.leftHandWeapon.bulletsCount
            maxBulletsCount *= 2
        bulletsCount = f"{self.getAlignedNumber(bulletsCount)}/{maxBulletsCount}"
        textItems.append((bulletsCount, viewportWidth + 220, 10))

        self.textRenderer.render(textItems)

    def getAlignedNumber(self, number):
        if number < 9:
            number = "  " + str(number)
        elif number < 99:
            number = " " + str(number)
        else:
            number = str(number)

        return number
