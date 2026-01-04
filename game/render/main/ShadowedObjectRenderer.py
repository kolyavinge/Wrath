from OpenGL.GL import *

from game.anx.CommonConstants import CommonConstants
from game.engine.GameState import GameState
from game.gl.ext import GL_DEFAULT_FRAMEBUFFER_ID, gleBlitFramebuffer
from game.gl.vbo.ScreenQuadVBO import ScreenQuadVBO
from game.gl.vbo.VBORenderer import VBORenderer
from game.lib.EventManager import EventManager, Events
from game.render.common.ShaderProgramCollection import ShaderProgramCollection
from game.render.main.ShadowedObjectFramebuffer import ShadowedObjectFramebuffer


class ShadowedObjectRenderer:

    def __init__(
        self,
        gameData: GameState,
        shadowedObjectFramebuffer: ShadowedObjectFramebuffer,
        vboRenderer: VBORenderer,
        shaderProgramCollection: ShaderProgramCollection,
        screenQuadVBO: ScreenQuadVBO,
        eventManager: EventManager,
    ):
        self.gameData = gameData
        self.shadowedObjectFramebuffer = shadowedObjectFramebuffer
        self.vboRenderer = vboRenderer
        self.shaderProgramCollection = shaderProgramCollection
        self.screenQuadVBO = screenQuadVBO
        eventManager.attachToEvent(Events.viewportSizeChanged, self.onViewportSizeChanged)

    def onViewportSizeChanged(self, size):
        self.width, self.height = size
        self.shadowedObjectFramebuffer.init(self.width, self.height)

    def render(self, renderObjectFunc, renderShadowCastersFunc):
        self.calculateLightComponents(renderObjectFunc)
        self.calculateShadowVolumes(renderShadowCastersFunc)
        self.calculateStencilMask()
        self.composeScene()
        self.copySceneToDefaultFBO()

    def calculateLightComponents(self, renderObjectFunc):
        # calculate light components and write them in shadowedObjectFramebuffer
        # ambient light in ambientBuffer, diffuse + specular in diffuseSpecularTexture
        # draw scene normaly
        glBindFramebuffer(GL_FRAMEBUFFER, self.shadowedObjectFramebuffer.id)
        glDepthMask(GL_TRUE)
        glDisable(GL_STENCIL_TEST)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_CULL_FACE)
        glCullFace(GL_BACK)
        glClear(GL_DEPTH_BUFFER_BIT | GL_COLOR_BUFFER_BIT)
        shader = self.shaderProgramCollection.mainSceneLightComponents
        shader.use()
        shader.setViewMatrix(self.gameData.camera.viewMatrix)
        shader.setProjectionMatrix(self.gameData.camera.projectionMatrix)
        shader.setMaxDepth(CommonConstants.maxDepth)
        renderObjectFunc(shader)
        shader.unuse()
        glDisable(GL_CULL_FACE)
        glDisable(GL_DEPTH_TEST)

    def calculateShadowVolumes(self, renderShadowCastersFunc):
        # calculate shadow volumes by z-fail method
        # draw only shadow caster objects
        glColorMask(GL_FALSE, GL_FALSE, GL_FALSE, GL_FALSE)
        glDepthMask(GL_FALSE)
        glEnable(GL_DEPTH_CLAMP)
        glClear(GL_STENCIL_BUFFER_BIT)
        glEnable(GL_STENCIL_TEST)
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_FLAT)
        # stencil test always succeeds, decrements for front faces and increments for back
        glStencilFunc(GL_ALWAYS, 0, 0xFFFF)
        glStencilOpSeparate(GL_FRONT, GL_KEEP, GL_DECR_WRAP, GL_KEEP)
        glStencilOpSeparate(GL_BACK, GL_KEEP, GL_INCR_WRAP, GL_KEEP)
        shader = self.shaderProgramCollection.mainSceneShadowVolumes
        shader.use()
        shader.setViewMatrix(self.gameData.camera.viewMatrix)
        shader.setProjectionMatrix(self.gameData.camera.projectionMatrix)
        renderShadowCastersFunc(shader)
        shader.unuse()
        glShadeModel(GL_SMOOTH)
        glDisable(GL_DEPTH_TEST)
        glDisable(GL_STENCIL_TEST)
        glDisable(GL_DEPTH_CLAMP)
        glColorMask(GL_TRUE, GL_TRUE, GL_TRUE, GL_TRUE)

    def calculateStencilMask(self):
        # calculate stencil mask and write it in shadowedObjectFramebuffer.stencilMaskTexture
        glEnable(GL_STENCIL_TEST)
        glStencilFunc(GL_EQUAL, 0, 0xFFFF)  # render pixels that have a stencil value 0
        glStencilOp(GL_KEEP, GL_KEEP, GL_KEEP)
        shader = self.shaderProgramCollection.mainSceneStencilMask
        shader.use()
        self.vboRenderer.render(self.screenQuadVBO.vbo)
        shader.unuse()
        glDisable(GL_STENCIL_TEST)

    def composeScene(self):
        # compose scene by calculating light + stencil mask
        glEnable(GL_BLEND)
        glBlendFunc(GL_ONE, GL_ONE)
        glActiveTexture(GL_TEXTURE0)
        glBindTexture(GL_TEXTURE_2D, self.shadowedObjectFramebuffer.diffuseSpecularTexture)
        glActiveTexture(GL_TEXTURE1)
        glBindTexture(GL_TEXTURE_2D, self.shadowedObjectFramebuffer.stencilMaskTexture)
        shader = self.shaderProgramCollection.mainSceneCompose
        shader.use()
        shader.setResolution(self.width, self.height)
        self.vboRenderer.render(self.screenQuadVBO.vbo)
        shader.unuse()
        glDisable(GL_BLEND)

    def copySceneToDefaultFBO(self):
        gleBlitFramebuffer(
            self.shadowedObjectFramebuffer.id,
            GL_DEFAULT_FRAMEBUFFER_ID,
            self.width,
            self.height,
            GL_DEPTH_BUFFER_BIT | GL_COLOR_BUFFER_BIT,
            GL_NEAREST,
        )
        glBindFramebuffer(GL_FRAMEBUFFER, GL_DEFAULT_FRAMEBUFFER_ID)
