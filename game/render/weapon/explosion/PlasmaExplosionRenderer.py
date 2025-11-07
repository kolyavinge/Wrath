from OpenGL.GL import *

from game.anx.CommonConstants import CommonConstants
from game.anx.Events import Events
from game.engine.GameData import GameData
from game.gl.ext import GL_DEFAULT_FRAMEBUFFER_ID, gleBlitFramebuffer
from game.gl.FeedbackParticleRenderer import FeedbackParticleRenderer
from game.gl.TexturedFramebuffer import TexturedFramebuffer
from game.gl.vbo.ScreenQuadVBO import ScreenQuadVBO
from game.gl.vbo.VBORenderer import VBORenderer
from game.lib.EventManager import EventManager
from game.render.anx.ParticleBufferCollection import ParticleBufferCollection
from game.render.anx.PlasmaExplosionParticleBufferInitializer import *
from game.render.common.ShaderProgramCollection import ShaderProgramCollection


class PlasmaExplosionRenderer:

    def __init__(
        self,
        gameData: GameData,
        particleRenderer: FeedbackParticleRenderer,
        bufferInitializer: PlasmaExplosionParticleBufferInitializer,
        shaderProgramCollection: ShaderProgramCollection,
        screenQuadVBO: ScreenQuadVBO,
        vboRenderer: VBORenderer,
        eventManager: EventManager,
    ):
        self.gameData = gameData
        self.particleRenderer = particleRenderer
        self.bufferCollection = ParticleBufferCollection(bufferInitializer)
        self.shaderProgramCollection = shaderProgramCollection
        self.screenQuadVBO = screenQuadVBO
        self.vboRenderer = vboRenderer
        self.texturedFramebuffer = TexturedFramebuffer(addDepthComponent=True)
        eventManager.attachToEvent(Events.viewportSizeChanged, self.onViewportSizeChanged)

    def renderExplosions(self, explosions):
        self.prepareFramebuffer()
        self.prepareShader()
        self.updateAndRenderExplosions(explosions)
        self.blurRenderedExplosions()

    def prepareFramebuffer(self):
        gleBlitFramebuffer(
            GL_DEFAULT_FRAMEBUFFER_ID, self.texturedFramebuffer.id, self.viewportWidth, self.viewportHeight, GL_DEPTH_BUFFER_BIT, GL_NEAREST
        )
        glBindFramebuffer(GL_FRAMEBUFFER, self.texturedFramebuffer.id)
        glClear(GL_COLOR_BUFFER_BIT)

    def prepareShader(self):
        shader = self.shaderProgramCollection.plasmaExplosion
        shader.use()
        shader.setViewMatrix(self.gameData.camera.viewMatrix)
        shader.setProjectionMatrix(self.gameData.camera.projectionMatrix)
        shader.setDeltaTime(CommonConstants.renderTimerMsec)
        shader.unuse()

    def updateAndRenderExplosions(self, explosions):
        shader = self.shaderProgramCollection.plasmaExplosion
        shader.use()
        for explosion in explosions:
            self.updateAndRenderExplosion(explosion, shader)
        shader.unuse()

    def updateAndRenderExplosion(self, explosion, shader):
        shader.setParticleLifeTime(explosion.particleLifeTimeMsec)
        shader.setParticleSize(explosion.particleSize)
        particleBuffer = self.bufferCollection.getBufferFor(explosion)
        self.particleRenderer.update(particleBuffer, shader)
        self.particleRenderer.render(particleBuffer, shader, 24)
        particleBuffer.swapBuffers()

    def blurRenderedExplosions(self):
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
        shader.setOffsetsCount(4)
        self.vboRenderer.render(self.screenQuadVBO.vbo)
        shader.unuse()
        glDisable(GL_DEPTH_TEST)
        glDisable(GL_ALPHA_TEST)
        glDisable(GL_BLEND)

    def onViewportSizeChanged(self, size):
        self.viewportWidth, self.viewportHeight = size
        self.texturedFramebuffer.init(self.viewportWidth, self.viewportHeight)
