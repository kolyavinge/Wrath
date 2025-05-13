from game.engine.GameData import GameData
from game.gl.model3d.RenderModel3dLoader import RenderModel3dLoader
from game.model.Material import Material
from game.render.person.EnemyModel3dFactory import EnemyModel3dFactory


class EnemyRenderCollection:

    def __init__(
        self,
        gameData: GameData,
        enemyModel3dFactory: EnemyModel3dFactory,
        renderModel3dLoader: RenderModel3dLoader,
    ):
        self.gameData = gameData
        self.enemyModel3dFactory = enemyModel3dFactory
        self.renderModel3dLoader = renderModel3dLoader
        self.enemyModel = None

    def init(self):
        if self.gameData.noEnemies:
            return

        if self.enemyModel is not None:
            self.enemyModel.release()

        self.makeEnemy()

    def makeEnemy(self):
        model = self.enemyModel3dFactory.makeEnemy()
        self.enemyModel = self.renderModel3dLoader.make(model, Material.person)
