from game.calc.Vector3 import Vector3
from game.engine.GameData import GameData
from game.lib.Random import Random


class PowerUpPositionGenerator:

    def __init__(self, gameData):
        self.gameData = gameData
        self.rand = Random()

    def getPosition(self, height):
        floors = self.gameData.level.floors
        floor = floors[self.rand.getInt(0, len(floors))]

        downLeft = floor.downLeft
        upLeft = floor.upLeft
        downRight = floor.downRight

        x = self.rand.getFloat(downLeft.x, downRight.x)
        y = self.rand.getFloat(downLeft.y, upLeft.y)
        z = floor.getZ(x, y) + height

        return Vector3(x, y, z)


def makePowerUpPositionGenerator(resolver):
    return PowerUpPositionGenerator(resolver.resolve(GameData))
