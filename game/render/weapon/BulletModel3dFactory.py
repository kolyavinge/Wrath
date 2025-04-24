from game.gl.model3d.Model3dLoader import Model3dLoader
from game.render.common.Model3dDirectory import Model3dDirectory


class BulletModel3dFactory:

    def __init__(self, model3dLoader, model3dDirectory):
        self.model3dLoader = model3dLoader
        self.model3dDirectory = model3dDirectory

    def makePlasmaBullet(self):
        model = self.model3dLoader.load(self.model3dDirectory.getModelFileFromDirectory("plasmaBullet"))
        model.setScale(0.05)

        return model

    def makeLauncherBullet(self):
        model = self.model3dLoader.load(self.model3dDirectory.getModelFileFromDirectory("launcherBullet"))
        model.setScale(0.1)

        return model


def makeBulletModel3dFactory(resolver):
    return BulletModel3dFactory(resolver.resolve(Model3dLoader), resolver.resolve(Model3dDirectory))
