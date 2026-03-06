from game.gl.ShaderProgram import ShaderProgram


class PlasmaRayShaderProgram(ShaderProgram):

    def __init__(self, shaders):
        super().__init__(shaders)

    def setResolution(self, width, height):
        self.uniformSetter.setVector2("resolution", width, height)

    def setInitTimeSec(self, initTimeSec):
        self.uniformSetter.setFloat32("initTimeSec", initTimeSec)

    def setCurrentTimeSec(self, currentTimeSec):
        self.uniformSetter.setFloat32("currentTimeSec", currentTimeSec)
