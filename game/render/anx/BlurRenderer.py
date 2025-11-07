from OpenGL.GL import *

from game.gl.ext import GL_DEFAULT_FRAMEBUFFER_ID, gleBlitFramebuffer
from game.gl.TexturedFramebuffer import TexturedFramebuffer
from game.gl.vbo.ScreenQuadVBO import ScreenQuadVBO
from game.gl.vbo.VBORenderer import VBORenderer
from game.lib.EventManager import EventManager, Events
from game.render.common.ShaderProgramCollection import ShaderProgramCollection


class BlurRenderer:

    def __init__(
        self,
        shaderProgramCollection: ShaderProgramCollection,
        screenQuadVBO: ScreenQuadVBO,
        vboRenderer: VBORenderer,
        eventManager: EventManager,
    ):
        self.shaderProgramCollection = shaderProgramCollection
        self.screenQuadVBO = screenQuadVBO
        self.vboRenderer = vboRenderer
        self.texturedFramebuffer = TexturedFramebuffer(addDepthComponent=True)
        eventManager.attachToEvent(Events.viewportSizeChanged, self.onViewportSizeChanged)

    def prepare(self):
        gleBlitFramebuffer(
            GL_DEFAULT_FRAMEBUFFER_ID, self.texturedFramebuffer.id, self.viewportWidth, self.viewportHeight, GL_DEPTH_BUFFER_BIT, GL_NEAREST
        )
        glBindFramebuffer(GL_FRAMEBUFFER, self.texturedFramebuffer.id)
        glClear(GL_COLOR_BUFFER_BIT)

    def blur(self, offsetsCount):
        gleBlitFramebuffer(
            self.texturedFramebuffer.id, GL_DEFAULT_FRAMEBUFFER_ID, self.viewportWidth, self.viewportHeight, GL_DEPTH_BUFFER_BIT, GL_NEAREST
        )
        glBindFramebuffer(GL_FRAMEBUFFER, GL_DEFAULT_FRAMEBUFFER_ID)
        glEnable(GL_BLEND)
        glEnable(GL_ALPHA_TEST)
        glEnable(GL_DEPTH_TEST)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glActiveTexture(GL_TEXTURE0)
        glBindTexture(GL_TEXTURE_2D, self.texturedFramebuffer.texture)
        shader = self.shaderProgramCollection.blur
        shader.use()
        shader.setResolution(self.viewportWidth, self.viewportHeight)
        shader.setOffsetsCount(offsetsCount)
        self.vboRenderer.render(self.screenQuadVBO.vbo)
        shader.unuse()
        glDisable(GL_DEPTH_TEST)
        glDisable(GL_ALPHA_TEST)
        glDisable(GL_BLEND)

    def onViewportSizeChanged(self, size):
        self.viewportWidth, self.viewportHeight = size
        self.texturedFramebuffer.init(self.viewportWidth, self.viewportHeight)
