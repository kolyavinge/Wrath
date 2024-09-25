import numpy
from OpenGL.GL import *

from game.lib.sys import warn


class ShaderProgram:

    def __init__(self, shaders):
        self.id = glCreateProgram()
        for shader in shaders:
            glAttachShader(self.id, shader.id)
        glLinkProgram(self.id)

    def use(self):
        glUseProgram(self.id)

    def unuse(self):
        glUseProgram(0)

    def setInt32(self, name, value):
        location = self.getUniformLocation(name)
        glUniform1i(location, numpy.int32(value))

    def setFloat32(self, name, value):
        location = self.getUniformLocation(name)
        glUniform1f(location, numpy.float32(value))

    def setVector3(self, name, value):
        location = self.getUniformLocation(name)
        glUniform3fv(location, 1, numpy.array([value.x, value.y, value.z], dtype=numpy.float32))

    def setMatrix3(self, name, value):
        location = self.getUniformLocation(name)
        glUniformMatrix3fv(location, 1, GL_FALSE, numpy.array(value.items, dtype=numpy.float32))

    def setTransformMatrix4(self, name, value):
        location = self.getUniformLocation(name)
        glUniformMatrix4fv(location, 1, GL_FALSE, numpy.array(value.items, dtype=numpy.float32))

    def getUniformLocation(self, name):
        location = glGetUniformLocation(self.id, name)
        if location == -1:
            warn(f"Shader program has no {name} uniform.")
        return location
