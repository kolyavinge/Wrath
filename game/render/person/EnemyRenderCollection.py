from game.gl.RenderModel3dLoader import RenderModel3dLoader
from game.model.Material import Material
from game.render.person.EnemyModel3dFactory import EnemyModel3dFactory


class EnemyRenderCollection:

    def __init__(self, enemyModel3dFactory, renderModel3dLoader):
        self.enemyModel3dFactory = enemyModel3dFactory
        self.renderModel3dLoader = renderModel3dLoader
        self.enemyModel = None

    def init(self):
        if self.enemyModel is not None:
            self.enemyModel.release()

        self.makeEnemy()

    def makeEnemy(self):
        model = self.enemyModel3dFactory.makeEnemy()
        self.enemyModel = self.renderModel3dLoader.make(model, Material.person)


def makeEnemyRenderCollection(resolver):
    return EnemyRenderCollection(resolver.resolve(EnemyModel3dFactory), resolver.resolve(RenderModel3dLoader))
