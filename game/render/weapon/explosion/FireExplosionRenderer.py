from OpenGL.GL import GL_TEXTURE0

from game.engine.GameState import GameState
from game.gl.ParticleRenderer import ParticleRenderer
from game.render.anx.FireExplosionParticleBufferInitializer import *
from game.render.anx.ParticleBufferCollection import ParticleBufferCollection
from game.render.common.ShaderProgramCollection import ShaderProgramCollection


class FireExplosionRenderer:

    def __init__(
        self,
        gameState: GameState,
        particleRenderer: ParticleRenderer,
        bufferInitializer: FireExplosionParticleBufferInitializer,
        shaderProgramCollection: ShaderProgramCollection,
    ):
        self.gameState = gameState
        self.particleRenderer = particleRenderer
        self.bufferCollection = ParticleBufferCollection(bufferInitializer)
        self.shaderProgramCollection = shaderProgramCollection

    def renderExplosions(self, explosions, explosionTexture):
        shader = self.shaderProgramCollection.fireExplosion
        shader.use()
        shader.setViewMatrix(self.gameState.camera.viewMatrix)
        shader.setProjectionMatrix(self.gameState.camera.projectionMatrix)
        shader.setCurrentTimeSec(self.gameState.globalTimeSec)
        explosionTexture.bind(GL_TEXTURE0)
        for explosion in explosions:
            particleBuffer = self.bufferCollection.getBufferFor(explosion)
            shader.setInitTimeSec(explosion.initTimeSec)
            self.particleRenderer.render(particleBuffer, 6)
        shader.unuse()
