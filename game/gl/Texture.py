from OpenGL.GL import *


class Texture:

    def __init__(self, id, width, height):
        if id is None or id <= 0:
            raise Exception("Invalid texture id.")

        self.id = id
        self.width = width
        self.height = height

    def bind(self, textureIndex):
        glActiveTexture(textureIndex)
        glBindTexture(GL_TEXTURE_2D, self.id)

    def unbind(self):
        glBindTexture(GL_TEXTURE_2D, 0)

    def release(self):
        glDeleteTextures(1, self.id)
