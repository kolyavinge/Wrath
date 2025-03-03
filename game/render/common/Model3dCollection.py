from game.gl.model3d.AsyncModel3dLoader import AsyncModel3dLoader
from game.render.common.Model3dDirectory import Model3dDirectory


class Model3dCollection:

    def __init__(self, asyncModel3dLoader, model3dDirectory):
        self.asyncModel3dLoader = asyncModel3dLoader
        self.model3dDirectory = model3dDirectory

    def load(self):
        modelNames = [
            self.model3dDirectory.getModelFileFromDirectory("largeHealth"),
            self.model3dDirectory.getModelFileFromDirectory("launcher"),
            self.model3dDirectory.getModelFileFromDirectory("launcherBullet"),
            self.model3dDirectory.getModelFileFromDirectory("pistol"),
            self.model3dDirectory.getModelFileFromDirectory("plasma"),
            self.model3dDirectory.getModelFileFromDirectory("plasmaBullet"),
            self.model3dDirectory.getModelFileFromDirectory("railgun"),
            self.model3dDirectory.getModelFileFromDirectory("rifle"),
            self.model3dDirectory.getModelFileFromDirectory("smallHealth"),
            self.model3dDirectory.getModelFileFromDirectory("sniper"),
            self.model3dDirectory.getModelFileFromDirectory("vest"),
        ]
        self.models = self.asyncModel3dLoader.loadAsync(modelNames)

    def getModel(self, modelName):
        return self.models[modelName]


def makeModel3dCollection(resolver):
    return Model3dCollection(resolver.resolve(AsyncModel3dLoader), resolver.resolve(Model3dDirectory))
