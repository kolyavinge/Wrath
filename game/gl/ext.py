from OpenGL.GL import *

GL_DEFAULT_FRAMEBUFFER_ID = 0


def gleGetViewportSize():
    viewport = glGetIntegerv(GL_VIEWPORT)
    width = viewport[2]
    height = viewport[3]

    return (width, height)


def gleBlitFramebuffer(fromId, toId, width, height, mask, filter):
    glBindFramebuffer(GL_READ_FRAMEBUFFER, fromId)
    glBindFramebuffer(GL_DRAW_FRAMEBUFFER, toId)
    glBlitFramebuffer(0, 0, width, height, 0, 0, width, height, mask, filter)
