from OpenGL.GL import *

from game.anx.CommonConstants import CommonConstants
from game.gl.FeedbackParticleRenderer import FeedbackParticleRenderer
from game.render.anx.BlurRenderer import BlurRenderer
from game.render.anx.LauncherBulletTraceParticleBufferInitializer import *
from game.render.anx.ParticleBufferCollection import ParticleBufferCollection
from game.render.common.ShaderProgramCollection import ShaderProgramCollection


class LauncherBulletTraceRenderer:

    def __init__(
        self,
        particleRenderer: FeedbackParticleRenderer,
        blurRenderer: BlurRenderer,
        bufferInitializer: LauncherBulletTraceParticleBufferInitializer,
        shaderProgramCollection: ShaderProgramCollection,
    ):
        self.particleRenderer = particleRenderer
        self.blurRenderer = blurRenderer
        self.bufferCollection = ParticleBufferCollection(bufferInitializer)
        self.shaderProgramCollection = shaderProgramCollection

    def renderTraces(self, traces, camera):
        self.blurRenderer.prepare()
        self.prepareShader(camera)
        self.updateAndRenderTraces(traces)
        self.blurRenderer.blur(32)

    def prepareShader(self, camera):
        shader = self.shaderProgramCollection.launcherBulletTrace
        shader.use()
        shader.setViewMatrix(camera.viewMatrix)
        shader.setProjectionMatrix(camera.projectionMatrix)
        shader.setDeltaTime(CommonConstants.mainTimerMsec)
        shader.unuse()

    def updateAndRenderTraces(self, traces):
        shader = self.shaderProgramCollection.launcherBulletTrace
        shader.use()
        for trace in traces:
            self.updateAndRenderTrace(trace, shader)
        shader.unuse()

    def updateAndRenderTrace(self, trace, shader):
        shader.setTracePosition(trace.currentPosition)
        shader.setBulletDirection(trace.bullet.direction)
        shader.setBulletDirectionTopNormal(trace.bullet.weapon.directionTopNormal)
        shader.setBulletNozzleRadius(trace.bullet.nozzleRadius)
        shader.setIsBulletAlive(trace.bullet.isAlive)
        shader.setParticleLifeTime(trace.particleLifeTimeMsec)
        shader.setParticleSize(trace.particleSize)
        particleBuffer = self.bufferCollection.getBufferFor(trace)
        self.particleRenderer.update(particleBuffer, shader)
        self.particleRenderer.render(particleBuffer, shader, 24)
        particleBuffer.swapBuffers()
