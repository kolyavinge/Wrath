from game.gl.model3d.Model3dLoader import Model3dLoader
from game.render.common.Model3dDirectory import Model3dDirectory


class EnemyModel3dFactory:

    def __init__(
        self,
        model3dLoader: Model3dLoader,
        model3dDirectory: Model3dDirectory,
    ):
        self.model3dLoader = model3dLoader
        self.model3dDirectory = model3dDirectory

    def makeEnemy(self):
        model = self.model3dLoader.load(self.model3dDirectory.getModelFileFromDirectory("enemy", "model.glb"))

        return model

    def makeEnemyForShadow(self):
        model = self.model3dLoader.load(self.model3dDirectory.getModelFileFromDirectory("enemy", "modelForShadow.glb"))

        return model
