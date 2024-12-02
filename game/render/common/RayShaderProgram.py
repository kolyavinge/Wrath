from game.gl.ShaderProgram import ShaderProgram


class RayShaderProgram(ShaderProgram):

    def __init__(self, shaders):
        super().__init__(shaders)

    def setModelMatrix(self, modelMatrix):
        self.setTransformMatrix4("modelMatrix", modelMatrix)

    def setViewMatrix(self, viewMatrix):
        self.setTransformMatrix4("viewMatrix", viewMatrix)

    def setProjectionMatrix(self, projectionMatrix):
        self.setTransformMatrix4("projectionMatrix", projectionMatrix)

    def setOriginPosition(self, origin):
        self.setVector3("origin", origin)

    def setMainAxis(self, axis):
        self.setVector3("mainAxis", axis)

    def setRayHeight(self, height):
        self.setFloat32("rayHeight", height)

    def setRayColor(self, color):
        self.setVector3("rayColor", color)

    def setShineStrength(self, shineStrength):
        self.setFloat32("shineStrength", shineStrength)
