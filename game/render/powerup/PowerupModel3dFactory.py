from game.gl.Model3dLoader import Model3dLoader
from game.render.common.Model3dDirectory import Model3dDirectory


class PowerupModel3dFactory:

    def __init__(self, model3dLoader, model3dDirectory):
        self.model3dLoader = model3dLoader
        self.model3dDirectory = model3dDirectory

    def makeSmallHealth(self):
        model = self.model3dLoader.load(self.model3dDirectory.getObjFileFromDirectory("smallHealth"))
        model.setScale(0.1)

        return model

    def makeLargeHealth(self):
        model = self.model3dLoader.load(self.model3dDirectory.getObjFileFromDirectory("largeHealth"))
        model.setScale(0.08)

        return model

    def makeVest(self):
        model = self.model3dLoader.load(self.model3dDirectory.getObjFileFromDirectory("vest"))

        return model


def makePowerupModel3dFactory(resolver):
    return PowerupModel3dFactory(resolver.resolve(Model3dLoader), resolver.resolve(Model3dDirectory))
