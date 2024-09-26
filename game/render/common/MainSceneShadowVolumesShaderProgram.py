from game.gl.ShaderProgram import ShaderProgram


class MainSceneShadowVolumesShaderProgram(ShaderProgram):

    def __init__(self, shaders):
        super().__init__(shaders)

    def setLight(self, lights, player, torch):
        lightIndex = 0
        for light in lights:
            self.setVector3(f"lightPosition[{lightIndex}]", light.position)
            lightIndex += 1
        if torch.isActive:
            self.setVector3(f"lightPosition[{lightIndex}]", player.eyePosition)
            lightIndex += 1
        self.setInt32("lightsCount", lightIndex)
