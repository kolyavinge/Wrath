import numpy
from OpenGL.GL import *


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

        if isinstance(value, numpy.float32):
            glUniform1f(location, value)
        elif isinstance(value, numpy.ndarray) and len(value) == 3:
            glUniform3fv(location, 1, value)
        elif isinstance(value, numpy.ndarray) and len(value) == 16:
            glUniformMatrix4fv(location, 1, GL_FALSE, value)
        else:
            raise Exception()
