from game.gl.TextureLoader import TextureLoader
from game.lib.Environment import Environment


class TextureCollection:

    def __init__(self, textureLoader):
        self.textureLoader = textureLoader

    def init(self):
        path = Environment.programRootPath + "\\res\\textures\\"
        self.blank = self.textureLoader.load(path + "blank.png")
        self.wallMetal1 = self.textureLoader.load(path + "wallMetal1.jpg")
        self.wallMetal2 = self.textureLoader.load(path + "wallMetal2.jpg")
        self.wallMetal3 = self.textureLoader.load(path + "wallMetal3.jpg")
        self.floorMetal1 = self.textureLoader.load(path + "floorMetal1.jpg")
        self.floorMetal2 = self.textureLoader.load(path + "floorMetal2.jpg")
        self.ceilingMetal1 = self.textureLoader.load(path + "ceilingMetal1.jpg")
        self.edgeMetal1 = self.textureLoader.load(path + "edgeMetal1.jpg")


def makeTextureCollection(resolver):
    return TextureCollection(resolver.resolve(TextureLoader))
