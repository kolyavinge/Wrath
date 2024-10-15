from game.gl.Model3dLoader import Model3dLoader
from game.lib.Environment import Environment
from game.lib.FileSystem import FileSystem


class WeaponModel3dFactory:

    def __init__(self, fileSystem, model3dLoader):
        self.fileSystem = fileSystem
        self.model3dLoader = model3dLoader

    def makePistol(self):
        return self.model3dLoader.load("")

    def makeRifle(self):
        model = self.model3dLoader.load(self.getObjFileFromDirectory("rifle"))
        model.setScale(0.025)

        return model

    def makeLauncher(self):
        return self.model3dLoader.load("")

    def getObjFileFromDirectory(self, directoryName):
        path = f"{Environment.programRootPath}\\res\\3dmodels\\{directoryName}"
        objFiles = self.fileSystem.findFilesByExtension(path, ".obj")
        if len(objFiles) == 0:
            raise Exception(f"No obj file in {path}.")
        if len(objFiles) > 1:
            raise Exception(f"Many obj files in {path}.")

        return objFiles[0]


def makeWeaponModel3dFactory(resolver):
    return WeaponModel3dFactory(resolver.resolve(FileSystem), resolver.resolve(Model3dLoader))
