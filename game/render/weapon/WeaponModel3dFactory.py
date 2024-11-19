from game.gl.Model3dLoader import Model3dLoader
from game.render.common.Model3dDirectory import Model3dDirectory


class WeaponModel3dFactory:

    def __init__(self, model3dLoader, model3dDirectory):
        self.model3dLoader = model3dLoader
        self.model3dDirectory = model3dDirectory

    def makePistol(self):
        model = self.model3dLoader.load(self.model3dDirectory.getObjFileFromDirectory("pistol"))
        model.setScale(0.025)

        return model

    def makeRifle(self):
        model = self.model3dLoader.load(self.model3dDirectory.getObjFileFromDirectory("rifle"))
        model.setScale(0.025)

        return model

    def makeLauncher(self):
        model = self.model3dLoader.load(self.model3dDirectory.getObjFileFromDirectory("launcher"))
        model.setScale(0.12)

        return model

    def makeRailgun(self):
        model = self.model3dLoader.load(self.model3dDirectory.getObjFileFromDirectory("railgun"))
        model.setScale(0.5)

        return model


def makeWeaponModel3dFactory(resolver):
    return WeaponModel3dFactory(resolver.resolve(Model3dLoader), resolver.resolve(Model3dDirectory))
