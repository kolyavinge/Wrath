from game.gl.ShaderProgram import ShaderProgram
from game.model.light.Spot import Spot


class MainSceneLightComponentsShaderProgram(ShaderProgram):

    def __init__(self, shaders):
        super().__init__(shaders)

    def setModelMatrix(self, modelMatrix):
        self.setTransformMatrix4("modelMatrix", modelMatrix)

    def setViewMatrix(self, viewMatrix):
        self.setTransformMatrix4("viewMatrix", viewMatrix)

    def setProjectionMatrix(self, projectionMatrix):
        self.setTransformMatrix4("projectionMatrix", projectionMatrix)

    def setMaxDepth(self, maxDepth):
        self.setFloat32("maxDepth", maxDepth)

    def setMaterial(self, material):
        self.setFloat32("material.ambient", material.ambient)
        self.setFloat32("material.diffuse", material.diffuse)
        self.setFloat32("material.specular", material.specular)
        self.setFloat32("material.shininess", material.shininess)

    def setLight(self, lights, torch):
        # lights
        lightIndex = 0
        spotIndex = 0
        for light in lights:
            if isinstance(light, Spot):
                self.setVector3(f"spots[{spotIndex}].color", light.color)
                self.setVector3(f"spots[{spotIndex}].position", light.lightPosition)
                self.setVector3(f"spots[{spotIndex}].direction", light.direction)
                self.setFloat32(f"spots[{spotIndex}].attenuation", light.attenuation)
                self.setFloat32(f"spots[{spotIndex}].cutoffCos", light.cutoffCos)
                spotIndex += 1
            else:
                self.setVector3(f"lights[{lightIndex}].color", light.color)
                self.setVector3(f"lights[{lightIndex}].position", light.lightPosition)
                lightIndex += 1
        # player torch
        if torch.isActive:
            self.setVector3(f"spots[{spotIndex}].color", torch.color)
            self.setVector3(f"spots[{spotIndex}].position", torch.position)
            self.setVector3(f"spots[{spotIndex}].direction", torch.direction)
            self.setFloat32(f"spots[{spotIndex}].attenuation", torch.attenuation)
            self.setFloat32(f"spots[{spotIndex}].cutoffCos", torch.cutoffCos)
            spotIndex += 1
        self.setInt32("lightsCount", lightIndex)
        self.setInt32("spotsCount", spotIndex)
