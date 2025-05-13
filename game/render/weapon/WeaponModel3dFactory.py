from game.gl.model3d.Model3dLoader import Model3dLoader
from game.render.common.Model3dDirectory import Model3dDirectory


class WeaponModel3dFactory:

    def __init__(
        self,
        model3dLoader: Model3dLoader,
        model3dDirectory: Model3dDirectory,
    ):
        self.model3dLoader = model3dLoader
        self.model3dDirectory = model3dDirectory

    def makePistol(self):
        model = self.model3dLoader.load(self.model3dDirectory.getModelFileFromDirectory("pistol"))
        model.setScale(0.04)

        return model

    def makeRifle(self):
        model = self.model3dLoader.load(self.model3dDirectory.getModelFileFromDirectory("rifle"))
        model.setScale(0.035)

        return model

    def makePlasma(self):
        model = self.model3dLoader.load(self.model3dDirectory.getModelFileFromDirectory("plasma"))
        model.setScale(0.0025)

        return model

    def makeLauncher(self):
        model = self.model3dLoader.load(self.model3dDirectory.getModelFileFromDirectory("launcher"))
        model.setScale(0.5)

        return model

    def makeRailgun(self):
        model = self.model3dLoader.load(self.model3dDirectory.getModelFileFromDirectory("railgun"))
        model.setScale(0.7)

        return model

    def makeSniper(self):
        model = self.model3dLoader.load(self.model3dDirectory.getModelFileFromDirectory("sniper"))
        model.setScale(0.15)

        return model


def makeWeaponModel3dFactory(resolver):
    return WeaponModel3dFactory(
        resolver.resolve(Model3dLoader),
        resolver.resolve(Model3dDirectory),
    )
