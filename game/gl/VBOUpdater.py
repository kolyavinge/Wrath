from OpenGL.GL import *

from game.gl.UpdatableVBO import UpdatableVBO


class VBOUpdater:

    def __init__(self):
        self.vbo = None

    def beginUpdate(self, vbo):
        self.newVerticesCount = 0
        self.newNormalsCount = 0
        self.newTexCoordsCount = 0
        self.newFacesCount = 0
        self.vbo = vbo

    def endUpdate(self):
        if self.newVerticesCount == 0:
            raise Exception("Vertices have not been updated.")
        if self.newNormalsCount == 0:
            raise Exception("Normals have not been updated.")
        if self.newTexCoordsCount == 0:
            raise Exception("Texture coords have not been updated.")
        if self.newFacesCount == 0:
            raise Exception("Faces have not been updated.")
        if self.newVerticesCount != self.newNormalsCount:
            raise Exception("Vertices and normals must be the same count.")
        if self.newVerticesCount != self.newTexCoordsCount:
            raise Exception("Vertices and texture coords must be the same count.")
        self.vbo.verticesCount += self.newVerticesCount
        self.vbo = None
        glBindBuffer(GL_ARRAY_BUFFER, 0)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0)

    def addVertex(self, vector):
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo.vboIds[0])
        mapBuffer = glMapBuffer(GL_ARRAY_BUFFER, GL_WRITE_ONLY)
        mapArray = (GLfloat * self.vbo.maxElementsCount).from_address(mapBuffer)
        mapArray[self.vbo.verticesLastIndex] = vector.x
        mapArray[self.vbo.verticesLastIndex + 1] = vector.y
        mapArray[self.vbo.verticesLastIndex + 2] = vector.z
        glUnmapBuffer(GL_ARRAY_BUFFER)
        self.vbo.verticesLastIndex += 3
        self.newVerticesCount += 1

    def addNormal(self, vector):
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo.vboIds[1])
        mapBuffer = glMapBuffer(GL_ARRAY_BUFFER, GL_WRITE_ONLY)
        mapArray = (GLfloat * self.vbo.maxElementsCount).from_address(mapBuffer)
        mapArray[self.vbo.normalsLastIndex] = vector.x
        mapArray[self.vbo.normalsLastIndex + 1] = vector.y
        mapArray[self.vbo.normalsLastIndex + 2] = vector.z
        glUnmapBuffer(GL_ARRAY_BUFFER)
        self.vbo.normalsLastIndex += 3
        self.newNormalsCount += 1

    def addTexCoord(self, x, y):
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo.vboIds[2])
        mapBuffer = glMapBuffer(GL_ARRAY_BUFFER, GL_WRITE_ONLY)
        mapArray = (GLfloat * self.vbo.maxElementsCount).from_address(mapBuffer)
        mapArray[self.vbo.texCoordsLastIndex] = x
        mapArray[self.vbo.texCoordsLastIndex + 1] = y
        glUnmapBuffer(GL_ARRAY_BUFFER)
        self.vbo.texCoordsLastIndex += 2
        self.newTexCoordsCount += 1

    def addFace(self, i1, i2, i3):
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.vbo.vboIds[3])
        mapBuffer = glMapBuffer(GL_ELEMENT_ARRAY_BUFFER, GL_WRITE_ONLY)
        mapArray = (GLuint * self.vbo.maxElementsCount).from_address(mapBuffer)
        mapArray[self.vbo.elementsCount] = self.vbo.verticesCount + i1
        mapArray[self.vbo.elementsCount + 1] = self.vbo.verticesCount + i2
        mapArray[self.vbo.elementsCount + 2] = self.vbo.verticesCount + i3
        glUnmapBuffer(GL_ELEMENT_ARRAY_BUFFER)
        self.vbo.elementsCount += 3
        self.newFacesCount += 1

    def buildUnfilled(self, maxElementsCount):
        vaoId = glGenVertexArrays(1)
        glBindVertexArray(vaoId)

        vboIds = glGenBuffers(4)

        glBindBuffer(GL_ARRAY_BUFFER, vboIds[0])
        glBufferData(GL_ARRAY_BUFFER, 3 * 4 * maxElementsCount, None, GL_STATIC_DRAW)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)

        glBindBuffer(GL_ARRAY_BUFFER, vboIds[1])
        glBufferData(GL_ARRAY_BUFFER, 3 * 4 * maxElementsCount, None, GL_STATIC_DRAW)
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 0, None)

        glBindBuffer(GL_ARRAY_BUFFER, vboIds[2])
        glBufferData(GL_ARRAY_BUFFER, 2 * 4 * maxElementsCount, None, GL_STATIC_DRAW)
        glVertexAttribPointer(2, 2, GL_FLOAT, GL_FALSE, 0, None)

        glEnableVertexAttribArray(0)
        glEnableVertexAttribArray(1)
        glEnableVertexAttribArray(2)

        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, vboIds[3])
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, 3 * 4 * maxElementsCount, None, GL_STATIC_DRAW)

        glBindBuffer(GL_ARRAY_BUFFER, 0)
        glBindVertexArray(0)

        return UpdatableVBO(vaoId, vboIds, 0, maxElementsCount)
