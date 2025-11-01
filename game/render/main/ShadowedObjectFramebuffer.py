from OpenGL.GL import *

from game.gl.ext import GL_DEFAULT_FRAMEBUFFER_ID, gleGetViewportSize


class ShadowedObjectFramebuffer:

    def __init__(self):
        self.depthBuffer = 0
        self.ambientBuffer = 0
        self.diffuseSpecularTexture = 0
        self.stencilMaskTexture = 0
        self.id = 0

    def init(self):
        glDeleteRenderbuffers(2, [self.depthBuffer, self.ambientBuffer])
        glDeleteTextures(2, [self.diffuseSpecularTexture, self.stencilMaskTexture])
        glDeleteFramebuffers(1, [self.id])

        self.viewportWidth, self.viewportHeight = gleGetViewportSize()

        self.depthBuffer = glGenRenderbuffers(1)
        glBindRenderbuffer(GL_RENDERBUFFER, self.depthBuffer)
        glRenderbufferStorage(GL_RENDERBUFFER, GL_DEPTH24_STENCIL8, self.viewportWidth, self.viewportHeight)

        self.ambientBuffer = glGenRenderbuffers(1)
        glBindRenderbuffer(GL_RENDERBUFFER, self.ambientBuffer)
        glRenderbufferStorage(GL_RENDERBUFFER, GL_RGBA, self.viewportWidth, self.viewportHeight)

        self.diffuseSpecularTexture = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, self.diffuseSpecularTexture)
        glTexStorage2D(GL_TEXTURE_2D, 1, GL_RGBA8, self.viewportWidth, self.viewportHeight)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

        self.stencilMaskTexture = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, self.stencilMaskTexture)
        glTexStorage2D(GL_TEXTURE_2D, 1, GL_RGB8, self.viewportWidth, self.viewportHeight)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

        self.id = glGenFramebuffers(1)
        glBindFramebuffer(GL_FRAMEBUFFER, self.id)
        glFramebufferRenderbuffer(GL_FRAMEBUFFER, GL_DEPTH_STENCIL_ATTACHMENT, GL_RENDERBUFFER, self.depthBuffer)
        glFramebufferRenderbuffer(GL_FRAMEBUFFER, GL_COLOR_ATTACHMENT0, GL_RENDERBUFFER, self.ambientBuffer)
        glFramebufferTexture2D(GL_FRAMEBUFFER, GL_COLOR_ATTACHMENT1, GL_TEXTURE_2D, self.diffuseSpecularTexture, 0)
        glFramebufferTexture2D(GL_FRAMEBUFFER, GL_COLOR_ATTACHMENT2, GL_TEXTURE_2D, self.stencilMaskTexture, 0)
        glDrawBuffers(3, [GL_COLOR_ATTACHMENT0, GL_COLOR_ATTACHMENT1, GL_COLOR_ATTACHMENT2])

        if glCheckFramebufferStatus(GL_FRAMEBUFFER) != GL_FRAMEBUFFER_COMPLETE:
            raise Exception("ShadowedObjectFramebuffer create error.")

        glBindTexture(GL_TEXTURE_2D, 0)
        glBindFramebuffer(GL_FRAMEBUFFER, GL_DEFAULT_FRAMEBUFFER_ID)
