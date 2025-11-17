from OpenGL.GL import *

from game.gl.ParticleBuffer import ExtraParticleDataBuffers, ParticleBuffer


class ParticleBufferFactory:

    def make(self, particlesCount, extraDataBuffers=[]):
        particleBuffer = ParticleBuffer(particlesCount)
        self.initDataBuffers(particleBuffer, extraDataBuffers)
        self.initVertexBuffer(particleBuffer)

        return particleBuffer

    def initDataBuffers(self, particleBuffer, extraDataBuffers):
        particleBuffer.positionBuffer = glGenBuffers(1)
        particleBuffer.velocityBuffer = glGenBuffers(1)
        particleBuffer.ageBuffer = glGenBuffers(1)
        particleBuffer.scaleBuffer = None
        particleBuffer.colorBuffer = None
        particleBuffer.texCoordBuffer = None
        particleBuffer.randomBuffer = None

        self.initDataBuffer(particleBuffer.positionBuffer, particleBuffer.particlesCount, 4, 3)
        self.initDataBuffer(particleBuffer.velocityBuffer, particleBuffer.particlesCount, 4, 3)
        self.initDataBuffer(particleBuffer.ageBuffer, particleBuffer.particlesCount, 4, 1)
        if ExtraParticleDataBuffers.scaleBuffer in extraDataBuffers:
            particleBuffer.scaleBuffer = glGenBuffers(1)
            self.initDataBuffer(particleBuffer.scaleBuffer, 4, 1)
        if ExtraParticleDataBuffers.colorBuffer in extraDataBuffers:
            particleBuffer.colorBuffer = glGenBuffers(1)
            self.initDataBuffer(particleBuffer.colorBuffer, 4, 4)
        if ExtraParticleDataBuffers.texCoordBuffer in extraDataBuffers:
            particleBuffer.texCoordBuffer = glGenBuffers(1)
            self.initDataBuffer(particleBuffer.texCoordBuffer, particleBuffer.particlesCount, 4, 4)
        if ExtraParticleDataBuffers.random in extraDataBuffers:
            particleBuffer.randomBuffer = glGenBuffers(1)
            self.initDataBuffer(particleBuffer.randomBuffer, particleBuffer.particlesCount, 4, 4)

    def initDataBuffer(self, buffer, particlesCount, elementSize, elementsCount):
        memorySize = particlesCount * elementSize * elementsCount
        glBindBuffer(GL_ARRAY_BUFFER, buffer)
        glBufferData(GL_ARRAY_BUFFER, memorySize, None, GL_DYNAMIC_COPY)

    def initVertexBuffer(self, particleBuffer):
        particleBuffer.vaid = glGenVertexArrays(1)
        glBindVertexArray(particleBuffer.vaid)

        glBindBuffer(GL_ARRAY_BUFFER, particleBuffer.positionBuffer)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)
        glEnableVertexAttribArray(0)

        glBindBuffer(GL_ARRAY_BUFFER, particleBuffer.velocityBuffer)
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 0, None)
        glEnableVertexAttribArray(1)

        glBindBuffer(GL_ARRAY_BUFFER, particleBuffer.ageBuffer)
        glVertexAttribPointer(2, 1, GL_FLOAT, GL_FALSE, 0, None)
        glEnableVertexAttribArray(2)

        if particleBuffer.scaleBuffer is not None:
            glBindBuffer(GL_ARRAY_BUFFER, particleBuffer.scaleBuffer)
            glVertexAttribPointer(3, 1, GL_FLOAT, GL_FALSE, 0, None)
            glEnableVertexAttribArray(3)

        if particleBuffer.colorBuffer is not None:
            glBindBuffer(GL_ARRAY_BUFFER, particleBuffer.colorBuffer)
            glVertexAttribPointer(4, 4, GL_FLOAT, GL_FALSE, 0, None)
            glEnableVertexAttribArray(4)

        if particleBuffer.texCoordBuffer is not None:
            glBindBuffer(GL_ARRAY_BUFFER, particleBuffer.texCoordBuffer)
            glVertexAttribPointer(5, 4, GL_FLOAT, GL_FALSE, 0, None)
            glEnableVertexAttribArray(5)

        if particleBuffer.randomBuffer is not None:
            glBindBuffer(GL_ARRAY_BUFFER, particleBuffer.randomBuffer)
            glVertexAttribPointer(6, 4, GL_FLOAT, GL_FALSE, 0, None)
            glEnableVertexAttribArray(6)

        glBindVertexArray(0)
