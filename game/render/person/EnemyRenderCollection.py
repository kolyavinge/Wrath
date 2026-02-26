from game.anx.DebugSettings import DebugSettings
from game.gl.model3d.RenderModel3dLoader import RenderModel3dLoader
from game.model.Material import Material
from game.render.person.EnemyModel3dFactory import EnemyModel3dFactory


class EnemyRenderCollection:

    def __init__(
        self,
        enemyModel3dFactory: EnemyModel3dFactory,
        renderModel3dLoader: RenderModel3dLoader,
    ):
        self.enemyModel3dFactory = enemyModel3dFactory
        self.renderModel3dLoader = renderModel3dLoader
        self.enemyModel = None
        self.withAdjacency = True

    def isInitialized(self):
        return self.enemyModel is not None

    def init(self, forced=False):
        if not forced and not DebugSettings.allowBots:
            return

        if self.enemyModel is not None:
            self.enemyModel.release()

        self.makeEnemy()
        self.makeEnemyForShadow()

    def makeEnemy(self):
        model = self.enemyModel3dFactory.makeEnemy()
        self.enemyModel = self.renderModel3dLoader.make(model, Material.person)

    def makeEnemyForShadow(self):
        model = self.enemyModel3dFactory.makeEnemyForShadow()
        self.enemyModelForShadow = self.renderModel3dLoader.make(model, Material.person, self.withAdjacency)
