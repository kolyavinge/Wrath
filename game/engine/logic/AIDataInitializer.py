from game.calc.Geometry import Geometry
from game.engine.GameData import GameData
from game.lib.Random import Random


class AIDataInitializer:

    def __init__(self, gameData):
        self.gameData = gameData

    def init(self):
        rand = Random()
        for enemy in self.gameData.enemies:
            self.initForEnemy(enemy.aiData, rand)

    def initForEnemy(self, aiData, rand):
        aiData.horizontalFieldViewRadians = Geometry.degreesToRadians(45.0 + rand.getFloat(0.0, 15.0))
        aiData.checkCollisionLength = 2.0 + rand.getFloat(0.0, 2.0)
        aiData.checkCollisionDirectionsCount = 4 + rand.getInt(0, 6)
        aiData.fireDistance = 10 + rand.getInt(0, 10)
        aiData.commit()


def makeAIDataInitializer(resolver):
    return AIDataInitializer(resolver.resolve(GameData))
