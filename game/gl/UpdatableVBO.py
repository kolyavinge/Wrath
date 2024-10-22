from OpenGL.GL import *

from game.gl.VBO import VBO


class UpdatableVBO(VBO):

    def __init__(self, vaoId, vboIds, elementsCount, maxElementsCount):
        super().__init__(vaoId, vboIds, elementsCount, GL_TRIANGLES)
        self.maxElementsCount = maxElementsCount
        self.verticesCount = 0
        self.verticesLastIndex = 0
        self.normalsLastIndex = 0
        self.texCoordsLastIndex = 0
