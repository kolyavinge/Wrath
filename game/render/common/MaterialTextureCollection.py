from game.model.Material import Material
from game.render.common.TextureCollection import TextureCollection


class MaterialTextureCollection:

    def __init__(self, textureCollection):
        self.textureCollection = textureCollection

    def init(self):
        self.materials = {}
        self.materials[Material.blank] = self.textureCollection.blank
        self.materials[Material.wallMetal1] = self.textureCollection.wallMetal1
        self.materials[Material.floorMetal1] = self.textureCollection.floorMetal1
        self.materials[Material.ceilingMetal1] = self.textureCollection.ceilingMetal1

    def getTextureForMaterial(self, material):
        return self.materials[material]


def makeMaterialTextureCollection(resolver):
    return MaterialTextureCollection(resolver.resolve(TextureCollection))
