from game.model.weapon.Launcher import Launcher
from game.model.weapon.Pistol import Pistol
from game.model.weapon.Rifle import Rifle
from game.model.weapon.Sniper import Sniper
from game.render.weapon.WeaponFlashRenderMeshFactory import WeaponFlashRenderMeshFactory


class WeaponFlashRenderCollection:

    def __init__(self, renderMeshFactory: WeaponFlashRenderMeshFactory):
        self.renderMeshFactory = renderMeshFactory

    def init(self):
        self.meshes = {}
        self.meshes[Pistol] = self.renderMeshFactory.makePistolFlash()
        self.meshes[Rifle] = self.renderMeshFactory.makeRifleFlash()
        self.meshes[Launcher] = self.renderMeshFactory.makeRifleFlash()
        self.meshes[Sniper] = self.renderMeshFactory.makeSniperFlash()

    def getRenderMesh(self, weaponType):
        return self.meshes[weaponType]


def makeWeaponFlashRenderCollection(resolver):
    return WeaponFlashRenderCollection(resolver.resolve(WeaponFlashRenderMeshFactory))
