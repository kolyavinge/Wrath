from game.render.common.Model3dDirectory import Model3dDirectory
from game.render.lib.model3d.Model3dLoader import Model3dLoader


class BulletModel3dFactory:

    def __init__(
        self,
        model3dLoader: Model3dLoader,
        model3dDirectory: Model3dDirectory,
    ):
        self.model3dLoader = model3dLoader
        self.model3dDirectory = model3dDirectory

    def makeRifleGrenade(self):
        model = self.model3dLoader.load(self.model3dDirectory.getModelFileFromDirectory("rifleGrenade"))
        model.setScale(12)

        return model

    def makePlasmaBullet(self):
        model = self.model3dLoader.load(self.model3dDirectory.getModelFileFromDirectory("plasmaBullet"))
        model.setScale(0.05)

        return model

    def makeLauncherBullet(self):
        model = self.model3dLoader.load(self.model3dDirectory.getModelFileFromDirectory("launcherBullet"))
        model.setScale(0.1)

        return model
