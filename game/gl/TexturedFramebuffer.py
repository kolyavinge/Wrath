from OpenGL.GL import *

from game.gl.ext import GL_DEFAULT_FRAMEBUFFER_ID


class TexturedFramebuffer:

    def __init__(self, addDepthComponent=False):
        self.depthBuffer = 0
        self.texture = 0
        self.id = 0
        self.addDepthComponent = addDepthComponent
        self.textureWidth = 0
        self.textureHeight = 0

    def init(self, textureWidth, textureHeight):
        self.textureWidth = textureWidth
        self.textureHeight = textureHeight

        if self.addDepthComponent:
            glDeleteRenderbuffers(1, [self.depthBuffer])
        glDeleteTextures(1, [self.texture])
        glDeleteFramebuffers(1, [self.id])

        if self.addDepthComponent:
            self.depthBuffer = glGenRenderbuffers(1)
            glBindRenderbuffer(GL_RENDERBUFFER, self.depthBuffer)
            glRenderbufferStorage(GL_RENDERBUFFER, GL_DEPTH_COMPONENT, textureWidth, textureHeight)

        self.texture = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, self.texture)
        glTexStorage2D(GL_TEXTURE_2D, 1, GL_RGBA8, textureWidth, textureHeight)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

        self.id = glGenFramebuffers(1)
        glBindFramebuffer(GL_FRAMEBUFFER, self.id)
        if self.addDepthComponent:
            glFramebufferRenderbuffer(GL_FRAMEBUFFER, GL_DEPTH_ATTACHMENT, GL_RENDERBUFFER, self.depthBuffer)
        glFramebufferTexture2D(GL_FRAMEBUFFER, GL_COLOR_ATTACHMENT0, GL_TEXTURE_2D, self.texture, 0)
        glDrawBuffers(1, [GL_COLOR_ATTACHMENT0])

        if glCheckFramebufferStatus(GL_FRAMEBUFFER) != GL_FRAMEBUFFER_COMPLETE:
            raise Exception("TexturedFramebuffer create error.")

        glBindTexture(GL_TEXTURE_2D, 0)
        glBindFramebuffer(GL_FRAMEBUFFER, GL_DEFAULT_FRAMEBUFFER_ID)
