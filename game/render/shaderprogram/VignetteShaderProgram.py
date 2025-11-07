from game.gl.ShaderProgram import ShaderProgram


class VignetteShaderProgram(ShaderProgram):

    def __init__(self, shaders):
        super().__init__(shaders)

    def setResolution(self, width, height):
        self.setVector2("resolution", width, height)

    def setRadius(self, radius):
        self.setFloat32("radius", radius)

    def setAlphaFactor(self, factor):
        self.setFloat32("alphaFactor", factor)
