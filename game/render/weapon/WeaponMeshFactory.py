from game.gl.MeshLoader import MeshLoader


class WeaponMeshFactory:

    def __init__(self, meshLoader):
        self.meshLoader = meshLoader

    def makePistol(self):
        return self.meshLoader.load("")

    def makeRifle(self):
        return self.meshLoader.load("")

    def makeLauncher(self):
        return self.meshLoader.load("")


def makeWeaponMeshFactory(resolver):
    return WeaponMeshFactory(resolver.resolve(MeshLoader))
