from game.calc.Geometry import Geometry
from game.engine.GameData import GameData
from game.lib.Random import Random


class AIDataInitializer:

    def __init__(self, gameData: GameData):
        self.gameData = gameData

    def init(self):
        for enemy in self.gameData.enemies:
            self.initForEnemy(enemy.aiData)

    def initForEnemy(self, aiData):
        aiData.horizontalFieldViewRadians = Geometry.degreesToRadians(45.0 + Random.getFloat(0.0, 15.0))
        aiData.checkCollisionLength = 2.0 + Random.getFloat(0.0, 2.0)
        aiData.checkCollisionDirectionsCount = 4 + Random.getInt(0, 6)
        aiData.fireDistance = 10 + Random.getInt(0, 10)
        aiData.criticalHealth = Random.getInt(10, 50)
        aiData.patrollingTimeLimit = Random.getInt(500, 2000)
        aiData.commit()
