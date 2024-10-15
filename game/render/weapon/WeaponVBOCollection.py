from game.gl.TexturedVBO import TexturedVBO
from game.gl.VBOBuilderFactory import VBOBuilderFactory
from game.model.weapon.Launcher import Launcher
from game.model.weapon.Pistol import Pistol
from game.model.weapon.Rifle import Rifle
from game.render.weapon.WeaponModel3dFactory import WeaponModel3dFactory
from game.render.weapon.WeaponVBO import WeaponVBO


class WeaponVBOCollection:

    def __init__(self, weaponModel3dFactory, vboBuilderFactory):
        self.weaponModel3dFactory = weaponModel3dFactory
        self.vboBuilderFactory = vboBuilderFactory
        self.vbos = {}

    def init(self):
        for vbo in self.vbos:
            vbo.release()

        self.vbos = {}
        # self.makePistol()
        self.makeRifle()
        # self.makeLauncher()

    def makePistol(self):
        mesh = self.weaponModel3dFactory.makePistol()
        self.vbos[Pistol] = self.makeWeaponVBO(mesh)

    def makeRifle(self):
        mesh = self.weaponModel3dFactory.makeRifle()
        self.vbos[Rifle] = self.makeWeaponVBO(mesh)

    def makeLauncher(self):
        mesh = self.weaponModel3dFactory.makeLauncher()
        self.vbos[Launcher] = self.makeWeaponVBO(mesh)

    def makeWeaponVBO(self, mesh):
        vboBuilder = self.vboBuilderFactory.makeModel3dVBOBuilder()
        vbos = vboBuilder.build(mesh)
        texturedVBOs = [TexturedVBO(vbo, mesh.texture) for mesh, vbo in vbos]

        return WeaponVBO(texturedVBOs)

    def getWeaponVBO(self, weaponType):
        return self.vbos[weaponType]


def makeWeaponVBOCollection(resolver):
    return WeaponVBOCollection(resolver.resolve(WeaponModel3dFactory), resolver.resolve(VBOBuilderFactory))
