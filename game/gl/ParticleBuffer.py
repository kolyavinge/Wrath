import numpy
from OpenGL.GL import *


class ExtraParticleDataBuffers:

    lifeTimeBuffer = 3
    colorBuffer = 4
    texCoordBuffer = 5
    random = 6


class ParticleBuffer:

    def __init__(self, particlesCount):
        self.particlesCount = particlesCount

    def setPositionData(self, positionData):
        plainData = []
        for vector in positionData:
            plainData.append(vector.x)
            plainData.append(vector.y)
            plainData.append(vector.z)
        plainData = numpy.array(plainData, dtype=numpy.float32)
        self.setData(self.positionBuffer, plainData)

    def setVelocityData(self, velocityData):
        plainData = []
        for vector in velocityData:
            plainData.append(vector.x)
            plainData.append(vector.y)
            plainData.append(vector.z)
        plainData = numpy.array(plainData, dtype=numpy.float32)
        self.setData(self.velocityBuffer, plainData)

    def setAgeData(self, ageData):
        data = numpy.array(ageData, dtype=numpy.float32)
        self.setData(self.ageBuffer, data)

    def setLifeTimeData(self, lifeTimeData):
        if self.lifeTimeBuffer is None:
            raise Exception("LifeTime buffer is not initialized")
        data = numpy.array(lifeTimeData, dtype=numpy.float32)
        self.setData(self.lifeTimeBuffer, data)

    def setColorData(self, colorData):
        if self.colorBuffer is None:
            raise Exception("Color buffer is not initialized")
        plainData = []
        for vector in colorData:
            plainData.append(vector.x)
            plainData.append(vector.y)
            plainData.append(vector.z)
            plainData.append(vector.w)
        plainData = numpy.array(plainData, dtype=numpy.float32)
        self.setData(self.colorBuffer, plainData)

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
        if self.lifeTimeBuffer is not None:
            glVertexAttribDivisor(3, index)
        if self.colorBuffer is not None:
            glVertexAttribDivisor(4, index)
        if self.texCoordBuffer is not None:
            glVertexAttribDivisor(5, index)
        if self.randomBuffer is not None:
            glVertexAttribDivisor(6, index)

    def release(self):
        glDeleteVertexArrays(1, self.vaid)
        glDeleteBuffers(1, self.positionBuffer)
        glDeleteBuffers(1, self.velocityBuffer)
        glDeleteBuffers(1, self.ageBuffer)
        if self.lifeTimeBuffer is not None:
            glDeleteBuffers(1, self.lifeTimeBuffer)
        if self.colorBuffer is not None:
            glDeleteBuffers(1, self.colorBuffer)
        if self.texCoordBuffer is not None:
            glDeleteBuffers(1, self.texCoordBuffer)
        if self.randomBuffer is not None:
            glDeleteBuffers(1, self.randomBuffer)
        self.vaid = None
        self.positionBuffer = None
        self.velocityBuffer = None
        self.ageBuffer = None
        self.lifeTimeBuffer = None
        self.colorBuffer = None
        self.texCoordBuffer = None
        self.randomBuffer = None
