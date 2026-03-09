from OpenGL.GL import GL_TRIANGLES

from game.gl.vbo.VBO import VBO


class UpdatableVBO:

    def __init__(self, vaoId, vboIds, elementsCount, maxVerticesCount, maxFacesCount):
        self.vbo = VBO(vaoId, vboIds, elementsCount, GL_TRIANGLES)
        self.vaoId = vaoId
        self.vboIds = vboIds
        self.elementsCount = elementsCount
        self.format = GL_TRIANGLES
        self.maxVerticesCount = maxVerticesCount
        self.maxFacesCount = maxFacesCount
        self.maxElementsCount = 3 * maxFacesCount
        self.refill()

    def isFilled(self):
        return self.verticesCount == self.maxVerticesCount

    def refill(self):
        self.verticesCount = 0
        self.verticesLastIndex = 0
        self.normalsLastIndex = 0
        self.texCoordsLastIndex = 0
        self.colorsLastIndex = 0
        self.faceLastIndex = 0

    def reset(self):
        self.elementsCount = 0
        self.refill()

    def release(self):
        self.vbo.release()
