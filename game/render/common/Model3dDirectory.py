from game.lib.Environment import Environment
from game.lib.FileSystem import FileSystem


class Model3dDirectory:

    def __init__(self, fileSystem):
        self.fileSystem = fileSystem

    def getObjFileFromDirectory(self, model3dDirectoryName):
        path = f"{Environment.programRootPath}\\res\\3dmodels\\{model3dDirectoryName}"
        objFiles = self.fileSystem.findFilesByExtension(path, ".obj")

        if len(objFiles) == 0:
            raise Exception(f"No obj file in {path}.")

        if len(objFiles) > 1:
            raise Exception(f"Many obj files in {path}.")

        return objFiles[0]


def makeModel3dDirectory(resolver):
    return Model3dDirectory(resolver.resolve(FileSystem))
