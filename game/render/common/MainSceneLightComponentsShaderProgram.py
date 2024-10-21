from game.gl.ShaderProgram import ShaderProgram
from game.model.light.Spot import Spot


class MainSceneLightComponentsShaderProgram(ShaderProgram):

    def __init__(self, shaders):
        super().__init__(shaders)

    def setModelViewMatrix(self, modelViewMatrix):
        self.modelViewMatrix = modelViewMatrix
        self.setTransformMatrix4("modelViewMatrix", modelViewMatrix)

    def setModelViewProjectionMatrix(self, modelViewProjectionMatrix):
        self.setTransformMatrix4("modelViewProjectionMatrix", modelViewProjectionMatrix)

    def setNormalMatrix(self, normalMatrix):
        self.normalMatrix = normalMatrix
        self.setMatrix3("normalMatrix", normalMatrix)

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
                directionView = self.normalMatrix.mulVector3(light.direction)
                directionView.normalize()
                self.setVector3(f"spots[{spotIndex}].color", light.color)
                self.setVector3(f"spots[{spotIndex}].positionView", self.modelViewMatrix.mulVector3(light.position))
                self.setVector3(f"spots[{spotIndex}].directionView", directionView)
                self.setFloat32(f"spots[{spotIndex}].attenuation", light.attenuation)
                self.setFloat32(f"spots[{spotIndex}].cutoffCos", light.cutoffCos)
                spotIndex += 1
            else:
                self.setVector3(f"lights[{lightIndex}].color", light.color)
                self.setVector3(f"lights[{lightIndex}].positionView", self.modelViewMatrix.mulVector3(light.position))
                lightIndex += 1
        # player torch
        if torch.isActive:
            directionView = self.normalMatrix.mulVector3(torch.direction)
            directionView.normalize()
            self.setVector3(f"spots[{spotIndex}].color", torch.color)
            self.setVector3(f"spots[{spotIndex}].positionView", self.modelViewMatrix.mulVector3(torch.position))
            self.setVector3(f"spots[{spotIndex}].directionView", directionView)
            self.setFloat32(f"spots[{spotIndex}].attenuation", torch.attenuation)
            self.setFloat32(f"spots[{spotIndex}].cutoffCos", torch.cutoffCos)
            spotIndex += 1
        self.setInt32("lightsCount", lightIndex)
        self.setInt32("spotsCount", spotIndex)
