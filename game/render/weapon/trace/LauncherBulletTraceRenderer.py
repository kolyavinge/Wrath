from OpenGL.GL import *

from game.anx.CommonConstants import CommonConstants
from game.engine.GameData import GameData
from game.gl.ColorVector3 import ColorVector3
from game.render.anx.BulletTraceParticleBufferCollection import *
from game.render.anx.LauncherBulletTraceParticleBufferInitializer import *
from game.render.common.ShaderProgramCollection import ShaderProgramCollection


class LauncherBulletTraceRenderer:

    def __init__(
        self,
        gameData: GameData,
        bufferInitializer: LauncherBulletTraceParticleBufferInitializer,
        shaderProgramCollection: ShaderProgramCollection,
    ):
        self.gameData = gameData
        self.bufferCollection = BulletTraceParticleBufferCollection(bufferInitializer)
        self.shaderProgramCollection = shaderProgramCollection
        self.particleColor = ColorVector3(150, 150, 150)
        self.particleColor.normalize()

    def renderTraces(self, traces):
        for trace in traces:
            self.renderTrace(trace)

    def renderTrace(self, trace):
        particleBuffer = self.bufferCollection.getBufferForTrace(trace)

        shader = self.shaderProgramCollection.launcherBulletTrace
        shader.use()
        shader.setTracePosition(trace.currentPosition)
        shader.setBulletDirection(trace.bullet.direction)
        shader.setBulletDirectionTopNormal(trace.bullet.directionTopNormal)
        shader.setBulletNozzleRadius(trace.bullet.nozzleRadius)
        shader.setViewMatrix(self.gameData.camera.viewMatrix)
        shader.setProjectionMatrix(self.gameData.camera.projectionMatrix)
        shader.setParticleAppearanceDelay(trace.particleAppearanceDelayMsec)
        shader.setParticleLifeTime(trace.particleLifeTimeMsec)
        shader.setParticleColor(self.particleColor)
        shader.setParticleSize(0.01)
        shader.setDeltaTime(CommonConstants.renderTimerMsec)

        # pass 1 - update
        shader.setPassNumber(1)
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

        # pass 2 - render
        shader.setPassNumber(2)
        glDepthMask(GL_FALSE)
        glBindVertexArray(particleBuffer.destinationBufferId)
        glVertexAttribDivisor(0, 1)
        glVertexAttribDivisor(1, 1)
        glVertexAttribDivisor(2, 1)
        glDrawArraysInstanced(GL_TRIANGLES, 0, 6, particleBuffer.particlesCount)
        glBindVertexArray(0)
        glDepthMask(GL_TRUE)
        glDisable(GL_DEPTH_TEST)
        glDisable(GL_ALPHA_TEST)
        glDisable(GL_BLEND)

        shader.unuse()

        particleBuffer.swapBuffers()
