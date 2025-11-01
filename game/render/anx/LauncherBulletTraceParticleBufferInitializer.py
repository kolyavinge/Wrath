from game.gl.ParticleBuffer import ParticleBuffer
from game.lib.Math import Math
from game.lib.Random import Random


class LauncherBulletTraceParticleBufferInitializer:

    def makeEmpty(self, trace):
        particlesCount = trace.particlesInGroup * trace.particleGroupsCount
        buffer = ParticleBuffer(particlesCount)

        return buffer

    def init(self, buffer, trace):
        buffer.setInitAgeData(self.getAgeData(trace))
        buffer.setInitRandomData(self.getRandomData(trace))

    def getAgeData(self, trace):
        ageData = []
        for groupNumber in range(0, trace.particleGroupsCount):
            appearanceDelayMsec = trace.initDelayMsec + groupNumber * trace.particleAppearanceDelayMsec
            ageData.extend([-appearanceDelayMsec] * trace.particlesInGroup)

        return ageData

    def getRandomData(self, trace):
        particlesCount = trace.particlesInGroup * trace.particleGroupsCount
        randomData = []
        for _ in range(particlesCount):
            randomData.append(Random.getFloat(0.0, 1.0))
            randomData.append(Random.getFloat(0.0, 2.0))
            randomData.append(Random.getFloat(-Math.piDouble, Math.piDouble))
            randomData.append(Random.getFloat(0.2, 1.0))

        return randomData
