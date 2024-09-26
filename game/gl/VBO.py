from OpenGL.GL import *


class VBO:

    def __init__(self, vaoId, vboIds, elementsCount, format):
        self.vaoId = vaoId
        self.vboIds = vboIds
        self.elementsCount = elementsCount
        self.format = format

    def release(self):
        glBindBuffer(GL_ARRAY_BUFFER, 0)
        glBindVertexArray(0)
        glDeleteBuffers(len(self.vboIds), self.vboIds)
        glDeleteVertexArrays(1, self.vaoId)
