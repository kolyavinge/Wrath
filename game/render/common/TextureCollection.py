from game.gl.TextureLoader import TextureLoader
from game.lib.Environment import Environment


class TextureCollection:

    def __init__(self, textureLoader):
        self.textureLoader = textureLoader

    def init(self):
        path = Environment.programRootPath + "\\res\\textures\\"
        self.blank = self.textureLoader.load(path + "blank.png")
        self.wallMetal1 = self.textureLoader.load(path + "wallMetal1.jpg")
        self.floorMetal1 = self.textureLoader.load(path + "floorMetal1.jpg")


def makeTextureCollection(resolver):
    return TextureCollection(resolver.resolve(TextureLoader))
