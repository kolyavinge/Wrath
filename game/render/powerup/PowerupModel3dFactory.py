from game.gl.model3d.Model3dLoader import Model3dLoader
from game.render.common.Model3dDirectory import Model3dDirectory


class PowerupModel3dFactory:

    def __init__(
        self,
        model3dLoader: Model3dLoader,
        model3dDirectory: Model3dDirectory,
    ):
        self.model3dLoader = model3dLoader
        self.model3dDirectory = model3dDirectory

    def makeSmallHealth(self):
        model = self.model3dLoader.load(self.model3dDirectory.getModelFileFromDirectory("smallHealth"))
        model.setScale(0.1)

        return model

    def makeLargeHealth(self):
        model = self.model3dLoader.load(self.model3dDirectory.getModelFileFromDirectory("largeHealth"))
        model.setScale(0.08)

        return model

    def makeVest(self):
        model = self.model3dLoader.load(self.model3dDirectory.getModelFileFromDirectory("vest"))

        return model
