from OpenGL.GL import *

from game.anx.CommonConstants import CommonConstants
from game.gl.FeedbackParticleRenderer import FeedbackParticleRenderer
from game.render.anx.BlurRenderer import BlurRenderer
from game.render.anx.ParticleBufferCollection import ParticleBufferCollection
from game.render.anx.PlasmaExplosionParticleBufferInitializer import *
from game.render.common.ShaderProgramCollection import ShaderProgramCollection


class PlasmaExplosionRenderer:

    def __init__(
        self,
        particleRenderer: FeedbackParticleRenderer,
        blurRenderer: BlurRenderer,
        bufferInitializer: PlasmaExplosionParticleBufferInitializer,
        shaderProgramCollection: ShaderProgramCollection,
    ):
        self.particleRenderer = particleRenderer
        self.blurRenderer = blurRenderer
        self.bufferInitializer = bufferInitializer
        self.shaderProgramCollection = shaderProgramCollection

    def init(self, camera):
        self.camera = camera
        self.bufferCollection = ParticleBufferCollection(self.bufferInitializer, self.camera)

    def renderExplosions(self, explosions, globalTimeSec):
        self.blurRenderer.prepare()
        self.prepareShader()
        self.updateAndRenderExplosions(explosions)
        self.blurRenderer.blur(4)

    def prepareShader(self):
        shader = self.shaderProgramCollection.plasmaExplosion
        shader.use()
        shader.setViewMatrix(self.camera.viewMatrix)
        shader.setProjectionMatrix(self.camera.projectionMatrix)
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
