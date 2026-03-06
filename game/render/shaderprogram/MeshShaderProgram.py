from game.gl.ShaderProgram import ShaderProgram


class MeshShaderProgram(ShaderProgram):

    def __init__(self, shaders):
        super().__init__(shaders)

    def setModelMatrix(self, modelMatrix):
        self.uniformSetter.setTransformMatrix4("modelMatrix", modelMatrix)

    def setViewMatrix(self, viewMatrix):
        self.uniformSetter.setTransformMatrix4("viewMatrix", viewMatrix)

    def setProjectionMatrix(self, projectionMatrix):
        self.uniformSetter.setTransformMatrix4("projectionMatrix", projectionMatrix)

    def setColorFactor(self, factor):
        self.uniformSetter.setFloat32("colorFactor", factor)

    def setAlphaFactor(self, factor):
        self.uniformSetter.setFloat32("alphaFactor", factor)
