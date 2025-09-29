from OpenGL.GL import *

from game.anx.Events import Events
from game.calc.TransformMatrix4 import TransformMatrix4
from game.engine.DashboardUpdater import DashboardUpdater
from game.engine.GameData import GameData
from game.gl.TextRenderer import TextRenderer
from game.lib.EventManager import EventManager
from game.render.common.ShaderProgramCollection import ShaderProgramCollection


class DashboardRenderer:

    def __init__(
        self,
        gameData: GameData,
        dashboardUpdater: DashboardUpdater,
        shaderProgramCollection: ShaderProgramCollection,
        textRenderer: TextRenderer,
        eventManager: EventManager,
    ):
        self.gameData = gameData
        self.dashboardUpdater = dashboardUpdater
        self.shaderProgramCollection = shaderProgramCollection
        self.textRenderer = textRenderer
        self.model = TransformMatrix4()
        self.model.scale(0.8, 1.0, 1.0)
        eventManager.attachToEvent(Events.viewportSizeChanged, self.onViewportSizeChanged)

    def render(self):
        self.dashboardUpdater.update()
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
        dashboard = self.gameData.dashboard
        textItems = [
            (dashboard.healthStr, 10, 10),
            (dashboard.vestStr, 200, 10),
            (dashboard.bulletsCountStr, self.viewportWidth + 220, 10),
        ]
        self.textRenderer.render(textItems)

    def onViewportSizeChanged(self, size):
        self.viewportWidth, self.viewportHeight = size
        self.projection = TransformMatrix4()
        self.projection.ortho(0, self.viewportWidth, 0, self.viewportHeight, -1, 1)
