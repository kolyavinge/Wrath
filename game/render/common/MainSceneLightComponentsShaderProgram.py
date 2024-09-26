from game.gl.ShaderProgram import ShaderProgram
from game.model.light.Spot import Spot


class MainSceneLightComponentsShaderProgram(ShaderProgram):

    def __init__(self, shaders):
        super().__init__(shaders)

    def setModelViewMatrix(self, modelViewMatrix):
        self.setTransformMatrix4("modelViewMatrix", modelViewMatrix)

    def setModelViewProjectionMatrix(self, modelViewProjectionMatrix):
        self.setTransformMatrix4("modelViewProjectionMatrix", modelViewProjectionMatrix)

    def setNormalMatrix(self, normalMatrix):
        self.setMatrix3("normalMatrix", normalMatrix)

    def setMaxDepth(self, maxDepth):
        self.setFloat32("maxDepth", maxDepth)

    def setMaterial(self, material):
        self.setFloat32("material.ambient", material.ambient)
        self.setFloat32("material.diffuse", material.diffuse)
        self.setFloat32("material.specular", material.specular)
        self.setFloat32("material.shininess", material.shininess)

    def setLight(self, lights, player, torch):
        # lights
        lightIndex = 0
        spotIndex = 0
        for light in lights:
            if isinstance(light, Spot):
                self.setVector3(f"spot[{spotIndex}].color", light.color)
                self.setVector3(f"spot[{spotIndex}].position", light.position)
                self.setVector3(f"spot[{spotIndex}].direction", light.direction)
                self.setFloat32(f"spot[{spotIndex}].attenuation", light.attenuation)
                self.setFloat32(f"spot[{spotIndex}].cutoffCos", light.cutoffCos)
                spotIndex += 1
            else:
                self.setVector3(f"light[{lightIndex}].color", light.color)
                self.setVector3(f"light[{lightIndex}].position", light.position)
                lightIndex += 1
        # player torch
        if torch.isActive:
            self.setVector3(f"spot[{spotIndex}].color", torch.color)
            self.setVector3(f"spot[{spotIndex}].position", player.eyePosition)
            self.setVector3(f"spot[{spotIndex}].direction", player.lookDirection)
            self.setFloat32(f"spot[{spotIndex}].attenuation", torch.attenuation)
            self.setFloat32(f"spot[{spotIndex}].cutoffCos", torch.cutoffCos)
            spotIndex += 1
        self.setInt32("lightsCount", lightIndex)
        self.setInt32("spotsCount", spotIndex)
