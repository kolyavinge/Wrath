from game.gl.ShaderProgram import ShaderProgram


class MainSceneShadowVolumesShaderProgram(ShaderProgram):

    def __init__(self, shaders):
        super().__init__(shaders)

    def setModelMatrix(self, modelMatrix):
        self.setTransformMatrix4("modelMatrix", modelMatrix)

    def setViewMatrix(self, viewMatrix):
        self.setTransformMatrix4("viewMatrix", viewMatrix)

    def setProjectionMatrix(self, projectionMatrix):
        self.setTransformMatrix4("projectionMatrix", projectionMatrix)

    def hasAnimation(self, value):
        self.setInt32("hasAnimation", 1 if value else 0)

    def setBoneTransformMatrices(self, boneTransformMatrices):
        for index, matrix in enumerate(boneTransformMatrices):
            self.setTransformMatrix4(f"boneTransformMatrices[{index}]", matrix)

    def setLight(self, lights, torch):
        lightIndex = 0
        for light in lights:
            self.setVector3(f"lightPositions[{lightIndex}]", light.lightPosition)
            lightIndex += 1
        if torch.isActive:
            self.setVector3(f"lightPositions[{lightIndex}]", torch.position)
            lightIndex += 1
        self.setInt32("lightsCount", lightIndex)
