from OpenGL.GL import *

GL_DEFAULT_FRAMEBUFFER_ID = 0


def gleGetViewportSize():
    viewport = glGetIntegerv(GL_VIEWPORT)
    width = viewport[2]
    height = viewport[3]

    return (width, height)
