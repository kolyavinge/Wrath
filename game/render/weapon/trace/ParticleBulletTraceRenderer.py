from game.anx.CommonConstants import CommonConstants
from game.render.anx.BlurRenderer import BlurRenderer
from game.render.anx.BulletTraceParticleBufferInitializer import *
from game.render.anx.ParticleBufferPool import ParticleBufferPool
from game.render.common.ShaderProgramCollection import ShaderProgramCollection
from game.render.lib.FeedbackParticleRenderer import FeedbackParticleRenderer


class ParticleBulletTraceRenderer:

    def __init__(
        self,
        particleRenderer: FeedbackParticleRenderer,
        blurRenderer: BlurRenderer,
        bufferInitializer: BulletTraceParticleBufferInitializer,
        shaderProgramCollection: ShaderProgramCollection,
    ):
        self.particleRenderer = particleRenderer
        self.blurRenderer = blurRenderer
        self.bufferPool = ParticleBufferPool(bufferInitializer)
        self.shaderProgramCollection = shaderProgramCollection

    def renderTraces(self, traces, camera):
        self.blurRenderer.prepare()
        self.prepareShader(camera)
        self.updateAndRenderTraces(traces)
        self.blurRenderer.blur(32)

    def prepareShader(self, camera):
        shader = self.shaderProgramCollection.particleBulletTrace
        shader.use()
        shader.setViewMatrix(camera.viewMatrix)
        shader.setProjectionMatrix(camera.projectionMatrix)
        shader.setDeltaTime(CommonConstants.mainTimerMsec)
        shader.unuse()

    def updateAndRenderTraces(self, traces):
        shader = self.shaderProgramCollection.particleBulletTrace
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
        particleBuffer = self.bufferPool.getBufferFor(trace)
        self.particleRenderer.update(particleBuffer, shader)
        self.particleRenderer.render(particleBuffer, shader, 24)
        particleBuffer.swapBuffers()
