from game.lib.Environment import Environment
from game.lib.FileSystem import FileSystem


class Model3dDirectory:

    def __init__(self, fileSystem):
        self.fileSystem = fileSystem
        self.extensions = [".obj", ".fbx"]

    def getModelFileFromDirectory(self, model3dDirectoryName):
        path = f"{Environment.programRootPath}\\res\\3dmodels\\{model3dDirectoryName}"

        for ext in self.extensions:
            modelFiles = self.fileSystem.findFilesByExtension(path, ext)
            if len(modelFiles) > 1:
                raise Exception(f"Many model files in {path}.")
            if len(modelFiles) == 1:
                return modelFiles[0]

        raise Exception(f"No model files in {path}.")


def makeModel3dDirectory(resolver):
    return Model3dDirectory(resolver.resolve(FileSystem))
