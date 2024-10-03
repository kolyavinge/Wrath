from OpenGL.GL import *

from game.anx.CommonConstants import CommonConstants
from game.anx.Events import Events
from game.engine.GameData import GameData
from game.gl.ext import *
from game.gl.ScreenQuadVBO import ScreenQuadVBO
from game.gl.VBORenderer import VBORenderer
from game.lib.EventManager import EventManager
from game.render.common.ShaderProgramCollection import ShaderProgramCollection
from game.render.level.LevelRenderer import LevelRenderer
from game.render.level.ShadowCastLevelItemCollection import *
from game.render.main.MainSceneFramebuffer import MainSceneFramebuffer


class MainSceneRenderer:

    def __init__(self, gameData, mainSceneFramebuffer, levelRenderer, vboRenderer, shaderProgramCollection, screenQuadVBO, eventManager):
        self.gameData = gameData
        self.mainSceneFramebuffer = mainSceneFramebuffer
        self.levelRenderer = levelRenderer
        self.vboRenderer = vboRenderer
        self.shaderProgramCollection = shaderProgramCollection
        self.screenQuadVBO = screenQuadVBO
        eventManager.attachToEvent(Events.viewportSizeChanged, self.onViewportSizeChanged)

    def init(self):
        pass

    def onViewportSizeChanged(self):
        self.mainSceneFramebuffer.init()
        self.viewportWidth, self.viewportHeight = glGetViewportSize()

    def render(self):
        self.calculateLightComponents()
        self.calculateShadowVolumes()
        self.composeScene()

    def calculateLightComponents(self):
        glDepthMask(GL_TRUE)
        glDisable(GL_STENCIL_TEST)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_TEXTURE_2D)
        glEnable(GL_CULL_FACE)
        glCullFace(GL_BACK)
        glBindFramebuffer(GL_FRAMEBUFFER, self.mainSceneFramebuffer.colorDepthFBO)
        glClear(GL_DEPTH_BUFFER_BIT | GL_COLOR_BUFFER_BIT)
        shader = self.shaderProgramCollection.mainSceneLightComponents
        shader.use()
        camera = self.gameData.camera
        mvpMatrix = camera.projectionMatrix.copy()
        mvpMatrix.mul(camera.viewMatrix)
        shader.setModelViewMatrix(camera.viewMatrix)
        shader.setModelViewProjectionMatrix(mvpMatrix)
        shader.setNormalMatrix(camera.viewMatrix.toMatrix3())
        shader.setMaxDepth(CommonConstants.maxDepth)
        self.levelRenderer.renderLevelSegments(shader)
        shader.unuse()
        glDisable(GL_CULL_FACE)
        glDisable(GL_TEXTURE_2D)
        glDisable(GL_DEPTH_TEST)

    def calculateShadowVolumes(self):
        # copy depth and color buffers from colorDepthFBO to default FBO
        glBindFramebuffer(GL_READ_FRAMEBUFFER, self.mainSceneFramebuffer.colorDepthFBO)
        glBindFramebuffer(GL_DRAW_FRAMEBUFFER, 0)
        width = self.viewportWidth - 1
        height = self.viewportHeight - 1
        glBlitFramebuffer(0, 0, width, height, 0, 0, width, height, GL_DEPTH_BUFFER_BIT | GL_COLOR_BUFFER_BIT, GL_NEAREST)
        glColorMask(GL_FALSE, GL_FALSE, GL_FALSE, GL_FALSE)
        glDepthMask(GL_FALSE)
        glEnable(GL_DEPTH_CLAMP)
        glBindFramebuffer(GL_FRAMEBUFFER, 0)
        glClear(GL_STENCIL_BUFFER_BIT)
        glEnable(GL_STENCIL_TEST)
        glEnable(GL_DEPTH_TEST)
        # stencil test always succeeds, increments for front faces and decrements for back
        glStencilFunc(GL_ALWAYS, 0, 0xFFFF)
        glStencilOpSeparate(GL_FRONT, GL_KEEP, GL_DECR_WRAP, GL_KEEP)
        glStencilOpSeparate(GL_BACK, GL_KEEP, GL_INCR_WRAP, GL_KEEP)
        shader = self.shaderProgramCollection.mainSceneShadowVolumes
        shader.use()
        shader.setProjectionMatrix(self.gameData.camera.projectionMatrix)
        shader.setModelViewMatrix(self.gameData.camera.viewMatrix)
        self.levelRenderer.renderShadowCasters(shader)
        shader.unuse()
        glDisable(GL_DEPTH_CLAMP)
        glColorMask(GL_TRUE, GL_TRUE, GL_TRUE, GL_TRUE)
        glDisable(GL_DEPTH_TEST)
        glDisable(GL_STENCIL_TEST)

    def composeScene(self):
        glEnable(GL_STENCIL_TEST)
        glEnable(GL_BLEND)
        glEnable(GL_TEXTURE_2D)
        glBlendFunc(GL_ONE, GL_ONE)
        glStencilFunc(GL_EQUAL, 0, 0xFFFF)  # render pixels that have a stencil value 0
        glStencilOp(GL_KEEP, GL_KEEP, GL_KEEP)
        shader = self.shaderProgramCollection.mainSceneCompose
        shader.use()
        glActiveTexture(GL_TEXTURE0)
        glBindTexture(GL_TEXTURE_2D, self.mainSceneFramebuffer.diffuseSpecularTexture)
        self.vboRenderer.render(self.screenQuadVBO.vbo)
        shader.unuse()
        glDisable(GL_TEXTURE_2D)
        glDisable(GL_BLEND)
        glDisable(GL_STENCIL_TEST)


def makeMainSceneRenderer(resolver):
    return MainSceneRenderer(
        resolver.resolve(GameData),
        resolver.resolve(MainSceneFramebuffer),
        resolver.resolve(LevelRenderer),
        resolver.resolve(VBORenderer),
        resolver.resolve(ShaderProgramCollection),
        resolver.resolve(ScreenQuadVBO),
        resolver.resolve(EventManager),
    )
