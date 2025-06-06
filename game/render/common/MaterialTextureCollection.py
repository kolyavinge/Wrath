from game.model.Material import Material
from game.render.common.TextureCollection import TextureCollection


class MaterialTextureCollection:

    def __init__(self, textureCollection: TextureCollection):
        self.textureCollection = textureCollection

    def init(self):
        self.materials = {}
        self.materials[Material.blank] = self.textureCollection.blank
        self.materials[Material.construction1] = self.textureCollection.construction1
        self.materials[Material.construction2] = self.textureCollection.construction2
        self.materials[Material.construction3] = self.textureCollection.construction3
        self.materials[Material.construction4] = self.textureCollection.construction4
        self.materials[Material.construction5] = self.textureCollection.construction5
        self.materials[Material.construction6] = self.textureCollection.construction6
        self.materials[Material.construction7] = self.textureCollection.construction7
        self.materials[Material.construction8] = self.textureCollection.construction8
        self.materials[Material.construction9] = self.textureCollection.construction9
        self.materials[Material.construction10] = self.textureCollection.construction10
        self.materials[Material.construction11] = self.textureCollection.construction11
        self.materials[Material.construction12] = self.textureCollection.construction12
        self.materials[Material.construction13] = self.textureCollection.construction13
        self.materials[Material.construction14] = self.textureCollection.construction14
        self.materials[Material.construction15] = self.textureCollection.construction15
        self.materials[Material.construction16] = self.textureCollection.construction16
        self.materials[Material.construction17] = self.textureCollection.construction17
        self.materials[Material.rock1] = self.textureCollection.rock1
        self.materials[Material.edgeMetal1] = self.textureCollection.edgeMetal1
        self.materials[Material.edgeMetal2] = self.textureCollection.edgeMetal2
        self.materials[Material.edgeMetal3] = self.textureCollection.edgeMetal3
        self.materials[Material.bulletHole] = self.textureCollection.bulletHole
        self.materials[Material.blackHole] = self.textureCollection.blackHole
        self.materials[Material.explosionHole] = self.textureCollection.explosionHole

    def getTextureForMaterial(self, material):
        return self.materials[material]
