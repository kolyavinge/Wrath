from OpenGL.GL import *

from game.gl.VBO import VBO


class UpdatableVBO(VBO):

    def __init__(self, vaoId, vboIds, elementsCount, maxVerticesCount, maxFacesCount):
        super().__init__(vaoId, vboIds, elementsCount, GL_TRIANGLES)
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
        self.faceLastIndex = 0
