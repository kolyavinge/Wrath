import numpy
from OpenGL.GL import *


class ParticleBuffer:

    def __init__(self, particlesCount):
        self.particlesCount = particlesCount
        self.initDataBuffers()
        self.initVertexBuffers()
        self.initFeedbacks()
        self.sourceBufferId = self.particleBuffers[0]
        self.destinationBufferId = self.particleBuffers[1]
        self.sourceFeedbackId = self.feedbacks[0]
        self.destinationFeedbackId = self.feedbacks[1]

    def initDataBuffers(self):
        # transform feedback to update particle data

        self.positionBuffers = glGenBuffers(2)
        self.velocityBuffers = glGenBuffers(2)
        self.ageBuffers = glGenBuffers(2)
        self.randomBuffer = glGenBuffers(1)

        # set position data
        glBindBuffer(GL_ARRAY_BUFFER, self.positionBuffers[0])
        glBufferData(GL_ARRAY_BUFFER, self.particlesCount * 4 * 3, None, GL_DYNAMIC_COPY)
        glBindBuffer(GL_ARRAY_BUFFER, self.positionBuffers[1])
        glBufferData(GL_ARRAY_BUFFER, self.particlesCount * 4 * 3, None, GL_DYNAMIC_COPY)

        # set velocity data
        glBindBuffer(GL_ARRAY_BUFFER, self.velocityBuffers[0])
        glBufferData(GL_ARRAY_BUFFER, self.particlesCount * 4 * 3, None, GL_DYNAMIC_COPY)
        glBindBuffer(GL_ARRAY_BUFFER, self.velocityBuffers[1])
        glBufferData(GL_ARRAY_BUFFER, self.particlesCount * 4 * 3, None, GL_DYNAMIC_COPY)

        # set age data
        glBindBuffer(GL_ARRAY_BUFFER, self.ageBuffers[0])
        glBufferData(GL_ARRAY_BUFFER, self.particlesCount * 4, None, GL_DYNAMIC_COPY)
        glBindBuffer(GL_ARRAY_BUFFER, self.ageBuffers[1])
        glBufferData(GL_ARRAY_BUFFER, self.particlesCount * 4, None, GL_DYNAMIC_COPY)

        # set random data
        glBindBuffer(GL_ARRAY_BUFFER, self.randomBuffer)
        glBufferData(GL_ARRAY_BUFFER, self.particlesCount * 4 * 4, None, GL_STATIC_DRAW)

        glBindBuffer(GL_ARRAY_BUFFER, 0)

    def initVertexBuffers(self):
        self.particleBuffers = glGenVertexArrays(2)

        # first
        glBindVertexArray(self.particleBuffers[0])

        glBindBuffer(GL_ARRAY_BUFFER, self.positionBuffers[0])
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)
        glEnableVertexAttribArray(0)

        glBindBuffer(GL_ARRAY_BUFFER, self.velocityBuffers[0])
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 0, None)
        glEnableVertexAttribArray(1)

        glBindBuffer(GL_ARRAY_BUFFER, self.ageBuffers[0])
        glVertexAttribPointer(2, 1, GL_FLOAT, GL_FALSE, 0, None)
        glEnableVertexAttribArray(2)

        glBindBuffer(GL_ARRAY_BUFFER, self.randomBuffer)
        glVertexAttribPointer(3, 4, GL_FLOAT, GL_FALSE, 0, None)
        glEnableVertexAttribArray(3)

        # second
        glBindVertexArray(self.particleBuffers[1])

        glBindBuffer(GL_ARRAY_BUFFER, self.positionBuffers[1])
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)
        glEnableVertexAttribArray(0)

        glBindBuffer(GL_ARRAY_BUFFER, self.velocityBuffers[1])
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 0, None)
        glEnableVertexAttribArray(1)

        glBindBuffer(GL_ARRAY_BUFFER, self.ageBuffers[1])
        glVertexAttribPointer(2, 1, GL_FLOAT, GL_FALSE, 0, None)
        glEnableVertexAttribArray(2)

        glBindBuffer(GL_ARRAY_BUFFER, self.randomBuffer)
        glVertexAttribPointer(3, 4, GL_FLOAT, GL_FALSE, 0, None)
        glEnableVertexAttribArray(3)

        glBindVertexArray(0)

    def initFeedbacks(self):
        self.feedbacks = glGenTransformFeedbacks(2)

        glBindTransformFeedback(GL_TRANSFORM_FEEDBACK, self.feedbacks[0])
        glBindBufferBase(GL_TRANSFORM_FEEDBACK_BUFFER, 0, self.positionBuffers[0])
        glBindBufferBase(GL_TRANSFORM_FEEDBACK_BUFFER, 1, self.velocityBuffers[0])
        glBindBufferBase(GL_TRANSFORM_FEEDBACK_BUFFER, 2, self.ageBuffers[0])

        glBindTransformFeedback(GL_TRANSFORM_FEEDBACK, self.feedbacks[1])
        glBindBufferBase(GL_TRANSFORM_FEEDBACK_BUFFER, 0, self.positionBuffers[1])
        glBindBufferBase(GL_TRANSFORM_FEEDBACK_BUFFER, 1, self.velocityBuffers[1])
        glBindBufferBase(GL_TRANSFORM_FEEDBACK_BUFFER, 2, self.ageBuffers[1])

        glBindTransformFeedback(GL_TRANSFORM_FEEDBACK, 0)

    def setInitAgeData(self, ageData):
        ageData = numpy.array(ageData, dtype=numpy.float32)
        glBindBuffer(GL_ARRAY_BUFFER, self.ageBuffers[0])
        glBufferSubData(GL_ARRAY_BUFFER, 0, ageData.nbytes, ageData)

    def setInitRandomData(self, randomData):
        randomData = numpy.array(randomData, dtype=numpy.float32)
        glBindBuffer(GL_ARRAY_BUFFER, self.randomBuffer)
        glBufferSubData(GL_ARRAY_BUFFER, 0, randomData.nbytes, randomData)
        glBindBuffer(GL_ARRAY_BUFFER, 0)

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
        glDeleteBuffers(1, self.randomBuffer)
        self.feedbacks = None
        self.particleBuffers = None
        self.positionBuffers = None
        self.velocityBuffers = None
        self.ageBuffers = None
        self.randomBuffer = None
