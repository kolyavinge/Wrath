from game.render.lib.ShaderProgram import ShaderProgram


class MainSceneShadowVolumesShaderProgram(ShaderProgram):

    def __init__(self, shaders):
        super().__init__(shaders)

    def setModelMatrix(self, modelMatrix):
        self.uniformSetter.setTransformMatrix4("modelMatrix", modelMatrix)

    def setViewMatrix(self, viewMatrix):
        self.uniformSetter.setTransformMatrix4("viewMatrix", viewMatrix)

    def setProjectionMatrix(self, projectionMatrix):
        self.uniformSetter.setTransformMatrix4("projectionMatrix", projectionMatrix)

    def hasAnimation(self, value):
        self.uniformSetter.setBoolean("hasAnimation", value)

    def setBoneTransformMatrices(self, boneTransformMatrices):
        for index, matrix in enumerate(boneTransformMatrices):
            self.uniformSetter.setTransformMatrix4(f"boneTransformMatrices[{index}]", matrix)

    def setLight(self, lights, torch):
        lightIndex = 0
        for light in lights:
            self.uniformSetter.setVector3(f"lightPositions[{lightIndex}]", light.lightPosition)
            lightIndex += 1
        if torch.isActive:
            self.uniformSetter.setVector3(f"lightPositions[{lightIndex}]", torch.position)
            lightIndex += 1
        self.uniformSetter.setInt32("lightsCount", lightIndex)
