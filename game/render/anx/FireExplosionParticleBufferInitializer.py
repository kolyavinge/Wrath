from game.calc.Vector3 import Vector3
from game.calc.Vector4 import Vector4
from game.gl.ParticleBuffer import ExtraParticleDataBuffers
from game.gl.ParticleBufferFactory import ParticleBufferFactory
from game.lib.Math import Math
from game.lib.Random import Random


class FireExplosionParticleBufferInitializer:

    def __init__(self, particleBufferFactory: ParticleBufferFactory):
        self.particleBufferFactory = particleBufferFactory

    def makeEmpty(self, explosion):
        particlesCount = 1
        buffer = self.particleBufferFactory.make(
            particlesCount,
            [ExtraParticleDataBuffers.lifeTimeBuffer, ExtraParticleDataBuffers.texCoordBuffer],
        )

        return buffer

    def init(self, buffer, explosion):
        buffer.setPositionData(self.getPositionData(explosion))
        buffer.setVelocityData(self.getVelocityData(explosion))
        buffer.setAgeData(self.getAgeData(explosion))
        buffer.setLifeTimeData(self.getLifeTimeData(explosion))
        buffer.setTexCoordData(self.getTexCoordData(explosion))

    def getPositionData(self, explosion):
        positionData = [explosion.position] * 1

        return positionData

    def getVelocityData(self, explosion):
        velocityData = [Vector3(0, 0, 0.1)] * 1

        return velocityData

    def getAgeData(self, explosion):
        ageData = [0] * 1

        return ageData

    def getLifeTimeData(self, explosion):
        lifeTimeData = [1.0] * 1

        return lifeTimeData

    def getTexCoordData(self, explosion):
        texCoordData = [Vector4(0, 0, 1, 1)] * 1

        return texCoordData
