from OpenGL.GL import *
from PIL import Image

from game.gl.Texture import Texture
from game.lib.Numeric import Numeric
from game.lib.sys import warn


class TextureLoader:

    def load(self, fullFilePath):
        with Image.open(fullFilePath) as image:
            image = image.transpose(Image.FLIP_TOP_BOTTOM)
            if not Numeric.isPowerOf2(image.width) or not Numeric.isPowerOf2(image.height):
                warn(f"Texture size '{fullFilePath}' isn't power of two.")
            imageData = image.convert("RGBA").tobytes()
            textureId = glGenTextures(1)
            glBindTexture(GL_TEXTURE_2D, textureId)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
            glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image.width, image.height, 0, GL_RGBA, GL_UNSIGNED_BYTE, imageData)
            glBindTexture(GL_TEXTURE_2D, 0)

        return Texture(textureId, image.width, image.height)
