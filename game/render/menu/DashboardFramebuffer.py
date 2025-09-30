from OpenGL.GL import *

from game.gl.ext import GL_DEFAULT_FRAMEBUFFER_ID, glGetViewportSize


class DashboardFramebuffer:

    def __init__(self):
        self.texture = 0
        self.id = 0

    def init(self):
        glDeleteTextures(1, [self.texture])
        glDeleteFramebuffers(1, [self.id])

        viewportWidth, viewportHeight = glGetViewportSize()

        self.texture = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, self.texture)
        glTexStorage2D(GL_TEXTURE_2D, 1, GL_RGBA8, viewportWidth, viewportHeight)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

        self.id = glGenFramebuffers(1)
        glBindFramebuffer(GL_FRAMEBUFFER, self.id)
        glFramebufferTexture2D(GL_FRAMEBUFFER, GL_COLOR_ATTACHMENT0, GL_TEXTURE_2D, self.texture, 0)
        glDrawBuffers(1, [GL_COLOR_ATTACHMENT0])

        glBindTexture(GL_TEXTURE_2D, 0)
        glBindFramebuffer(GL_FRAMEBUFFER, GL_DEFAULT_FRAMEBUFFER_ID)
