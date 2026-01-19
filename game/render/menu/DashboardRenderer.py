from OpenGL.GL import *

from game.calc.TransformMatrix4 import TransformMatrix4
from game.engine.GameState import GameState
from game.engine.person.DashboardUpdater import DashboardUpdater
from game.gl.ext import GL_DEFAULT_FRAMEBUFFER_ID
from game.gl.TexturedFramebuffer import TexturedFramebuffer
from game.gl.vbo.ScreenQuadVBO import ScreenQuadVBO
from game.gl.vbo.VBORenderer import VBORenderer
from game.lib.EventManager import EventManager, Events
from game.render.common.ShaderProgramCollection import ShaderProgramCollection
from game.render.menu.DashboardSpriteRenderer import DashboardSpriteRenderer
from game.render.menu.DashboardTextRenderer import DashboardTextRenderer


class DashboardRenderer:

    def __init__(
        self,
        gameState: GameState,
        dashboardUpdater: DashboardUpdater,
        dashboardTextRenderer: DashboardTextRenderer,
        dashboardSpriteRenderer: DashboardSpriteRenderer,
        shaderProgramCollection: ShaderProgramCollection,
        screenQuadVBO: ScreenQuadVBO,
        vboRenderer: VBORenderer,
        eventManager: EventManager,
    ):
        self.gameState = gameState
        self.dashboardUpdater = dashboardUpdater
        self.dashboardTextRenderer = dashboardTextRenderer
        self.dashboardSpriteRenderer = dashboardSpriteRenderer
        self.shaderProgramCollection = shaderProgramCollection
        self.screenQuadVBO = screenQuadVBO
        self.vboRenderer = vboRenderer
        self.dashboardFramebuffer = TexturedFramebuffer()
        eventManager.attachToEvent(Events.viewportSizeChanged, self.onViewportSizeChanged)

    def init(self):
        self.dashboardSpriteRenderer.init()

    def render(self):
        self.dashboardUpdater.update(self.gameState)
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
        glEnable(GL_BLEND)
        glEnable(GL_ALPHA_TEST)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        self.vboRenderer.render(self.screenQuadVBO.vbo)
        glDisable(GL_ALPHA_TEST)
        glDisable(GL_BLEND)
        shader.unuse()

    def updateRenderDataIfDashboardChanged(self):
        if self.gameState.dashboard.hasChanged:
            self.gameState.dashboard.resetChanges()
            self.updateRenderData()

    def updateRenderData(self):
        glBindFramebuffer(GL_FRAMEBUFFER, self.dashboardFramebuffer.id)
        glClear(GL_COLOR_BUFFER_BIT)
        glEnable(GL_BLEND)
        glEnable(GL_ALPHA_TEST)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        self.dashboardTextRenderer.render()
        self.dashboardSpriteRenderer.render()
        glDisable(GL_ALPHA_TEST)
        glDisable(GL_BLEND)
        glBindFramebuffer(GL_FRAMEBUFFER, GL_DEFAULT_FRAMEBUFFER_ID)

    def onViewportSizeChanged(self, size):
        viewportWidth, viewportHeight = size
        projectionMatrix = TransformMatrix4()
        projectionMatrix.ortho(0, viewportWidth, 0, viewportHeight, -1, 1)
        self.dashboardFramebuffer.init(viewportWidth, viewportHeight)
        self.dashboardTextRenderer.setData(projectionMatrix, viewportWidth, viewportHeight)
        self.dashboardSpriteRenderer.setData(projectionMatrix, viewportWidth)
        self.updateRenderData()
