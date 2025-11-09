from OpenGL.GL import *

from game.gl.FeedbackParticleBuffer import FeedbackParticleBuffer


class ExtraParticleDataBuffers:

    scaleBuffer = 3
    alphaBuffer = 4
    textureBuffer = 5
    random = 6


class FeedbackParticleBufferFactory:

    def make(self, particlesCount, extraDataBuffers=[]):
        particleBuffer = FeedbackParticleBuffer(particlesCount)
        self.initDataBuffers(particleBuffer, extraDataBuffers)
        self.initVertexBuffers(particleBuffer)
        self.initFeedbacks(particleBuffer)
        particleBuffer.sourceBufferId = particleBuffer.particleBuffers[0]
        particleBuffer.destinationBufferId = particleBuffer.particleBuffers[1]
        particleBuffer.sourceFeedbackId = particleBuffer.feedbacks[0]
        particleBuffer.destinationFeedbackId = particleBuffer.feedbacks[1]

        return particleBuffer

    def initDataBuffers(self, particleBuffer, extraDataBuffers):
        particleBuffer.positionBuffers = glGenBuffers(2)
        particleBuffer.velocityBuffers = glGenBuffers(2)
        particleBuffer.ageBuffers = glGenBuffers(2)
        particleBuffer.scaleBuffers = None
        particleBuffer.alphaBuffers = None
        particleBuffer.textureBuffer = None
        particleBuffer.randomBuffer = None

        self.initDataBufferForFeedback(particleBuffer.positionBuffers, particleBuffer.particlesCount, 4, 3)
        self.initDataBufferForFeedback(particleBuffer.velocityBuffers, particleBuffer.particlesCount, 4, 3)
        self.initDataBufferForFeedback(particleBuffer.ageBuffers, particleBuffer.particlesCount, 4, 1)
        if ExtraParticleDataBuffers.scaleBuffer in extraDataBuffers:
            particleBuffer.scaleBuffers = glGenBuffers(2)
            self.initDataBufferForFeedback(particleBuffer.scaleBuffers, 4, 1)
        if ExtraParticleDataBuffers.alphaBuffer in extraDataBuffers:
            particleBuffer.alphaBuffers = glGenBuffers(2)
            self.initDataBufferForFeedback(particleBuffer.alphaBuffers, 4, 1)
        if ExtraParticleDataBuffers.textureBuffer in extraDataBuffers:
            particleBuffer.textureBuffer = glGenBuffers(1)
            self.initDataBuffer(particleBuffer.textureBuffer, particleBuffer.particlesCount, 4, 2)
        if ExtraParticleDataBuffers.random in extraDataBuffers:
            particleBuffer.randomBuffer = glGenBuffers(1)
            self.initDataBuffer(particleBuffer.randomBuffer, particleBuffer.particlesCount, 4, 4)

    def initDataBufferForFeedback(self, buffers, particlesCount, elementSize, elementsCount):
        memorySize = particlesCount * elementSize * elementsCount
        glBindBuffer(GL_ARRAY_BUFFER, buffers[0])
        glBufferData(GL_ARRAY_BUFFER, memorySize, None, GL_DYNAMIC_COPY)
        glBindBuffer(GL_ARRAY_BUFFER, buffers[1])
        glBufferData(GL_ARRAY_BUFFER, memorySize, None, GL_DYNAMIC_COPY)

    def initDataBuffer(self, buffer, particlesCount, elementSize, elementsCount):
        memorySize = particlesCount * elementSize * elementsCount
        glBindBuffer(GL_ARRAY_BUFFER, buffer)
        glBufferData(GL_ARRAY_BUFFER, memorySize, None, GL_DYNAMIC_COPY)

    def initVertexBuffers(self, particleBuffer):
        particleBuffer.particleBuffers = glGenVertexArrays(2)
        self.initVertexBuffer(particleBuffer, 0)
        self.initVertexBuffer(particleBuffer, 1)
        glBindVertexArray(0)

    def initVertexBuffer(self, particleBuffer, vertexBufferIndex):
        glBindVertexArray(particleBuffer.particleBuffers[vertexBufferIndex])

        glBindBuffer(GL_ARRAY_BUFFER, particleBuffer.positionBuffers[vertexBufferIndex])
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)
        glEnableVertexAttribArray(0)

        glBindBuffer(GL_ARRAY_BUFFER, particleBuffer.velocityBuffers[vertexBufferIndex])
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 0, None)
        glEnableVertexAttribArray(1)

        glBindBuffer(GL_ARRAY_BUFFER, particleBuffer.ageBuffers[vertexBufferIndex])
        glVertexAttribPointer(2, 1, GL_FLOAT, GL_FALSE, 0, None)
        glEnableVertexAttribArray(2)

        if particleBuffer.scaleBuffers is not None:
            glBindBuffer(GL_ARRAY_BUFFER, particleBuffer.scaleBuffers[vertexBufferIndex])
            glVertexAttribPointer(3, 1, GL_FLOAT, GL_FALSE, 0, None)
            glEnableVertexAttribArray(3)

        if particleBuffer.alphaBuffers is not None:
            glBindBuffer(GL_ARRAY_BUFFER, particleBuffer.alphaBuffers[vertexBufferIndex])
            glVertexAttribPointer(4, 1, GL_FLOAT, GL_FALSE, 0, None)
            glEnableVertexAttribArray(4)

        if particleBuffer.textureBuffer is not None:
            glBindBuffer(GL_ARRAY_BUFFER, particleBuffer.textureBuffer)
            glVertexAttribPointer(5, 2, GL_FLOAT, GL_FALSE, 0, None)
            glEnableVertexAttribArray(5)

        if particleBuffer.randomBuffer is not None:
            glBindBuffer(GL_ARRAY_BUFFER, particleBuffer.randomBuffer)
            glVertexAttribPointer(6, 4, GL_FLOAT, GL_FALSE, 0, None)
            glEnableVertexAttribArray(6)

    def initFeedbacks(self, particleBuffer):
        particleBuffer.feedbacks = glGenTransformFeedbacks(2)
        self.initFeedback(particleBuffer, 0)
        self.initFeedback(particleBuffer, 1)
        glBindTransformFeedback(GL_TRANSFORM_FEEDBACK, 0)

    def initFeedback(self, particleBuffer, feedbackIndex):
        glBindTransformFeedback(GL_TRANSFORM_FEEDBACK, particleBuffer.feedbacks[feedbackIndex])
        glBindBufferBase(GL_TRANSFORM_FEEDBACK_BUFFER, 0, particleBuffer.positionBuffers[feedbackIndex])
        glBindBufferBase(GL_TRANSFORM_FEEDBACK_BUFFER, 1, particleBuffer.velocityBuffers[feedbackIndex])
        glBindBufferBase(GL_TRANSFORM_FEEDBACK_BUFFER, 2, particleBuffer.ageBuffers[feedbackIndex])
        if particleBuffer.scaleBuffers is not None:
            glBindBufferBase(GL_TRANSFORM_FEEDBACK_BUFFER, 3, particleBuffer.scaleBuffers[feedbackIndex])
        if particleBuffer.alphaBuffers is not None:
            glBindBufferBase(GL_TRANSFORM_FEEDBACK_BUFFER, 4, particleBuffer.alphaBuffers[feedbackIndex])
