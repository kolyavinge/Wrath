from game.render.anx.BulletTraceParticleBufferInitializer import BulletTraceParticleBufferInitializer
from game.render.anx.ParticleBufferPool import ParticleBufferPool
from game.render.weapon.trace.ParticleBulletTraceRenderer import ParticleBulletTraceRenderer


class RifleGrenadeTraceRenderer:

    def __init__(
        self,
        particleBulletTraceRenderer: ParticleBulletTraceRenderer,
        bufferInitializer: BulletTraceParticleBufferInitializer,
    ):
        self.particleBulletTraceRenderer = particleBulletTraceRenderer
        self.bufferPool = ParticleBufferPool(bufferInitializer)

    def renderTraces(self, traces, camera):
        self.particleBulletTraceRenderer.renderTraces(traces, camera, self.bufferPool)
