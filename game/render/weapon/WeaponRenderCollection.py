from game.gl.RenderModel3d import RenderMesh, RenderModel3d
from game.gl.VBOBuilderFactory import VBOBuilderFactory
from game.model.Material import Material
from game.model.weapon.Launcher import Launcher
from game.model.weapon.Pistol import Pistol
from game.model.weapon.Rifle import Rifle
from game.render.weapon.WeaponModel3dFactory import WeaponModel3dFactory


class WeaponRenderCollection:

    def __init__(self, weaponModel3dFactory, vboBuilderFactory):
        self.weaponModel3dFactory = weaponModel3dFactory
        self.vboBuilderFactory = vboBuilderFactory
        self.models = {}

    def init(self):
        for vbo in self.models:
            vbo.release()

        self.models = {}
        # self.makePistol()
        self.makeRifle()
        # self.makeLauncher()

    def makePistol(self):
        model = self.weaponModel3dFactory.makePistol()
        self.models[Pistol] = self.makeRenderModel3d(model)

    def makeRifle(self):
        model = self.weaponModel3dFactory.makeRifle()
        self.models[Rifle] = self.makeRenderModel3d(model)

    def makeLauncher(self):
        model = self.weaponModel3dFactory.makeLauncher()
        self.models[Launcher] = self.makeRenderModel3d(model)

    def makeRenderModel3d(self, model):
        vboBuilder = self.vboBuilderFactory.makeModel3dVBOBuilder()
        vbos = vboBuilder.build(model)
        meshes = [RenderMesh(vbo, mesh.texture, Material.weapon) for mesh, vbo in vbos]

        return RenderModel3d(meshes)

    def getRenderModel3d(self, weaponType):
        return self.models[weaponType]


def makeWeaponRenderCollection(resolver):
    return WeaponRenderCollection(resolver.resolve(WeaponModel3dFactory), resolver.resolve(VBOBuilderFactory))
