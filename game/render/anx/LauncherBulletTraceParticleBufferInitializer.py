from game.gl.FeedbackParticleBufferFactory import *
from game.gl.ParticleBuffer import ExtraParticleDataBuffers
from game.lib.Math import Math
from game.lib.Random import Random


class LauncherBulletTraceParticleBufferInitializer:

    def __init__(self, particleBufferFactory: FeedbackParticleBufferFactory):
        self.particleBufferFactory = particleBufferFactory

    def makeEmpty(self, trace):
        particlesCount = trace.particlesInGroup * trace.particleGroupsCount
        buffer = self.particleBufferFactory.make(particlesCount, [ExtraParticleDataBuffers.random])

        return buffer

    def init(self, buffer, trace):
        buffer.setAgeData(self.getAgeData(trace))
        buffer.setRandomData(self.getRandomData(trace))

    def getAgeData(self, trace):
        ageData = []
        for groupNumber in range(0, trace.particleGroupsCount):
            appearanceDelayMsec = trace.initDelayMsec + (groupNumber + 1) * trace.particleAppearanceDelayMsec
            ageData.extend([-appearanceDelayMsec] * trace.particlesInGroup)

        return ageData

    def getRandomData(self, trace):
        particlesCount = trace.particlesInGroup * trace.particleGroupsCount
        randomData = []
        for _ in range(particlesCount):
            randomData.append(Random.getFloat(0.0, 1.0))
            randomData.append(Random.getFloat(0.0, 2.0))
            randomData.append(Random.getFloat(-Math.piDouble, Math.piDouble))
            randomData.append(Random.getFloat(0.5, 2.0))

        return randomData
