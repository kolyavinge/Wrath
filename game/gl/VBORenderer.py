from OpenGL.GL import *


class VBORenderer:

    def render(self, vbo):
        glBindVertexArray(vbo.vaoId)
        glDrawElements(vbo.format, vbo.elementsCount, GL_UNSIGNED_INT, None)
        glBindVertexArray(0)


def makeVBORenderer(resolve):
    return VBORenderer()
