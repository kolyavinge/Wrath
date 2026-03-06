from game.gl.ShaderProgram import ShaderProgram
from game.model.light.Spot import Spot


class MainSceneLightComponentsShaderProgram(ShaderProgram):

    def __init__(self, shaders):
        super().__init__(shaders)

    def setModelMatrix(self, modelMatrix):
        self.uniformSetter.setTransformMatrix4("modelMatrix", modelMatrix)

    def setViewMatrix(self, viewMatrix):
        self.uniformSetter.setTransformMatrix4("viewMatrix", viewMatrix)

    def setProjectionMatrix(self, projectionMatrix):
        self.uniformSetter.setTransformMatrix4("projectionMatrix", projectionMatrix)

    def setMaxDepth(self, maxDepth):
        self.uniformSetter.setFloat32("maxDepth", maxDepth)

    def setAlphaFactor(self, factor):
        self.uniformSetter.setFloat32("alphaFactor", factor)

    def setMaterial(self, material):
        self.uniformSetter.setFloat32("material.ambient", material.ambient)
        self.uniformSetter.setFloat32("material.diffuse", material.diffuse)
        self.uniformSetter.setFloat32("material.specular", material.specular)
        self.uniformSetter.setFloat32("material.shininess", material.shininess)

    def hasAnimation(self, value):
        self.uniformSetter.setBoolean("hasAnimation", value)

    def setBoneTransformMatrices(self, boneTransformMatrices):
        for index, matrix in enumerate(boneTransformMatrices):
            self.uniformSetter.setTransformMatrix4(f"boneTransformMatrices[{index}]", matrix)

    def setLight(self, lights, torch):
        # lights
        lightIndex = 0
        spotIndex = 0
        for light in lights:
            if isinstance(light, Spot):
                self.uniformSetter.setVector3(f"spots[{spotIndex}].color", light.color)
                self.uniformSetter.setVector3(f"spots[{spotIndex}].position", light.lightPosition)
                self.uniformSetter.setVector3(f"spots[{spotIndex}].direction", light.direction)
                self.uniformSetter.setFloat32(f"spots[{spotIndex}].attenuation", light.attenuation)
                self.uniformSetter.setFloat32(f"spots[{spotIndex}].cutoffCos", light.cutoffCos)
                spotIndex += 1
            else:
                self.uniformSetter.setVector3(f"lights[{lightIndex}].color", light.color)
                self.uniformSetter.setVector3(f"lights[{lightIndex}].position", light.lightPosition)
                lightIndex += 1
        # player torch
        if torch.isActive:
            self.uniformSetter.setVector3(f"spots[{spotIndex}].color", torch.color)
            self.uniformSetter.setVector3(f"spots[{spotIndex}].position", torch.position)
            self.uniformSetter.setVector3(f"spots[{spotIndex}].direction", torch.direction)
            self.uniformSetter.setFloat32(f"spots[{spotIndex}].attenuation", torch.attenuation)
            self.uniformSetter.setFloat32(f"spots[{spotIndex}].cutoffCos", torch.cutoffCos)
            spotIndex += 1
        self.uniformSetter.setInt32("lightsCount", lightIndex)
        self.uniformSetter.setInt32("spotsCount", spotIndex)
