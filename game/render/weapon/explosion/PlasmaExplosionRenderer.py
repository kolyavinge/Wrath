from OpenGL.GL import *

from game.anx.CommonConstants import CommonConstants
from game.engine.GameState import GameState
from game.gl.FeedbackParticleRenderer import FeedbackParticleRenderer
from game.render.anx.BlurRenderer import BlurRenderer
from game.render.anx.ParticleBufferCollection import ParticleBufferCollection
from game.render.anx.PlasmaExplosionParticleBufferInitializer import *
from game.render.common.ShaderProgramCollection import ShaderProgramCollection


class PlasmaExplosionRenderer:

    def __init__(
        self,
        gameState: GameState,
        particleRenderer: FeedbackParticleRenderer,
        blurRenderer: BlurRenderer,
        bufferInitializer: PlasmaExplosionParticleBufferInitializer,
        shaderProgramCollection: ShaderProgramCollection,
    ):
        self.gameState = gameState
        self.particleRenderer = particleRenderer
        self.blurRenderer = blurRenderer
        self.bufferCollection = ParticleBufferCollection(bufferInitializer)
        self.shaderProgramCollection = shaderProgramCollection

    def renderExplosions(self, explosions):
        self.blurRenderer.prepare()
        self.prepareShader()
        self.updateAndRenderExplosions(explosions)
        self.blurRenderer.blur(4)

    def prepareShader(self):
        shader = self.shaderProgramCollection.plasmaExplosion
        shader.use()
        shader.setViewMatrix(self.gameState.camera.viewMatrix)
        shader.setProjectionMatrix(self.gameState.camera.projectionMatrix)
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
