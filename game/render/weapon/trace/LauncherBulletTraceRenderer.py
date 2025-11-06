from OpenGL.GL import *

from game.anx.CommonConstants import CommonConstants
from game.anx.Events import Events
from game.engine.GameData import GameData
from game.gl.ext import GL_DEFAULT_FRAMEBUFFER_ID, gleBlitFramebuffer
from game.gl.Shader import ShaderConstants
from game.gl.TexturedFramebuffer import TexturedFramebuffer
from game.gl.vbo.ScreenQuadVBO import ScreenQuadVBO
from game.gl.vbo.VBORenderer import VBORenderer
from game.lib.EventManager import EventManager
from game.render.anx.LauncherBulletTraceParticleBufferInitializer import *
from game.render.anx.ParticleBufferCollection import ParticleBufferCollection
from game.render.common.ShaderProgramCollection import ShaderProgramCollection


class LauncherBulletTraceRenderer:

    def __init__(
        self,
        gameData: GameData,
        bufferInitializer: LauncherBulletTraceParticleBufferInitializer,
        shaderProgramCollection: ShaderProgramCollection,
        screenQuadVBO: ScreenQuadVBO,
        vboRenderer: VBORenderer,
        eventManager: EventManager,
    ):
        self.gameData = gameData
        self.bufferCollection = ParticleBufferCollection(bufferInitializer)
        self.shaderProgramCollection = shaderProgramCollection
        self.screenQuadVBO = screenQuadVBO
        self.vboRenderer = vboRenderer
        self.texturedFramebuffer = TexturedFramebuffer(addDepthComponent=True)
        eventManager.attachToEvent(Events.viewportSizeChanged, self.onViewportSizeChanged)

    def renderTraces(self, traces):
        self.prepareFramebuffer()
        self.prepareShader()
        self.updateAndRenderTraces(traces)
        self.blurRenderedTraces()

    def prepareFramebuffer(self):
        gleBlitFramebuffer(
            GL_DEFAULT_FRAMEBUFFER_ID, self.texturedFramebuffer.id, self.viewportWidth, self.viewportHeight, GL_DEPTH_BUFFER_BIT, GL_NEAREST
        )
        glBindFramebuffer(GL_FRAMEBUFFER, self.texturedFramebuffer.id)
        glClear(GL_COLOR_BUFFER_BIT)

    def prepareShader(self):
        shader = self.shaderProgramCollection.launcherBulletTrace
        shader.use()
        shader.setViewMatrix(self.gameData.camera.viewMatrix)
        shader.setProjectionMatrix(self.gameData.camera.projectionMatrix)
        shader.setDeltaTime(CommonConstants.renderTimerMsec)
        shader.unuse()

    def updateAndRenderTraces(self, traces):
        shader = self.shaderProgramCollection.launcherBulletTrace
        shader.use()
        for trace in traces:
            self.updateAndRenderTrace(trace, shader)
        shader.unuse()

    def updateAndRenderTrace(self, trace, shader):
        particleBuffer = self.bufferCollection.getBufferFor(trace)

        shader.setTracePosition(trace.currentPosition)
        shader.setBulletDirection(trace.bullet.direction)
        shader.setBulletDirectionTopNormal(trace.bullet.directionTopNormal)
        shader.setBulletNozzleRadius(trace.bullet.nozzleRadius)
        shader.setIsBulletAlive(trace.bullet.isAlive)
        shader.setParticleAppearanceDelay(trace.particleAppearanceDelayMsec)
        shader.setParticleLifeTime(trace.particleLifeTimeMsec)
        shader.setParticleSize(trace.particleSize)

        shader.setPassNumber(ShaderConstants.updatePass)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnable(GL_ALPHA_TEST)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_RASTERIZER_DISCARD)
        glBindTransformFeedback(GL_TRANSFORM_FEEDBACK, particleBuffer.destinationFeedbackId)
        glBeginTransformFeedback(GL_POINTS)
        glBindVertexArray(particleBuffer.sourceBufferId)
        glVertexAttribDivisor(0, 0)
        glVertexAttribDivisor(1, 0)
        glVertexAttribDivisor(2, 0)
        glDrawArrays(GL_POINTS, 0, particleBuffer.particlesCount)
        glBindVertexArray(0)
        glEndTransformFeedback()
        glDisable(GL_RASTERIZER_DISCARD)

        shader.setPassNumber(ShaderConstants.renderPass)
        glBindVertexArray(particleBuffer.destinationBufferId)
        glVertexAttribDivisor(0, 1)
        glVertexAttribDivisor(1, 1)
        glVertexAttribDivisor(2, 1)
        glDrawArraysInstanced(GL_TRIANGLES, 0, 24, particleBuffer.particlesCount)
        glBindVertexArray(0)
        glDisable(GL_DEPTH_TEST)
        glDisable(GL_ALPHA_TEST)
        glDisable(GL_BLEND)

        particleBuffer.swapBuffers()

    def blurRenderedTraces(self):
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
        shader.setOffsetsCount(32)
        self.vboRenderer.render(self.screenQuadVBO.vbo)
        shader.unuse()
        glDisable(GL_DEPTH_TEST)
        glDisable(GL_ALPHA_TEST)
        glDisable(GL_BLEND)

    def onViewportSizeChanged(self, size):
        self.viewportWidth, self.viewportHeight = size
        self.texturedFramebuffer.init(self.viewportWidth, self.viewportHeight)
