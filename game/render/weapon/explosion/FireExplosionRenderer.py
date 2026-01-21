from OpenGL.GL import GL_TEXTURE0

from game.gl.ParticleRenderer import ParticleRenderer
from game.render.anx.FireExplosionParticleBufferInitializer import *
from game.render.anx.ParticleBufferCollection import ParticleBufferCollection
from game.render.common.ShaderProgramCollection import ShaderProgramCollection


class FireExplosionRenderer:

    def __init__(
        self,
        particleRenderer: ParticleRenderer,
        bufferInitializer: FireExplosionParticleBufferInitializer,
        shaderProgramCollection: ShaderProgramCollection,
    ):
        self.particleRenderer = particleRenderer
        self.bufferInitializer = bufferInitializer
        self.shaderProgramCollection = shaderProgramCollection

    def init(self, camera):
        self.camera = camera
        self.bufferCollection = ParticleBufferCollection(self.bufferInitializer, self.camera)

    def renderExplosions(self, explosions, explosionTexture, globalTimeSec):
        shader = self.shaderProgramCollection.fireExplosion
        shader.use()
        shader.setViewMatrix(self.camera.viewMatrix)
        shader.setProjectionMatrix(self.camera.projectionMatrix)
        shader.setCurrentTimeSec(globalTimeSec)
        explosionTexture.bind(GL_TEXTURE0)
        for explosion in explosions:
            particleBuffer = self.bufferCollection.getBufferFor(explosion)
            shader.setInitTimeSec(explosion.initTimeSec)
            self.particleRenderer.render(particleBuffer, 6)
        shader.unuse()
