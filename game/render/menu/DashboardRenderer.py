from OpenGL.GL import *

from game.anx.Events import Events
from game.calc.TransformMatrix4 import TransformMatrix4
from game.engine.DashboardUpdater import DashboardUpdater
from game.engine.GameData import GameData
from game.gl.ext import GL_DEFAULT_FRAMEBUFFER_ID
from game.gl.TextRenderer import TextRenderer
from game.gl.vbo.ScreenQuadVBO import ScreenQuadVBO
from game.gl.vbo.VBORenderer import VBORenderer
from game.lib.EventManager import EventManager
from game.render.common.ShaderProgramCollection import ShaderProgramCollection
from game.render.menu.DashboardFramebuffer import DashboardFramebuffer


class DashboardRenderer:

    def __init__(
        self,
        gameData: GameData,
        dashboardUpdater: DashboardUpdater,
        dashboardFramebuffer: DashboardFramebuffer,
        shaderProgramCollection: ShaderProgramCollection,
        textRenderer: TextRenderer,
        screenQuadVBO: ScreenQuadVBO,
        vboRenderer: VBORenderer,
        eventManager: EventManager,
    ):
        self.gameData = gameData
        self.dashboardUpdater = dashboardUpdater
        self.dashboardFramebuffer = dashboardFramebuffer
        self.shaderProgramCollection = shaderProgramCollection
        self.textRenderer = textRenderer
        self.screenQuadVBO = screenQuadVBO
        self.vboRenderer = vboRenderer
        self.model = TransformMatrix4()
        self.model.scale(0.8, 1.0, 1.0)
        eventManager.attachToEvent(Events.viewportSizeChanged, self.onViewportSizeChanged)

    def render(self):
        self.dashboardUpdater.update()
        self.updateRenderDataIfDashboardChanged()
        self.renderDashboardData()

    def renderDashboardData(self):
        shader = self.shaderProgramCollection.mesh
        shader.use()
        shader.setModelMatrix(TransformMatrix4.identity)
        shader.setViewMatrix(TransformMatrix4.identity)
        shader.setProjectionMatrix(TransformMatrix4.identity)
        shader.setColorFactor(1.0)
        shader.setAlphaFactor(1.0)
        glActiveTexture(GL_TEXTURE0)
        glBindTexture(GL_TEXTURE_2D, self.dashboardFramebuffer.texture)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnable(GL_BLEND)
        glEnable(GL_ALPHA_TEST)
        self.vboRenderer.render(self.screenQuadVBO.vbo)
        glDisable(GL_ALPHA_TEST)
        glDisable(GL_BLEND)
        shader.unuse()

    def updateRenderDataIfDashboardChanged(self):
        if self.gameData.dashboard.hasChanged:
            self.gameData.dashboard.resetChanges()
            self.updateRenderData()

    def updateRenderData(self):
        glBindFramebuffer(GL_FRAMEBUFFER, self.dashboardFramebuffer.id)
        glClear(GL_COLOR_BUFFER_BIT)
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
        self.updateTextData()
        glDisable(GL_ALPHA_TEST)
        glDisable(GL_BLEND)
        shader.unuse()
        glBindFramebuffer(GL_FRAMEBUFFER, GL_DEFAULT_FRAMEBUFFER_ID)

    def updateTextData(self):
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
        self.dashboardFramebuffer.init()
        self.updateRenderData()
