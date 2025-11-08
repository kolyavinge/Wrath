import numpy
from OpenGL.GL import *


class ExtraParticleDataBuffers:

    scaleBuffer = 3
    alphaBuffer = 4
    textureBuffer = 5
    random = 6


# This buffer uses transform feedback to update particles data
class FeedbackParticleBuffer:

    def __init__(self, particlesCount, extraDataBuffers=[]):
        self.particlesCount = particlesCount
        self.initDataBuffers(extraDataBuffers)
        self.initVertexBuffers()
        self.initFeedbacks()
        self.sourceBufferId = self.particleBuffers[0]
        self.destinationBufferId = self.particleBuffers[1]
        self.sourceFeedbackId = self.feedbacks[0]
        self.destinationFeedbackId = self.feedbacks[1]

    def initDataBuffers(self, extraDataBuffers):
        self.positionBuffers = glGenBuffers(2)
        self.velocityBuffers = glGenBuffers(2)
        self.ageBuffers = glGenBuffers(2)
        self.scaleBuffers = None
        self.alphaBuffers = None
        self.textureBuffer = None
        self.randomBuffer = None

        self.initDataBufferForFeedback(self.positionBuffers, 4, 3)
        self.initDataBufferForFeedback(self.velocityBuffers, 4, 3)
        self.initDataBufferForFeedback(self.ageBuffers, 4, 1)
        if ExtraParticleDataBuffers.scaleBuffer in extraDataBuffers:
            self.scaleBuffers = glGenBuffers(2)
            self.initDataBufferForFeedback(self.scaleBuffers, 4, 1)
        if ExtraParticleDataBuffers.alphaBuffer in extraDataBuffers:
            self.alphaBuffers = glGenBuffers(2)
            self.initDataBufferForFeedback(self.alphaBuffers, 4, 1)
        if ExtraParticleDataBuffers.textureBuffer in extraDataBuffers:
            self.textureBuffer = glGenBuffers(1)
            self.initDataBuffer(self.textureBuffer, 4, 2)
        if ExtraParticleDataBuffers.random in extraDataBuffers:
            self.randomBuffer = glGenBuffers(1)
            self.initDataBuffer(self.randomBuffer, 4, 4)

    def initDataBufferForFeedback(self, buffers, elementSize, elementsCount):
        memorySize = self.particlesCount * elementSize * elementsCount
        glBindBuffer(GL_ARRAY_BUFFER, buffers[0])
        glBufferData(GL_ARRAY_BUFFER, memorySize, None, GL_DYNAMIC_COPY)
        glBindBuffer(GL_ARRAY_BUFFER, buffers[1])
        glBufferData(GL_ARRAY_BUFFER, memorySize, None, GL_DYNAMIC_COPY)

    def initDataBuffer(self, buffer, elementSize, elementsCount):
        memorySize = self.particlesCount * elementSize * elementsCount
        glBindBuffer(GL_ARRAY_BUFFER, buffer)
        glBufferData(GL_ARRAY_BUFFER, memorySize, None, GL_DYNAMIC_COPY)

    def initVertexBuffers(self):
        self.particleBuffers = glGenVertexArrays(2)
        self.initVertexBuffer(0)
        self.initVertexBuffer(1)
        glBindVertexArray(0)

    def initVertexBuffer(self, vertexBufferIndex):
        glBindVertexArray(self.particleBuffers[vertexBufferIndex])

        glBindBuffer(GL_ARRAY_BUFFER, self.positionBuffers[vertexBufferIndex])
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)
        glEnableVertexAttribArray(0)

        glBindBuffer(GL_ARRAY_BUFFER, self.velocityBuffers[vertexBufferIndex])
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 0, None)
        glEnableVertexAttribArray(1)

        glBindBuffer(GL_ARRAY_BUFFER, self.ageBuffers[vertexBufferIndex])
        glVertexAttribPointer(2, 1, GL_FLOAT, GL_FALSE, 0, None)
        glEnableVertexAttribArray(2)

        if self.scaleBuffers is not None:
            glBindBuffer(GL_ARRAY_BUFFER, self.scaleBuffers[vertexBufferIndex])
            glVertexAttribPointer(3, 1, GL_FLOAT, GL_FALSE, 0, None)
            glEnableVertexAttribArray(3)

        if self.alphaBuffers is not None:
            glBindBuffer(GL_ARRAY_BUFFER, self.alphaBuffers[vertexBufferIndex])
            glVertexAttribPointer(4, 1, GL_FLOAT, GL_FALSE, 0, None)
            glEnableVertexAttribArray(4)

        if self.textureBuffer is not None:
            glBindBuffer(GL_ARRAY_BUFFER, self.textureBuffer)
            glVertexAttribPointer(5, 2, GL_FLOAT, GL_FALSE, 0, None)
            glEnableVertexAttribArray(5)

        if self.randomBuffer is not None:
            glBindBuffer(GL_ARRAY_BUFFER, self.randomBuffer)
            glVertexAttribPointer(6, 4, GL_FLOAT, GL_FALSE, 0, None)
            glEnableVertexAttribArray(6)

    def initFeedbacks(self):
        self.feedbacks = glGenTransformFeedbacks(2)
        self.initFeedback(0)
        self.initFeedback(1)
        glBindTransformFeedback(GL_TRANSFORM_FEEDBACK, 0)

    def initFeedback(self, feedbackIndex):
        glBindTransformFeedback(GL_TRANSFORM_FEEDBACK, self.feedbacks[feedbackIndex])
        glBindBufferBase(GL_TRANSFORM_FEEDBACK_BUFFER, 0, self.positionBuffers[feedbackIndex])
        glBindBufferBase(GL_TRANSFORM_FEEDBACK_BUFFER, 1, self.velocityBuffers[feedbackIndex])
        glBindBufferBase(GL_TRANSFORM_FEEDBACK_BUFFER, 2, self.ageBuffers[feedbackIndex])
        if self.scaleBuffers is not None:
            glBindBufferBase(GL_TRANSFORM_FEEDBACK_BUFFER, 3, self.scaleBuffers[feedbackIndex])
        if self.alphaBuffers is not None:
            glBindBufferBase(GL_TRANSFORM_FEEDBACK_BUFFER, 4, self.alphaBuffers[feedbackIndex])

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
        data = numpy.array(scaleData, dtype=numpy.float32)
        self.setData(self.scaleBuffers[0], data)
        self.setData(self.scaleBuffers[1], data)

    def setAlphaData(self, alphaData):
        data = numpy.array(alphaData, dtype=numpy.float32)
        self.setData(self.alphaBuffers[0], data)
        self.setData(self.alphaBuffers[1], data)

    def setTextureData(self, textureData):
        data = numpy.array(textureData, dtype=numpy.float32)
        self.setData(self.textureBuffer, data)

    def setRandomData(self, randomData):
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
        if self.alphaBuffers is not None:
            glVertexAttribDivisor(4, index)

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
        if self.alphaBuffers is not None:
            glDeleteBuffers(len(self.alphaBuffers), self.alphaBuffers)
        if self.textureBuffer is not None:
            glDeleteBuffers(1, self.textureBuffer)
        if self.randomBuffer is not None:
            glDeleteBuffers(1, self.randomBuffer)
        self.feedbacks = None
        self.particleBuffers = None
        self.positionBuffers = None
        self.velocityBuffers = None
        self.ageBuffers = None
        self.scaleBuffers = None
        self.alphaBuffers = None
        self.textureBuffer = None
        self.randomBuffer = None
