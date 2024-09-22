import numpy
from OpenGL.GL import *

from game.calc.Matrix3 import Matrix3
from game.calc.TranfsormMatrix4 import TransformMatrix4
from game.calc.Vector3 import Vector3
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

    def setUniform(self, name, value):
        location = glGetUniformLocation(self.id, name)
        if location == -1:
            warn(f"Shader program has no {name} uniform.")

        if isinstance(value, int):
            glUniform1i(location, numpy.int32(value))
        elif isinstance(value, float):
            glUniform1f(location, numpy.float32(value))
        elif isinstance(value, Vector3):
            glUniform3fv(location, 1, numpy.array([value.x, value.y, value.z], dtype=numpy.float32))
        elif isinstance(value, Matrix3):
            glUniformMatrix3fv(location, 1, GL_FALSE, numpy.array(value.items, dtype=numpy.float32))
        elif isinstance(value, TransformMatrix4):
            glUniformMatrix4fv(location, 1, GL_FALSE, numpy.array(value.items, dtype=numpy.float32))
        else:
            raise Exception()
