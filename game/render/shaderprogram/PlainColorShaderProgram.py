from game.render.gl.ShaderProgram import ShaderProgram


class PlainColorShaderProgram(ShaderProgram):

    def __init__(self, shaders):
        super().__init__(shaders)

    def setModelMatrix(self, modelMatrix):
        self.uniformSetter.setTransformMatrix4("modelMatrix", modelMatrix)

    def setViewMatrix(self, viewMatrix):
        self.uniformSetter.setTransformMatrix4("viewMatrix", viewMatrix)

    def setProjectionMatrix(self, projectionMatrix):
        self.uniformSetter.setTransformMatrix4("projectionMatrix", projectionMatrix)

    def setColor(self, color):
        self.uniformSetter.setVector3("color", color)

    def setAlphaFactor(self, factor):
        self.uniformSetter.setFloat32("alphaFactor", factor)
