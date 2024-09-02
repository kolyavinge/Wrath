from game.gl.ShaderProgram import ShaderProgram
from game.render.common.ShaderCollection import ShaderCollection


class ShaderProgramCollection:

    def __init__(self, shaderCollection):
        self.shaderCollection = shaderCollection

    def init(self):
        self.mainScene = ShaderProgram([self.shaderCollection.mainSceneVertex, self.shaderCollection.mainSceneFragment])


def makeShaderProgramCollection(resolver):
    return ShaderProgramCollection(resolver.resolve(ShaderCollection))
