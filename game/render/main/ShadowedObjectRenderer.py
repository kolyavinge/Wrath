from OpenGL.GL import *

from game.anx.CommonConstants import CommonConstants
from game.anx.Events import Events
from game.calc.TransformMatrix4 import TransformMatrix4
from game.engine.GameData import GameData
from game.gl.vbo.ScreenQuadVBO import ScreenQuadVBO
from game.gl.vbo.VBORenderer import VBORenderer
from game.lib.EventManager import EventManager
from game.render.common.ShaderProgramCollection import ShaderProgramCollection
from game.render.main.ShadowedObjectFramebuffer import ShadowedObjectFramebuffer


class ShadowedObjectRenderer:

    def __init__(self, gameData, shadowedObjectFramebuffer, vboRenderer, shaderProgramCollection, screenQuadVBO, eventManager):
        self.gameData = gameData
        self.shadowedObjectFramebuffer = shadowedObjectFramebuffer
        self.vboRenderer = vboRenderer
        self.shaderProgramCollection = shaderProgramCollection
        self.screenQuadVBO = screenQuadVBO
        eventManager.attachToEvent(Events.viewportSizeChanged, self.onViewportSizeChanged)

    def onViewportSizeChanged(self, size):
        self.shadowedObjectFramebuffer.init()
        self.width, self.height = size

    def render(self, renderObjectFunc, renderShadowCastersFunc):
        self.calculateLightComponents(renderObjectFunc)
        self.calculateShadowVolumes(renderShadowCastersFunc)
        self.composeScene()

    def calculateLightComponents(self, renderObjectFunc):
        glDepthMask(GL_TRUE)
        glDisable(GL_STENCIL_TEST)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_TEXTURE_2D)
        glEnable(GL_CULL_FACE)
        glCullFace(GL_BACK)
        glBindFramebuffer(GL_FRAMEBUFFER, self.shadowedObjectFramebuffer.colorDepthFBO)
        glClear(GL_DEPTH_BUFFER_BIT | GL_COLOR_BUFFER_BIT)
        shader = self.shaderProgramCollection.mainSceneLightComponents
        shader.use()
        shader.setViewMatrix(self.gameData.camera.viewMatrix)
        shader.setProjectionMatrix(self.gameData.camera.projectionMatrix)
        shader.setMaxDepth(CommonConstants.maxDepth)
        renderObjectFunc(shader)
        shader.unuse()
        glDisable(GL_CULL_FACE)
        glDisable(GL_TEXTURE_2D)
        glDisable(GL_DEPTH_TEST)

    def calculateShadowVolumes(self, renderShadowCastersFunc):
        # copy depth and color buffers from colorDepthFBO to default FBO
        glBindFramebuffer(GL_READ_FRAMEBUFFER, self.shadowedObjectFramebuffer.colorDepthFBO)
        glBindFramebuffer(GL_DRAW_FRAMEBUFFER, 0)
        glBlitFramebuffer(0, 0, self.width, self.height, 0, 0, self.width, self.height, GL_DEPTH_BUFFER_BIT | GL_COLOR_BUFFER_BIT, GL_NEAREST)
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
        shader.setModelMatrix(TransformMatrix4.identity)
        shader.setViewMatrix(self.gameData.camera.viewMatrix)
        shader.setProjectionMatrix(self.gameData.camera.projectionMatrix)
        renderShadowCastersFunc(shader)
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
        glBindTexture(GL_TEXTURE_2D, self.shadowedObjectFramebuffer.diffuseSpecularTexture)
        self.vboRenderer.render(self.screenQuadVBO.vbo)
        shader.unuse()
        glDisable(GL_TEXTURE_2D)
        glDisable(GL_BLEND)
        glDisable(GL_STENCIL_TEST)


def makeShadowedObjectRenderer(resolver):
    return ShadowedObjectRenderer(
        resolver.resolve(GameData),
        resolver.resolve(ShadowedObjectFramebuffer),
        resolver.resolve(VBORenderer),
        resolver.resolve(ShaderProgramCollection),
        resolver.resolve(ScreenQuadVBO),
        resolver.resolve(EventManager),
    )
