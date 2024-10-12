from game.gl.MeshLoader import MeshLoader
from game.lib.Environment import Environment
from game.lib.FileSystem import FileSystem


class WeaponMeshFactory:

    def __init__(self, fileSystem, meshLoader):
        self.fileSystem = fileSystem
        self.meshLoader = meshLoader

    def makePistol(self):
        return self.meshLoader.load("")

    def makeRifle(self):
        mesh = self.meshLoader.load(self.getObjFileFromDirectory("rifle"))
        mesh.flipYZ()
        mesh.mulAxes(1, -1, 1)
        mesh.mulAxes(0.05, 0.05, 0.05)
        mesh.centerBy("yz")

        return mesh

    def makeLauncher(self):
        return self.meshLoader.load("")

    def getObjFileFromDirectory(self, directoryName):
        path = f"{Environment.programRootPath}\\res\\3dmodels\\{directoryName}"
        objFiles = self.fileSystem.findFilesByExtension(path, ".obj")
        if len(objFiles) == 0:
            raise Exception(f"No obj file in {path}.")
        if len(objFiles) > 1:
            raise Exception(f"Many obj files in {path}.")

        return objFiles[0]


def makeWeaponMeshFactory(resolver):
    return WeaponMeshFactory(resolver.resolve(FileSystem), resolver.resolve(MeshLoader))
