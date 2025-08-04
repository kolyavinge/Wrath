import numpy
from OpenGL.GL import *

from game.lib.Math import Math
from game.lib.Random import Random


class RandomSamplingOffsetTextureBuilder:

    def makeOffsetTexture(self, textureSize, samplesU, samplesV):
        # makes 3d texture with sets of random samples
        # to blur an image by random sampling algorithm

        samples = samplesU * samplesV
        textureDataSize = textureSize * textureSize * samples * 2
        textureData = numpy.empty(textureDataSize, dtype=numpy.float32)

        for i in range(0, textureSize):
            for j in range(0, textureSize):
                for k in range(0, samples, 2):
                    x1 = k % samplesU
                    y1 = (samples - 1 - k) / samplesU
                    x2 = (k + 1) % samplesU
                    y2 = (samples - 1 - k - 1) / samplesU

                    # center on grid and jitter
                    x = (x1 + 0.5) + Random.getFloat(-0.5, 0.5)
                    y = (y1 + 0.5) + Random.getFloat(-0.5, 0.5)
                    z = (x2 + 0.5) + Random.getFloat(-0.5, 0.5)
                    w = (y2 + 0.5) + Random.getFloat(-0.5, 0.5)

                    # scale between 0 and 1
                    x /= samplesU
                    y /= samplesV
                    z /= samplesU
                    w /= samplesV

                    # warp to circle
                    cell = int(((k / 2) * textureSize * textureSize + j * textureSize + i) * 4)
                    textureData[cell + 0] = Math.sqrt(y) * Math.cos(Math.piDouble * x)
                    textureData[cell + 1] = Math.sqrt(y) * Math.sin(Math.piDouble * x)
                    textureData[cell + 2] = Math.sqrt(w) * Math.cos(Math.piDouble * z)
                    textureData[cell + 3] = Math.sqrt(w) * Math.sin(Math.piDouble * z)

        textureId = glGenTextures(1)
        glBindTexture(GL_TEXTURE_3D, textureId)
        glTexStorage3D(GL_TEXTURE_3D, 1, GL_RGBA32F, textureSize, textureSize, int(samples / 2))
        glTexSubImage3D(GL_TEXTURE_3D, 0, 0, 0, 0, textureSize, textureSize, int(samples / 2), GL_RGBA, GL_FLOAT, textureData)
        glTexParameteri(GL_TEXTURE_3D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_3D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

        return textureId
