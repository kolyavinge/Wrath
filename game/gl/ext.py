from OpenGL.GL import *


def glGetViewportSize():
    viewport = glGetIntegerv(GL_VIEWPORT)
    width = viewport[2]
    height = viewport[3]

    return (width, height)
