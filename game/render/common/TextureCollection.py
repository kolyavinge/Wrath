from game.gl.TextureLoader import TextureLoader
from game.lib.Environment import Environment


class TextureCollection:

    def __init__(self, textureLoader):
        self.textureLoader = textureLoader

    def init(self):
        path = Environment.programRootPath + "\\res\\textures\\"
        self.blank = self.textureLoader.load(path + "blank.png")


def makeTextureCollection(resolver):
    return TextureCollection(resolver.resolve(TextureLoader))
