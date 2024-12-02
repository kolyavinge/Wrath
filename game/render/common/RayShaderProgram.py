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

    def setMainAxis(self, mainAxis):
        self.setVector3("mainAxis", mainAxis)

    def setRayLength(self, rayLength):
        self.setFloat32("rayLength", rayLength)

    def setRayHeight(self, rayHeight):
        self.setFloat32("rayHeight", rayHeight)

    def setRayColor(self, rayColor):
        self.setVector3("rayColor", rayColor)

    def setRayBrightness(self, rayBrightness):
        self.setFloat32("rayBrightness", rayBrightness)

    def setShineStrength(self, shineStrength):
        self.setFloat32("shineStrength", shineStrength)
