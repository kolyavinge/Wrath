from OpenGL.GL import *

from game.lib.sys import convertListToLPLPChar
from game.render.gl.ShaderProgramUniformLocations import ShaderProgramUniformLocations
from game.render.gl.ShaderProgramUniformSetter import ShaderProgramUniformSetter


class ShaderProgram:

    def __init__(self, shaders):
        self.id = glCreateProgram()
        for shader in shaders:
            glAttachShader(self.id, shader.id)
        self.initBeforeLink()
        glLinkProgram(self.id)
        if glGetProgramiv(self.id, GL_LINK_STATUS) == GL_TRUE:
            self.uniformLocations = ShaderProgramUniformLocations(self.id)
            self.uniformSetter = ShaderProgramUniformSetter(self.uniformLocations)
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

    def setOutputNamesForTransformFeedback(self, outputNames):
        glTransformFeedbackVaryings(self.id, len(outputNames), convertListToLPLPChar(outputNames), GL_SEPARATE_ATTRIBS)
