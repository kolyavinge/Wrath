from game.render.lib.ShaderProgram import ShaderProgram


class VignetteShaderProgram(ShaderProgram):

    def __init__(self, shaders):
        super().__init__(shaders)

    def setResolution(self, width, height):
        self.uniformSetter.setVector2("resolution", width, height)

    def setRadius(self, radius):
        self.uniformSetter.setFloat32("radius", radius)

    def setAlphaFactor(self, factor):
        self.uniformSetter.setFloat32("alphaFactor", factor)
