from OpenGL.GL import *

from game.gl.ext import *


class ShadowedObjectFramebuffer:

    def __init__(self):
        self.depthBuffer = 0
        self.ambientBuffer = 0
        self.diffuseSpecularTexture = 0
        self.colorDepthFBO = 0

    def init(self):
        glDeleteRenderbuffers(2, [self.depthBuffer, self.ambientBuffer])
        glDeleteTextures(1, [self.diffuseSpecularTexture])
        glDeleteFramebuffers(1, [self.colorDepthFBO])
        self.viewportWidth, self.viewportHeight = glGetViewportSize()
        self.depthBuffer = glGenRenderbuffers(1)
        glBindRenderbuffer(GL_RENDERBUFFER, self.depthBuffer)
        glRenderbufferStorage(GL_RENDERBUFFER, GL_DEPTH_COMPONENT, self.viewportWidth, self.viewportHeight)
        self.ambientBuffer = glGenRenderbuffers(1)
        glBindRenderbuffer(GL_RENDERBUFFER, self.ambientBuffer)
        glRenderbufferStorage(GL_RENDERBUFFER, GL_RGBA, self.viewportWidth, self.viewportHeight)
        self.diffuseSpecularTexture = glGenTextures(1)
        glActiveTexture(GL_TEXTURE0)
        glBindTexture(GL_TEXTURE_2D, self.diffuseSpecularTexture)
        glTexStorage2D(GL_TEXTURE_2D, 1, GL_RGBA8, self.viewportWidth, self.viewportHeight)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        self.colorDepthFBO = glGenFramebuffers(1)
        glBindFramebuffer(GL_FRAMEBUFFER, self.colorDepthFBO)
        glFramebufferRenderbuffer(GL_FRAMEBUFFER, GL_DEPTH_ATTACHMENT, GL_RENDERBUFFER, self.depthBuffer)
        glFramebufferRenderbuffer(GL_FRAMEBUFFER, GL_COLOR_ATTACHMENT0, GL_RENDERBUFFER, self.ambientBuffer)
        glFramebufferTexture2D(GL_FRAMEBUFFER, GL_COLOR_ATTACHMENT1, GL_TEXTURE_2D, self.diffuseSpecularTexture, 0)
        glDrawBuffers(2, [GL_COLOR_ATTACHMENT0, GL_COLOR_ATTACHMENT1])
        glBindFramebuffer(GL_FRAMEBUFFER, 0)
        glBindTexture(GL_TEXTURE_2D, 0)
