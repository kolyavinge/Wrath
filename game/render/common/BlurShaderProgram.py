from game.gl.ShaderProgram import ShaderProgram


class BlurShaderProgram(ShaderProgram):

    def __init__(self, shaders):
        super().__init__(shaders)

    def setResolution(self, width, height):
        self.setVector2("resolution", width, height)

    def setOffsetsCount(self, offsetsCount):
        self.setInt32("offsetsCount", offsetsCount)
