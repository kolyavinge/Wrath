from game.model.Material import Material
from game.render.common.TextureCollection import TextureCollection


class MaterialTextureCollection:

    def __init__(self, textureCollection):
        self.textureCollection = textureCollection

    def init(self):
        self.materials = {}
        self.materials[Material.blank] = self.textureCollection.blank
        self.materials[Material.wallMetal1] = self.textureCollection.wallMetal1
        self.materials[Material.wallMetal2] = self.textureCollection.wallMetal2
        self.materials[Material.wallMetal3] = self.textureCollection.wallMetal3
        self.materials[Material.wallMetal4] = self.textureCollection.wallMetal4
        self.materials[Material.wallMetal5] = self.textureCollection.wallMetal5
        self.materials[Material.wallMetal6] = self.textureCollection.wallMetal6
        self.materials[Material.floorMetal1] = self.textureCollection.floorMetal1
        self.materials[Material.floorMetal2] = self.textureCollection.floorMetal2
        self.materials[Material.floorMetal3] = self.textureCollection.floorMetal3
        self.materials[Material.floorMetal4] = self.textureCollection.floorMetal4
        self.materials[Material.ceilingMetal1] = self.textureCollection.ceilingMetal1
        self.materials[Material.ceilingMetal2] = self.textureCollection.ceilingMetal2
        self.materials[Material.edgeMetal1] = self.textureCollection.edgeMetal1
        self.materials[Material.edgeMetal2] = self.textureCollection.edgeMetal2

    def getTextureForMaterial(self, material):
        return self.materials[material]


def makeMaterialTextureCollection(resolver):
    return MaterialTextureCollection(resolver.resolve(TextureCollection))
