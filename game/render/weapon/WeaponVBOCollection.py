from game.gl.TexturedVBO import TexturedVBO
from game.gl.VBOBuilderFactory import VBOBuilderFactory
from game.model.weapon.Launcher import Launcher
from game.model.weapon.Pistol import Pistol
from game.model.weapon.Rifle import Rifle
from game.render.weapon.WeaponMeshFactory import WeaponMeshFactory
from game.render.weapon.WeaponVBO import WeaponVBO


class WeaponVBOCollection:

    def __init__(self, weaponMeshFactory, vboBuilderFactory):
        self.weaponMeshFactory = weaponMeshFactory
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
        mesh = self.weaponMeshFactory.makePistol()
        self.vbos[Pistol] = self.makeWeaponVBO(mesh)

    def makeRifle(self):
        mesh = self.weaponMeshFactory.makeRifle()
        self.vbos[Rifle] = self.makeWeaponVBO(mesh)

    def makeLauncher(self):
        mesh = self.weaponMeshFactory.makeLauncher()
        self.vbos[Launcher] = self.makeWeaponVBO(mesh)

    def makeWeaponVBO(self, mesh):
        vboBuilder = self.vboBuilderFactory.makeMeshVBOBuilder()
        vbos = vboBuilder.build(mesh)
        texturedVBOs = [TexturedVBO(vbo, mesh.texture) for mesh, vbo in vbos]

        return WeaponVBO(texturedVBOs)

    def getWeaponVBO(self, weaponType):
        return self.vbos[weaponType]


def makeWeaponVBOCollection(resolver):
    return WeaponVBOCollection(resolver.resolve(WeaponMeshFactory), resolver.resolve(VBOBuilderFactory))
