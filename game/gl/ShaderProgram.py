import numpy
from OpenGL.GL import *

from game.lib.sys import warn


class ShaderProgram:

    def __init__(self, shaders):
        self.id = glCreateProgram()
        for shader in shaders:
            glAttachShader(self.id, shader.id)
        self.initBeforeLink()
        glLinkProgram(self.id)
        if glGetProgramiv(self.id, GL_LINK_STATUS) == GL_TRUE:
            self.fillLocations()
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
        location = self.getUniformLocationOrNone(name)
        if location is not None:
            glUniform1i(location, numpy.int32(value))

    def setFloat32(self, name, value):
        location = self.getUniformLocationOrNone(name)
        if location is not None:
            glUniform1f(location, numpy.float32(value))

    def setBoolean(self, name, value):
        self.setInt32(name, 1 if value else 0)

    def setVector2(self, name, x, y):
        location = self.getUniformLocationOrNone(name)
        if location is not None:
            x = numpy.float32(x)
            y = numpy.float32(y)
            glUniform2f(location, x, y)

    def setVector3(self, name, value):
        location = self.getUniformLocationOrNone(name)
        if location is not None:
            x = numpy.float32(value.x)
            y = numpy.float32(value.y)
            z = numpy.float32(value.z)
            glUniform3f(location, x, y, z)

    def setMatrix3(self, name, value):
        location = self.getUniformLocationOrNone(name)
        if location is not None:
            glUniformMatrix3fv(location, 1, GL_FALSE, numpy.array(value.items, dtype=numpy.float32))

    def setTransformMatrix4(self, name, value):
        location = self.getUniformLocationOrNone(name)
        if location is not None:
            glUniformMatrix4fv(location, 1, GL_FALSE, numpy.array(value.items, dtype=numpy.float32))

    def getUniformLocationOrNone(self, name):
        if name in self.locations:
            return self.locations[name]
        else:
            warn(f"Cannot find location {name} in shader program.")

    def fillLocations(self):
        self.locations = {}
        uniformsCount = glGetProgramiv(self.id, GL_ACTIVE_UNIFORMS)
        for uniform in range(0, uniformsCount):
            name, size, _ = glGetActiveUniform(self.id, uniform)
            location = glGetUniformLocation(self.id, name)
            name = name.decode("utf-8")
            self.locations[name] = location
            if size != 1:
                arrayName = name[0 : name.index("[")]
                for i in range(1, size):
                    arrayIndexName = f"{arrayName}[{i}]"
                    location = glGetUniformLocation(self.id, arrayIndexName)
                    self.locations[arrayIndexName] = location
