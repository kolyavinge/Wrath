from game.model.weapon.Rifle import Rifle
from game.render.weapon.WeaponFlashRenderMeshFactory import WeaponFlashRenderMeshFactory


class WeaponFlashRenderCollection:

    def __init__(self, renderMeshFactory):
        self.renderMeshFactory = renderMeshFactory

    def init(self):
        self.meshes = {}
        self.meshes[Rifle] = self.renderMeshFactory.makeRifleFlash()

    def getRenderMesh(self, weaponType):
        return self.meshes[weaponType]


def makeWeaponFlashRenderCollection(resolver):
    return WeaponFlashRenderCollection(resolver.resolve(WeaponFlashRenderMeshFactory))
