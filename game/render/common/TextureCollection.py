from game.gl.TextureLoader import TextureLoader
from game.lib.Environment import Environment


class TextureCollection:

    def __init__(self, textureLoader: TextureLoader):
        self.textureLoader = textureLoader

    def init(self):
        path = Environment.programRootPath + "\\res\\textures\\"
        self.blank = self.textureLoader.load(path + "blank.png")
        self.construction1 = self.textureLoader.load(path + "construction1.jpg")
        self.construction2 = self.textureLoader.load(path + "construction2.jpg")
        self.construction3 = self.textureLoader.load(path + "construction3.jpg")
        self.construction4 = self.textureLoader.load(path + "construction4.jpg")
        self.construction5 = self.textureLoader.load(path + "construction5.jpg")
        self.construction6 = self.textureLoader.load(path + "construction6.jpg")
        self.construction7 = self.textureLoader.load(path + "construction7.jpg")
        self.construction8 = self.textureLoader.load(path + "construction8.jpg")
        self.construction9 = self.textureLoader.load(path + "construction9.jpg")
        self.construction10 = self.textureLoader.load(path + "construction10.jpg")
        self.construction11 = self.textureLoader.load(path + "construction11.jpg")
        self.construction12 = self.textureLoader.load(path + "construction12.jpg")
        self.construction13 = self.textureLoader.load(path + "construction13.jpg")
        self.construction14 = self.textureLoader.load(path + "construction14.jpg")
        self.construction15 = self.textureLoader.load(path + "construction15.jpg")
        self.construction16 = self.textureLoader.load(path + "construction16.jpg")
        self.construction17 = self.textureLoader.load(path + "construction17.jpg")
        self.rock1 = self.textureLoader.load(path + "rock1.jpg")
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
