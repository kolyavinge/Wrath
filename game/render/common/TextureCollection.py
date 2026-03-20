from game.lib.Environment import Environment
from game.render.gl.TextureLoader import TextureLoader


class TextureCollection:

    def __init__(self, textureLoader: TextureLoader):
        self.textureLoader = textureLoader

    def init(self):
        self.initTextures()
        self.initMenu()

    def initTextures(self):
        texturesFolder = f"{Environment.programRootPath}\\res\\textures\\"

        def load(imageFileName):
            return self.textureLoader.load(f"{texturesFolder}{imageFileName}")

        self.blank = load("blank.png")
        self.construction1 = load("construction1.jpg")
        self.construction2 = load("construction2.jpg")
        self.construction3 = load("construction3.jpg")
        self.construction4 = load("construction4.jpg")
        self.construction5 = load("construction5.jpg")
        self.construction6 = load("construction6.jpg")
        self.construction7 = load("construction7.jpg")
        self.construction8 = load("construction8.jpg")
        self.construction9 = load("construction9.jpg")
        self.construction10 = load("construction10.jpg")
        self.construction11 = load("construction11.jpg")
        self.construction12 = load("construction12.jpg")
        self.construction13 = load("construction13.jpg")
        self.construction14 = load("construction14.jpg")
        self.construction15 = load("construction15.jpg")
        self.construction16 = load("construction16.jpg")
        self.construction17 = load("construction17.jpg")
        self.rock1 = load("rock1.jpg")
        self.edgeMetal1 = load("edgeMetal1.jpg")
        self.edgeMetal2 = load("edgeMetal2.jpg")
        self.edgeMetal3 = load("edgeMetal3.jpg")
        self.bulletHole = load("bulletHole.png")
        self.blackHole = load("blackHole.png")
        self.explosionHole = load("explosionHole.png")
        self.pistolFlash = load("pistolFlash.png")
        self.rifleFlash = load("rifleFlash.png")
        self.sniperFlash = load("sniperFlash.png")
        self.sniperCrosshair = load("sniperCrosshair.png")
        self.bloodStain1 = load("bloodStain1.png")
        self.launcherExplosion = load("launcherExplosion.png")
        self.background1 = load("background1.jpg")
        # self.background1 = load("sphereTest.png")

    def initMenu(self):
        menuFolder = f"{Environment.programRootPath}\\res\\menu\\"

        def load(imageFileName):
            return self.textureLoader.load(f"{menuFolder}{imageFileName}")

        self.alphabet = load("alphabet.png")
        self.sprites = load("sprites.png")
