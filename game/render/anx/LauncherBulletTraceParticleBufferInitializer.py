from game.gl.ParticleBuffer import ParticleBuffer


class LauncherBulletTraceParticleBufferInitializer:

    def makeEmpty(self, trace):
        particlesCount = trace.particlesInGroup * trace.particleGroupsCount
        buffer = ParticleBuffer(particlesCount)

        return buffer

    def init(self, buffer, trace):
        buffer.setInitAgeData(self.getAgeData(trace))

    def getAgeData(self, trace):
        ageData = []
        for groupNumber in range(0, trace.particleGroupsCount):
            appearanceDelayMsec = trace.initDelayMsec + groupNumber * trace.particleAppearanceDelayMsec
            ageData.extend([-appearanceDelayMsec] * trace.particlesInGroup)

        return ageData
