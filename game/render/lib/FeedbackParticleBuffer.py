# This buffer uses transform feedback to update particles data
class FeedbackParticleBuffer:

    def __init__(self, particlesCount):
        self.particlesCount = particlesCount
        self.particleBuffer1 = None
        self.particleBuffer2 = None

    def setPositionData(self, positionData):
        self.particleBuffer1.setPositionData(positionData)
        self.particleBuffer2.setPositionData(positionData)

    def setVelocityData(self, velocityData):
        self.particleBuffer1.setVelocityData(velocityData)
        self.particleBuffer2.setVelocityData(velocityData)

    def setAgeData(self, ageData):
        self.particleBuffer1.setAgeData(ageData)
        self.particleBuffer2.setAgeData(ageData)

    def setLifeTimeData(self, lifeTimeData):
        self.particleBuffer1.setLifeTimeData(lifeTimeData)
        self.particleBuffer2.setLifeTimeData(lifeTimeData)

    def setColorData(self, colorData):
        self.particleBuffer1.setColorData(colorData)
        self.particleBuffer2.setColorData(colorData)

    def setTexCoordData(self, texCoordData):
        self.particleBuffer1.setTexCoordData(texCoordData)
        self.particleBuffer2.setTexCoordData(texCoordData)

    def setRandomData(self, randomData):
        self.particleBuffer1.setRandomData(randomData)
        self.particleBuffer2.setRandomData(randomData)

    def setVertexAttribDivisor(self, index):
        self.particleBuffer1.setVertexAttribDivisor(index)

    def swapBuffers(self):
        tmp = self.sourceBufferId
        self.sourceBufferId = self.destinationBufferId
        self.destinationBufferId = tmp

        tmp = self.sourceFeedbackId
        self.sourceFeedbackId = self.destinationFeedbackId
        self.destinationFeedbackId = tmp

    def release(self):
        self.particleBuffer1.release()
        self.particleBuffer2.release()
