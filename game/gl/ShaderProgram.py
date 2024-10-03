import numpy
from OpenGL.GL import *


class ShaderProgram:

    def __init__(self, shaders):
        self.id = glCreateProgram()
        for shader in shaders:
            glAttachShader(self.id, shader.id)
        glLinkProgram(self.id)
        self.fillLocations()

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
        x = numpy.float32(value.x)
        y = numpy.float32(value.y)
        z = numpy.float32(value.z)
        glUniform3f(location, x, y, z)

    def setMatrix3(self, name, value):
        location = self.getUniformLocation(name)
        glUniformMatrix3fv(location, 1, GL_FALSE, numpy.array(value.items, dtype=numpy.float32))

    def setTransformMatrix4(self, name, value):
        location = self.getUniformLocation(name)
        glUniformMatrix4fv(location, 1, GL_FALSE, numpy.array(value.items, dtype=numpy.float32))

    def getUniformLocation(self, name):
        return self.locations[name]

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
