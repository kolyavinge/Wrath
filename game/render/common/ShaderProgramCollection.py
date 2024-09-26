from game.render.common.MainSceneComposeShaderProgram import *
from game.render.common.MainSceneLightComponentsShaderProgram import *
from game.render.common.MainSceneShaderProgram import *
from game.render.common.MainSceneShadowVolumesShaderProgram import *
from game.render.common.ShaderCollection import ShaderCollection


class ShaderProgramCollection:

    def __init__(self, shaderCollection):
        self.shaderCollection = shaderCollection

    def init(self):
        self.mainScene = MainSceneShaderProgram([self.shaderCollection.mainSceneVertex, self.shaderCollection.mainSceneFragment])

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


def makeShaderProgramCollection(resolver):
    return ShaderProgramCollection(resolver.resolve(ShaderCollection))
