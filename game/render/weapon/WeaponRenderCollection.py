from game.anx.DebugSettings import DebugSettings
from game.gl.model3d.RenderModel3dLoader import RenderModel3dLoader
from game.model.Material import Material
from game.model.weapon.Launcher import Launcher
from game.model.weapon.NullWeapon import NullWeapon
from game.model.weapon.Pistol import Pistol
from game.model.weapon.Plasma import Plasma
from game.model.weapon.Railgun import Railgun
from game.model.weapon.Rifle import Rifle
from game.model.weapon.Sniper import Sniper
from game.render.weapon.WeaponModel3dFactory import WeaponModel3dFactory


class WeaponRenderCollection:

    def __init__(
        self,
        weaponModel3dFactory: WeaponModel3dFactory,
        renderModel3dLoader: RenderModel3dLoader,
    ):
        self.weaponModel3dFactory = weaponModel3dFactory
        self.renderModel3dLoader = renderModel3dLoader
        self.models = {}
        self.withAdjacency = False

    def init(self):
        for vbo in self.models:
            vbo.release()

        self.models = {}

        if not DebugSettings.isDebug:
            self.makePistol()
            self.makeRifle()
            self.makePlasma()
            self.makeLauncher()
            self.makeRailgun()
            self.makeSniper()
        else:
            self.debugLoading()

        self.makeNullWeapon()

    def makePistol(self):
        model = self.weaponModel3dFactory.makePistol()
        self.models[Pistol] = self.renderModel3dLoader.make(model, Material.weapon, self.withAdjacency)

    def makeRifle(self):
        model = self.weaponModel3dFactory.makeRifle()
        self.models[Rifle] = self.renderModel3dLoader.make(model, Material.weapon, self.withAdjacency)

    def makePlasma(self):
        model = self.weaponModel3dFactory.makePlasma()
        self.models[Plasma] = self.renderModel3dLoader.make(model, Material.weapon, self.withAdjacency)

    def makeLauncher(self):
        model = self.weaponModel3dFactory.makeLauncher()
        self.models[Launcher] = self.renderModel3dLoader.make(model, Material.weapon, self.withAdjacency)

    def makeRailgun(self):
        model = self.weaponModel3dFactory.makeRailgun()
        self.models[Railgun] = self.renderModel3dLoader.make(model, Material.weapon, self.withAdjacency)

    def makeSniper(self):
        model = self.weaponModel3dFactory.makeSniper()
        self.models[Sniper] = self.renderModel3dLoader.make(model, Material.weapon, self.withAdjacency)

    def makeNullWeapon(self):
        self.models[NullWeapon] = self.models[Pistol]

    def debugLoading(self):
        self.makePistol()
        self.models[Rifle] = self.models[Pistol]
        self.models[Plasma] = self.models[Pistol]
        self.models[Launcher] = self.models[Pistol]
        self.models[Railgun] = self.models[Pistol]
        self.models[Sniper] = self.models[Pistol]

    def getRenderModel3d(self, weaponType):
        return self.models[weaponType]
