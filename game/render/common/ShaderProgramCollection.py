from game.render.common.CrossshairShaderProgram import CrossshairShaderProgram
from game.render.common.MainSceneComposeShaderProgram import *
from game.render.common.MainSceneLightComponentsShaderProgram import *
from game.render.common.MainSceneShadowVolumesShaderProgram import *
from game.render.common.MeshShaderProgram import MeshShaderProgram
from game.render.common.ShaderCollection import ShaderCollection
from game.render.common.ShineCircleShaderProgram import ShineCircleShaderProgram


class ShaderProgramCollection:

    def __init__(self, shaderCollection):
        self.shaderCollection = shaderCollection

    def init(self):
        self.mainSceneLightComponents = MainSceneLightComponentsShaderProgram(
            [self.shaderCollection.mainSceneLightComponentsVertex, self.shaderCollection.mainSceneLightComponentsFragment]
        )

        self.mainSceneShadowVolumes = MainSceneShadowVolumesShaderProgram(
            [
                self.shaderCollection.mainSceneShadowVolumesVertex,
                self.shaderCollection.mainSceneShadowVolumesGeometry,
                self.shaderCollection.mainSceneShadowVolumesFragment,
            ]
        )

        self.mainSceneCompose = MainSceneComposeShaderProgram(
            [self.shaderCollection.mainSceneComposeVertex, self.shaderCollection.mainSceneComposeFragment]
        )

        self.crosshair = CrossshairShaderProgram([self.shaderCollection.crosshairVertex, self.shaderCollection.crosshairFragment])

        self.mesh = MeshShaderProgram([self.shaderCollection.meshVertex, self.shaderCollection.meshFragment])

        self.shineCircle = ShineCircleShaderProgram([self.shaderCollection.shineCircleVertex, self.shaderCollection.shineCircleFragment])


def makeShaderProgramCollection(resolver):
    return ShaderProgramCollection(resolver.resolve(ShaderCollection))
