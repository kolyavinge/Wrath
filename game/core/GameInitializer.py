from game.render.common.ShaderCollection import ShaderCollection
from game.render.common.ShaderProgramCollection import ShaderProgramCollection
from game.render.common.TextureCollection import TextureCollection


class GameInitializer:

    def __init__(self, textureCollection, shaderCollection, shaderProgramCollection):
        self.textureCollection = textureCollection
        self.shaderCollection = shaderCollection
        self.shaderProgramCollection = shaderProgramCollection

    def init(self):
        self.textureCollection.init()
        self.shaderCollection.init()
        self.shaderProgramCollection.init()


def makeGameInitializer(resolver):
    return GameInitializer(resolver.resolve(TextureCollection), resolver.resolve(ShaderCollection), resolver.resolve(ShaderProgramCollection))
