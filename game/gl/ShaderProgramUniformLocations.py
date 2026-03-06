from OpenGL.GL import (
    GL_ACTIVE_UNIFORMS,
    glGetActiveUniform,
    glGetProgramiv,
    glGetUniformLocation,
)

from game.lib.sys import warn


class ShaderProgramUniformLocations:

    def __init__(self, shaderProgramId):
        self.fillLocations(shaderProgramId)

    def fillLocations(self, shaderProgramId):
        self.locations = {}
        uniformsCount = glGetProgramiv(shaderProgramId, GL_ACTIVE_UNIFORMS)
        for uniform in range(0, uniformsCount):
            name, size, _ = glGetActiveUniform(shaderProgramId, uniform)
            location = glGetUniformLocation(shaderProgramId, name)
            name = name.decode("utf-8")
            self.locations[name] = location
            if size != 1:
                arrayName = name[0 : name.index("[")]
                for i in range(1, size):
                    arrayIndexName = f"{arrayName}[{i}]"
                    location = glGetUniformLocation(shaderProgramId, arrayIndexName)
                    self.locations[arrayIndexName] = location

    def getLocationOrNone(self, uniformName):
        if uniformName in self.locations:
            return self.locations[uniformName]
        else:
            warn(f"Cannot find location {uniformName} in shader program.")
