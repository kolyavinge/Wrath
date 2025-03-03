from OpenGL.GL import *

from game.gl.BufferIndices import BufferIndices
from game.gl.vbo.UpdatableVBO import UpdatableVBO
from game.lib.Math import Math


class VBOUpdater:

    def beginUpdate(self, vbo):
        self.newVerticesCount = 0
        self.vbo = vbo

    def endUpdate(self):
        self.vbo.verticesCount += self.newVerticesCount
        self.vbo = None
        glBindBuffer(GL_ARRAY_BUFFER, 0)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0)

    def setVertex(self, index, vector):
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo.vboIds[BufferIndices.vertices])
        mapBuffer = glMapBuffer(GL_ARRAY_BUFFER, GL_WRITE_ONLY)
        mapArray = (GLfloat * (3 * self.vbo.maxVerticesCount)).from_address(mapBuffer)
        mapArray[3 * index] = vector.x
        mapArray[3 * index + 1] = vector.y
        mapArray[3 * index + 2] = vector.z
        glUnmapBuffer(GL_ARRAY_BUFFER)

    def setTexCoord(self, index, x, y):
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo.vboIds[BufferIndices.texCoords])
        mapBuffer = glMapBuffer(GL_ARRAY_BUFFER, GL_WRITE_ONLY)
        mapArray = (GLfloat * (2 * self.vbo.maxVerticesCount)).from_address(mapBuffer)
        mapArray[2 * index] = x
        mapArray[2 * index + 1] = y
        glUnmapBuffer(GL_ARRAY_BUFFER)

    def addVertex(self, vector):
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo.vboIds[BufferIndices.vertices])
        mapBuffer = glMapBuffer(GL_ARRAY_BUFFER, GL_WRITE_ONLY)
        mapArray = (GLfloat * (3 * self.vbo.maxVerticesCount)).from_address(mapBuffer)
        mapArray[self.vbo.verticesLastIndex] = vector.x
        mapArray[self.vbo.verticesLastIndex + 1] = vector.y
        mapArray[self.vbo.verticesLastIndex + 2] = vector.z
        glUnmapBuffer(GL_ARRAY_BUFFER)
        self.vbo.verticesLastIndex += 3
        self.newVerticesCount += 1

    def addNormal(self, vector):
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo.vboIds[BufferIndices.normals])
        mapBuffer = glMapBuffer(GL_ARRAY_BUFFER, GL_WRITE_ONLY)
        mapArray = (GLfloat * (3 * self.vbo.maxVerticesCount)).from_address(mapBuffer)
        mapArray[self.vbo.normalsLastIndex] = vector.x
        mapArray[self.vbo.normalsLastIndex + 1] = vector.y
        mapArray[self.vbo.normalsLastIndex + 2] = vector.z
        glUnmapBuffer(GL_ARRAY_BUFFER)
        self.vbo.normalsLastIndex += 3

    def addTexCoord(self, x, y):
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo.vboIds[BufferIndices.texCoords])
        mapBuffer = glMapBuffer(GL_ARRAY_BUFFER, GL_WRITE_ONLY)
        mapArray = (GLfloat * (2 * self.vbo.maxVerticesCount)).from_address(mapBuffer)
        mapArray[self.vbo.texCoordsLastIndex] = x
        mapArray[self.vbo.texCoordsLastIndex + 1] = y
        glUnmapBuffer(GL_ARRAY_BUFFER)
        self.vbo.texCoordsLastIndex += 2

    def addFace(self, i1, i2, i3):
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.vbo.vboIds[BufferIndices.faces])
        mapBuffer = glMapBuffer(GL_ELEMENT_ARRAY_BUFFER, GL_WRITE_ONLY)
        mapArray = (GLuint * (3 * self.vbo.maxFacesCount)).from_address(mapBuffer)
        mapArray[self.vbo.faceLastIndex] = self.vbo.verticesCount + i1
        mapArray[self.vbo.faceLastIndex + 1] = self.vbo.verticesCount + i2
        mapArray[self.vbo.faceLastIndex + 2] = self.vbo.verticesCount + i3
        glUnmapBuffer(GL_ELEMENT_ARRAY_BUFFER)
        self.vbo.elementsCount = Math.min(self.vbo.elementsCount + 3, self.vbo.maxElementsCount)
        self.vbo.faceLastIndex += 3

    def buildUnfilled(self, maxVerticesCount, maxFacesCount, bufferIndices=BufferIndices.all):
        vaoId = glGenVertexArrays(1)
        glBindVertexArray(vaoId)

        vboIds = [0, 0, 0, 0]

        if BufferIndices.vertices in bufferIndices:
            vboId = glGenBuffers(1)
            glBindBuffer(GL_ARRAY_BUFFER, vboId)
            glBufferData(GL_ARRAY_BUFFER, 3 * 4 * maxVerticesCount, None, GL_STATIC_DRAW)
            glVertexAttribPointer(BufferIndices.vertices, 3, GL_FLOAT, GL_FALSE, 0, None)
            glEnableVertexAttribArray(BufferIndices.vertices)
            vboIds[BufferIndices.vertices] = vboId

        if BufferIndices.normals in bufferIndices:
            vboId = glGenBuffers(1)
            glBindBuffer(GL_ARRAY_BUFFER, vboId)
            glBufferData(GL_ARRAY_BUFFER, 3 * 4 * maxVerticesCount, None, GL_STATIC_DRAW)
            glVertexAttribPointer(BufferIndices.normals, 3, GL_FLOAT, GL_FALSE, 0, None)
            glEnableVertexAttribArray(BufferIndices.normals)
            vboIds[BufferIndices.normals] = vboId

        if BufferIndices.texCoords in bufferIndices:
            vboId = glGenBuffers(1)
            glBindBuffer(GL_ARRAY_BUFFER, vboId)
            glBufferData(GL_ARRAY_BUFFER, 2 * 4 * maxVerticesCount, None, GL_STATIC_DRAW)
            glVertexAttribPointer(BufferIndices.texCoords, 2, GL_FLOAT, GL_FALSE, 0, None)
            glEnableVertexAttribArray(BufferIndices.texCoords)
            vboIds[BufferIndices.texCoords] = vboId

        if BufferIndices.faces in bufferIndices:
            vboId = glGenBuffers(1)
            glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, vboId)
            glBufferData(GL_ELEMENT_ARRAY_BUFFER, 3 * 4 * maxFacesCount, None, GL_STATIC_DRAW)
            vboIds[BufferIndices.faces] = vboId

        glBindBuffer(GL_ARRAY_BUFFER, 0)
        glBindVertexArray(0)

        return UpdatableVBO(vaoId, vboIds, 0, maxVerticesCount, maxFacesCount)
