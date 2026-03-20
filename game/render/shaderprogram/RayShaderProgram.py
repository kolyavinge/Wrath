from game.render.lib.ShaderProgram import ShaderProgram


class RayShaderProgram(ShaderProgram):

    def __init__(self, shaders):
        super().__init__(shaders)

    def setModelMatrix(self, modelMatrix):
        self.uniformSetter.setTransformMatrix4("modelMatrix", modelMatrix)

    def setViewMatrix(self, viewMatrix):
        self.uniformSetter.setTransformMatrix4("viewMatrix", viewMatrix)

    def setProjectionMatrix(self, projectionMatrix):
        self.uniformSetter.setTransformMatrix4("projectionMatrix", projectionMatrix)

    def setOriginPositions(self, origins):
        index = 0
        for origin in origins:
            self.uniformSetter.setVector3(f"origins[{index}]", origin)
            index += 1

    def setMainAxes(self, mainAxes):
        index = 0
        for mainAxis in mainAxes:
            self.uniformSetter.setVector3(f"mainAxes[{index}]", mainAxis)
            index += 1

    def setRayLengths(self, rayLengths):
        index = 0
        for rayLength in rayLengths:
            self.uniformSetter.setFloat32(f"rayLengths[{index}]", rayLength)
            index += 1

    def setRayHeight(self, rayHeight):
        self.uniformSetter.setFloat32("rayHeight", rayHeight)

    def setRayColor(self, rayColor):
        self.uniformSetter.setVector3("rayColor", rayColor)

    def setRayBrightnesses(self, rayBrightnesses):
        index = 0
        for rayBrightness in rayBrightnesses:
            self.uniformSetter.setFloat32(f"rayBrightnesses[{index}]", rayBrightness)
            index += 1

    def setShineStrength(self, shineStrength):
        self.uniformSetter.setFloat32("shineStrength", shineStrength)
