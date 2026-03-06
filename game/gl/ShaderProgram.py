import numpy
from OpenGL.GL import *

from game.gl.ShaderProgramUniformLocations import ShaderProgramUniformLocations
from game.lib.sys import convertListToLPLPChar


class ShaderProgram:

    def __init__(self, shaders):
        self.id = glCreateProgram()
        for shader in shaders:
            glAttachShader(self.id, shader.id)
        self.initBeforeLink()
        glLinkProgram(self.id)
        if glGetProgramiv(self.id, GL_LINK_STATUS) == GL_TRUE:
            self.uniformLocations = ShaderProgramUniformLocations(self.id)
        else:
            log = glGetProgramInfoLog(self.id)
            if len(log) > 0:
                raise Exception(log)

    def initBeforeLink(self):
        pass

    def use(self):
        glUseProgram(self.id)

    def unuse(self):
        glUseProgram(0)

    def setInt32(self, name, value):
        location = self.uniformLocations.getLocationOrNone(name)
        if location is not None:
            glUniform1i(location, numpy.int32(value))

    def setFloat32(self, name, value):
        location = self.uniformLocations.getLocationOrNone(name)
        if location is not None:
            glUniform1f(location, numpy.float32(value))

    def setBoolean(self, name, value):
        self.setInt32(name, 1 if value else 0)

    def setVector2(self, name, x, y):
        location = self.uniformLocations.getLocationOrNone(name)
        if location is not None:
            x = numpy.float32(x)
            y = numpy.float32(y)
            glUniform2f(location, x, y)

    def setVector3(self, name, value):
        location = self.uniformLocations.getLocationOrNone(name)
        if location is not None:
            x = numpy.float32(value.x)
            y = numpy.float32(value.y)
            z = numpy.float32(value.z)
            glUniform3f(location, x, y, z)

    def setMatrix3(self, name, value):
        location = self.uniformLocations.getLocationOrNone(name)
        if location is not None:
            glUniformMatrix3fv(location, 1, GL_FALSE, numpy.array(value.items, dtype=numpy.float32))

    def setTransformMatrix4(self, name, value):
        location = self.uniformLocations.getLocationOrNone(name)
        if location is not None:
            glUniformMatrix4fv(location, 1, GL_FALSE, numpy.array(value.items, dtype=numpy.float32))

    def setOutputNamesForTransformFeedback(self, outputNames):
        glTransformFeedbackVaryings(self.id, len(outputNames), convertListToLPLPChar(outputNames), GL_SEPARATE_ATTRIBS)
