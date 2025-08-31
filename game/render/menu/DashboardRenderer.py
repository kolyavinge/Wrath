from OpenGL.GL import *

from game.anx.Events import Events
from game.calc.TransformMatrix4 import TransformMatrix4
from game.engine.GameData import GameData
from game.gl.TextRenderer import TextRenderer
from game.lib.EventManager import EventManager
from game.render.common.ShaderProgramCollection import ShaderProgramCollection


class DashboardRenderer:

    def __init__(
        self,
        gameData: GameData,
        shaderProgramCollection: ShaderProgramCollection,
        textRenderer: TextRenderer,
        eventManager: EventManager,
    ):
        self.gameData = gameData
        self.shaderProgramCollection = shaderProgramCollection
        self.textRenderer = textRenderer
        self.model = TransformMatrix4()
        self.model.scale(0.8, 1.0, 1.0)
        eventManager.attachToEvent(Events.viewportSizeChanged, self.onViewportSizeChanged)

    def render(self):
        shader = self.shaderProgramCollection.mesh
        shader.use()
        shader.setModelMatrix(self.model)
        shader.setViewMatrix(TransformMatrix4.identity)
        shader.setProjectionMatrix(self.projection)
        shader.setColorFactor(1.0)
        shader.setAlphaFactor(1.0)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnable(GL_BLEND)
        glEnable(GL_ALPHA_TEST)
        self.renderInfo()
        glDisable(GL_ALPHA_TEST)
        glDisable(GL_BLEND)
        shader.unuse()

    def renderInfo(self):
        textItems = []

        textItems.append((self.getAlignedNumber(self.gameData.player.health), 10, 10))
        textItems.append((self.getAlignedNumber(self.gameData.playerItems.vest), 200, 10))

        bulletsCount = self.gameData.playerItems.getLeftRightWeaponBulletsCount()
        maxBulletsCount = self.gameData.playerItems.getLeftRightWeaponMaxBulletsCount()
        bulletsCount = f"{self.getAlignedNumber(bulletsCount)}/{maxBulletsCount}"
        textItems.append((bulletsCount, self.viewportWidth + 220, 10))

        self.textRenderer.render(textItems)

    def getAlignedNumber(self, number):
        if number < 10:
            number = "  " + str(number)
        elif number < 100:
            number = " " + str(number)
        else:
            number = str(number)

        return number

    def onViewportSizeChanged(self, size):
        self.viewportWidth, self.viewportHeight = size
        self.projection = TransformMatrix4()
        self.projection.ortho(0, self.viewportWidth, 0, self.viewportHeight, -1, 1)
