from game.render.gl.ShaderProgram import ShaderProgram


class MainSceneComposeShaderProgram(ShaderProgram):

    def __init__(self, shaders):
        super().__init__(shaders)

    def setResolution(self, width, height):
        self.uniformSetter.setVector2("resolution", width, height)
