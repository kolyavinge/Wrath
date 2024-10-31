from game.gl.ShaderProgram import ShaderProgram


class CrossshairShaderProgram(ShaderProgram):

    def __init__(self, shaders):
        super().__init__(shaders)

    def setResolution(self, width, height):
        self.setVector2("resolution", width, height)
