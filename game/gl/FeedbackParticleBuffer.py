import numpy
from OpenGL.GL import *


# This buffer uses transform feedback to update particles data
class FeedbackParticleBuffer:

    def __init__(self, particlesCount):
        self.particlesCount = particlesCount

    def setPositionData(self, positionData):
        plainData = []
        for vector in positionData:
            plainData.append(vector.x)
            plainData.append(vector.y)
            plainData.append(vector.z)
        plainData = numpy.array(plainData, dtype=numpy.float32)
        self.setData(self.positionBuffers[0], plainData)
        self.setData(self.positionBuffers[1], plainData)

    def setVelocityData(self, velocityData):
        plainData = []
        for vector in velocityData:
            plainData.append(vector.x)
            plainData.append(vector.y)
            plainData.append(vector.z)
        plainData = numpy.array(plainData, dtype=numpy.float32)
        self.setData(self.velocityBuffers[0], plainData)
        self.setData(self.velocityBuffers[1], plainData)

    def setAgeData(self, ageData):
        data = numpy.array(ageData, dtype=numpy.float32)
        self.setData(self.ageBuffers[0], data)
        self.setData(self.ageBuffers[1], data)

    def setScaleData(self, scaleData):
        if self.scaleBuffers is None:
            raise Exception("Scale buffer is not initialized")
        data = numpy.array(scaleData, dtype=numpy.float32)
        self.setData(self.scaleBuffers[0], data)
        self.setData(self.scaleBuffers[1], data)

    def setColorData(self, colorData):
        if self.colorBuffers is None:
            raise Exception("Color buffer is not initialized")
        plainData = []
        for vector in colorData:
            plainData.append(vector.x)
            plainData.append(vector.y)
            plainData.append(vector.z)
            plainData.append(vector.w)
        plainData = numpy.array(plainData, dtype=numpy.float32)
        self.setData(self.colorBuffers[0], plainData)
        self.setData(self.colorBuffers[1], plainData)

    def setTexCoordData(self, texCoordData):
        if self.texCoordBuffer is None:
            raise Exception("TexCoord buffer is not initialized")
        plainData = []
        for vector in texCoordData:
            plainData.append(vector.x)
            plainData.append(vector.y)
            plainData.append(vector.z)
            plainData.append(vector.w)
        plainData = numpy.array(texCoordData, dtype=numpy.float32)
        self.setData(self.texCoordBuffer, plainData)

    def setRandomData(self, randomData):
        if self.randomBuffer is None:
            raise Exception("Random buffer is not initialized")
        data = numpy.array(randomData, dtype=numpy.float32)
        self.setData(self.randomBuffer, data)

    def setData(self, bufferId, data):
        glBindBuffer(GL_ARRAY_BUFFER, bufferId)
        glBufferSubData(GL_ARRAY_BUFFER, 0, data.nbytes, data)
        glBindBuffer(GL_ARRAY_BUFFER, 0)

    def setVertexAttribDivisor(self, index):
        glVertexAttribDivisor(0, index)
        glVertexAttribDivisor(1, index)
        glVertexAttribDivisor(2, index)
        if self.scaleBuffers is not None:
            glVertexAttribDivisor(3, index)
        if self.colorBuffers is not None:
            glVertexAttribDivisor(4, index)
        if self.texCoordBuffer is not None:
            glVertexAttribDivisor(5, index)
        if self.randomBuffer is not None:
            glVertexAttribDivisor(6, index)

    def swapBuffers(self):
        tmp = self.sourceBufferId
        self.sourceBufferId = self.destinationBufferId
        self.destinationBufferId = tmp

        tmp = self.sourceFeedbackId
        self.sourceFeedbackId = self.destinationFeedbackId
        self.destinationFeedbackId = tmp

    def release(self):
        glDeleteTransformFeedbacks(len(self.feedbacks), self.feedbacks)
        glDeleteVertexArrays(len(self.particleBuffers), self.particleBuffers)
        glDeleteBuffers(len(self.positionBuffers), self.positionBuffers)
        glDeleteBuffers(len(self.velocityBuffers), self.velocityBuffers)
        glDeleteBuffers(len(self.ageBuffers), self.ageBuffers)
        if self.scaleBuffers is not None:
            glDeleteBuffers(len(self.scaleBuffers), self.scaleBuffers)
        if self.colorBuffers is not None:
            glDeleteBuffers(len(self.colorBuffers), self.colorBuffers)
        if self.texCoordBuffer is not None:
            glDeleteBuffers(1, self.texCoordBuffer)
        if self.randomBuffer is not None:
            glDeleteBuffers(1, self.randomBuffer)
        self.feedbacks = None
        self.particleBuffers = None
        self.positionBuffers = None
        self.velocityBuffers = None
        self.ageBuffers = None
        self.scaleBuffers = None
        self.colorBuffers = None
        self.texCoordBuffer = None
        self.randomBuffer = None
