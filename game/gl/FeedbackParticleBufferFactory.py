from OpenGL.GL import *

from game.gl.FeedbackParticleBuffer import FeedbackParticleBuffer
from game.gl.ParticleBufferFactory import ParticleBufferFactory


class FeedbackParticleBufferFactory:

    def __init__(self, particleBufferFactory: ParticleBufferFactory):
        self.particleBufferFactory = particleBufferFactory

    def make(self, particlesCount, extraDataBuffers=[]):
        feedbackParticleBuffer = FeedbackParticleBuffer(particlesCount)

        # make first particle buffer with all data buffers
        feedbackParticleBuffer.particleBuffer1 = self.particleBufferFactory.make(particlesCount, extraDataBuffers)

        # make second particle buffer for feedback with data buffers no need feedback
        # bind these share data buffers from first particle buffer
        feedbackParticleBuffer.particleBuffer2 = self.particleBufferFactory.make(particlesCount)
        self.bindShareDataBuffersNoNeedFeedback(feedbackParticleBuffer)

        self.initFeedbacks(feedbackParticleBuffer)

        return feedbackParticleBuffer

    def bindShareDataBuffersNoNeedFeedback(self, feedbackParticleBuffer):
        glBindVertexArray(feedbackParticleBuffer.particleBuffer2.vaid)

        if feedbackParticleBuffer.particleBuffer1.lifeTimeBuffer is not None:
            feedbackParticleBuffer.particleBuffer2.lifeTimeBuffer = feedbackParticleBuffer.particleBuffer1.lifeTimeBuffer
            glBindBuffer(GL_ARRAY_BUFFER, feedbackParticleBuffer.particleBuffer1.lifeTimeBuffer)
            glVertexAttribPointer(3, 1, GL_FLOAT, GL_FALSE, 0, None)
            glEnableVertexAttribArray(3)

        if feedbackParticleBuffer.particleBuffer1.colorBuffer is not None:
            feedbackParticleBuffer.particleBuffer2.colorBuffer = feedbackParticleBuffer.particleBuffer1.colorBuffer
            glBindBuffer(GL_ARRAY_BUFFER, feedbackParticleBuffer.particleBuffer1.colorBuffer)
            glVertexAttribPointer(4, 4, GL_FLOAT, GL_FALSE, 0, None)
            glEnableVertexAttribArray(4)

        if feedbackParticleBuffer.particleBuffer1.texCoordBuffer is not None:
            feedbackParticleBuffer.particleBuffer2.texCoordBuffer = feedbackParticleBuffer.particleBuffer1.texCoordBuffer
            glBindBuffer(GL_ARRAY_BUFFER, feedbackParticleBuffer.particleBuffer1.texCoordBuffer)
            glVertexAttribPointer(5, 4, GL_FLOAT, GL_FALSE, 0, None)
            glEnableVertexAttribArray(5)

        if feedbackParticleBuffer.particleBuffer1.randomBuffer is not None:
            feedbackParticleBuffer.particleBuffer2.randomBuffer = feedbackParticleBuffer.particleBuffer1.randomBuffer
            glBindBuffer(GL_ARRAY_BUFFER, feedbackParticleBuffer.particleBuffer1.randomBuffer)
            glVertexAttribPointer(6, 4, GL_FLOAT, GL_FALSE, 0, None)
            glEnableVertexAttribArray(6)

        glBindVertexArray(0)

    def initFeedbacks(self, feedbackParticleBuffer):
        feedbackParticleBuffer.feedbacks = glGenTransformFeedbacks(2)
        self.initFeedback(feedbackParticleBuffer.particleBuffer1, feedbackParticleBuffer.feedbacks[0])
        self.initFeedback(feedbackParticleBuffer.particleBuffer2, feedbackParticleBuffer.feedbacks[1])
        glBindTransformFeedback(GL_TRANSFORM_FEEDBACK, 0)
        # init fields to swap buffers
        feedbackParticleBuffer.sourceBufferId = feedbackParticleBuffer.particleBuffer1.vaid
        feedbackParticleBuffer.destinationBufferId = feedbackParticleBuffer.particleBuffer2.vaid
        feedbackParticleBuffer.sourceFeedbackId = feedbackParticleBuffer.feedbacks[0]
        feedbackParticleBuffer.destinationFeedbackId = feedbackParticleBuffer.feedbacks[1]

    def initFeedback(self, particleBuffer, feedbackBuffer):
        glBindTransformFeedback(GL_TRANSFORM_FEEDBACK, feedbackBuffer)
        glBindBufferBase(GL_TRANSFORM_FEEDBACK_BUFFER, 0, particleBuffer.positionBuffer)
        glBindBufferBase(GL_TRANSFORM_FEEDBACK_BUFFER, 1, particleBuffer.velocityBuffer)
        glBindBufferBase(GL_TRANSFORM_FEEDBACK_BUFFER, 2, particleBuffer.ageBuffer)
