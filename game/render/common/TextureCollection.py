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
        self.wallMetal4 = self.textureLoader.load(path + "wallMetal4.jpg")
        self.wallMetal5 = self.textureLoader.load(path + "wallMetal5.jpg")
        self.wallMetal6 = self.textureLoader.load(path + "wallMetal6.jpg")
        self.wallMetal7 = self.textureLoader.load(path + "wallMetal7.jpg")
        self.wallMetal8 = self.textureLoader.load(path + "wallMetal8.jpg")
        self.wallMetal9 = self.textureLoader.load(path + "wallMetal9.jpg")
        self.floorMetal1 = self.textureLoader.load(path + "floorMetal1.jpg")
        self.floorMetal2 = self.textureLoader.load(path + "floorMetal2.jpg")
        self.floorMetal3 = self.textureLoader.load(path + "floorMetal3.jpg")
        self.floorMetal4 = self.textureLoader.load(path + "floorMetal4.jpg")
        self.floorMetal5 = self.textureLoader.load(path + "floorMetal5.jpg")
        self.ceilingMetal1 = self.textureLoader.load(path + "ceilingMetal1.jpg")
        self.ceilingMetal2 = self.textureLoader.load(path + "ceilingMetal2.jpg")
        self.ceilingMetal3 = self.textureLoader.load(path + "ceilingMetal3.jpg")
        self.edgeMetal1 = self.textureLoader.load(path + "edgeMetal1.jpg")
        self.edgeMetal2 = self.textureLoader.load(path + "edgeMetal2.jpg")
        self.edgeMetal3 = self.textureLoader.load(path + "edgeMetal3.jpg")
        self.bulletHole = self.textureLoader.load(path + "bulletHole.png")
        self.blackHole = self.textureLoader.load(path + "blackHole.png")
        self.explosionHole = self.textureLoader.load(path + "explosionHole.png")
        self.pistolFlash = self.textureLoader.load(path + "pistolFlash.png")
        self.rifleFlash = self.textureLoader.load(path + "rifleFlash.png")
        self.sniperFlash = self.textureLoader.load(path + "sniperFlash.png")
        self.sniperCrosshair = self.textureLoader.load(path + "sniperCrosshair.png")
        self.background1 = self.textureLoader.load(path + "background1.jpg")


def makeTextureCollection(resolver):
    return TextureCollection(resolver.resolve(TextureLoader))
