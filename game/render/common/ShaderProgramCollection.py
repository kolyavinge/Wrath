from game.render.common.MainSceneShaderProgram import MainSceneShaderProgram
from game.render.common.ShaderCollection import ShaderCollection


class ShaderProgramCollection:

    def __init__(self, shaderCollection):
        self.shaderCollection = shaderCollection

    def init(self):
        self.mainScene = MainSceneShaderProgram([self.shaderCollection.mainSceneVertex, self.shaderCollection.mainSceneFragment])
        self.mainSceneLightComponents = None
        self.mainSceneShadowVolumes = None
        self.mainSceneShadowCompose = None


def makeShaderProgramCollection(resolver):
    return ShaderProgramCollection(resolver.resolve(ShaderCollection))
