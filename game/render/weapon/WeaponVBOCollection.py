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
        vbo = self.makeVBOFromMesh(mesh)
        self.vbos[Pistol] = WeaponVBO(vbo, mesh.mainTexture)

    def makeRifle(self):
        mesh = self.weaponMeshFactory.makeRifle()
        vbo = self.makeVBOFromMesh(mesh)
        self.vbos[Rifle] = WeaponVBO(vbo, mesh.mainTexture)

    def makeLauncher(self):
        mesh = self.weaponMeshFactory.makeLauncher()
        vbo = self.makeVBOFromMesh(mesh)
        self.vbos[Launcher] = WeaponVBO(vbo, mesh.mainTexture)

    def makeVBOFromMesh(self, mesh):
        vboBuilder = self.vboBuilderFactory.makeExtVBOBuilder()
        vboBuilder.addMesh(mesh)

        return vboBuilder.build()

    def getWeaponVBO(self, weaponType):
        return self.vbos[weaponType]


def makeWeaponVBOCollection(resolver):
    return WeaponVBOCollection(resolver.resolve(WeaponMeshFactory), resolver.resolve(VBOBuilderFactory))
