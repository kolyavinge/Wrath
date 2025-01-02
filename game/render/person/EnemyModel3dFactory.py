from game.gl.Model3dLoader import Model3dLoader
from game.render.common.Model3dDirectory import Model3dDirectory


class EnemyModel3dFactory:

    def __init__(self, model3dLoader, model3dDirectory):
        self.model3dLoader = model3dLoader
        self.model3dDirectory = model3dDirectory

    def makeEnemy(self):
        model = self.model3dLoader.load(self.model3dDirectory.getObjFileFromDirectory("enemy"))
        model.setScale(0.014)

        return model


def makeEnemyModel3dFactory(resolver):
    return EnemyModel3dFactory(resolver.resolve(Model3dLoader), resolver.resolve(Model3dDirectory))
