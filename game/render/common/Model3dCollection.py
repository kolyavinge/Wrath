from game.gl.AsyncModel3dLoader import AsyncModel3dLoader
from game.render.common.Model3dDirectory import Model3dDirectory


class Model3dCollection:

    def __init__(self, asyncModel3dLoader, model3dDirectory):
        self.asyncModel3dLoader = asyncModel3dLoader
        self.model3dDirectory = model3dDirectory

    def load(self):
        modelNames = [
            self.model3dDirectory.getObjFileFromDirectory("largeHealth"),
            self.model3dDirectory.getObjFileFromDirectory("launcher"),
            self.model3dDirectory.getObjFileFromDirectory("launcherBullet"),
            self.model3dDirectory.getObjFileFromDirectory("pistol"),
            self.model3dDirectory.getObjFileFromDirectory("plasma"),
            self.model3dDirectory.getObjFileFromDirectory("plasmaBullet"),
            self.model3dDirectory.getObjFileFromDirectory("railgun"),
            self.model3dDirectory.getObjFileFromDirectory("rifle"),
            self.model3dDirectory.getObjFileFromDirectory("smallHealth"),
            self.model3dDirectory.getObjFileFromDirectory("sniper"),
            self.model3dDirectory.getObjFileFromDirectory("vest"),
        ]
        self.models = self.asyncModel3dLoader.loadAsync(modelNames)

    def getModel(self, modelName):
        return self.models[modelName]


def makeModel3dCollection(resolver):
    return Model3dCollection(resolver.resolve(AsyncModel3dLoader), resolver.resolve(Model3dDirectory))
