from game.gl.ShaderProgram import ShaderProgram


class PlainColorShaderProgram(ShaderProgram):

    def __init__(self, shaders):
        super().__init__(shaders)

    def setModelMatrix(self, modelMatrix):
        self.setTransformMatrix4("modelMatrix", modelMatrix)

    def setViewMatrix(self, viewMatrix):
        self.setTransformMatrix4("viewMatrix", viewMatrix)

    def setProjectionMatrix(self, projectionMatrix):
        self.setTransformMatrix4("projectionMatrix", projectionMatrix)

    def setColor(self, color):
        self.setVector3("color", color)

    def setAlphaFactor(self, factor):
        self.setFloat32("alphaFactor", factor)
