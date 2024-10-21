from game.gl.ShaderProgram import ShaderProgram


class MainSceneShadowVolumesShaderProgram(ShaderProgram):

    def __init__(self, shaders):
        super().__init__(shaders)

    def setProjectionMatrix(self, projectionMatrix):
        self.setTransformMatrix4("projectionMatrix", projectionMatrix)

    def setModelViewMatrix(self, modelViewMatrix):
        self.setTransformMatrix4("modelViewMatrix", modelViewMatrix)

    def setLight(self, lights, torch):
        lightIndex = 0
        for light in lights:
            self.setVector3(f"lightPositions[{lightIndex}]", light.position)
            lightIndex += 1
        if torch.isActive:
            self.setVector3(f"lightPositions[{lightIndex}]", torch.position)
            lightIndex += 1
        self.setInt32("lightsCount", lightIndex)
