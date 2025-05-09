from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal
from game.engine.GameData import GameData
from game.lib.Math import Math
from game.lib.Random import Random


class PowerupPositionGenerator:

    def __init__(self, gameData, traversal):
        self.gameData = gameData
        self.traversal = traversal
        self.rand = Random()

    def getPosition(self):
        powerupAreas = self.gameData.level.powerupAreas
        powerupArea = powerupAreas[self.rand.getInt(0, len(powerupAreas) - 1)]

        if powerupArea.startPoint != powerupArea.endPoint:
            position = powerupArea.startPoint.getDirectionTo(powerupArea.endPoint)
            position.setLength(self.rand.getFloat(0, position.getLength()))
            position.add(powerupArea.startPoint)
        else:
            position = powerupArea.startPoint.copy()

        if powerupArea.radius != 0:
            radius = self.rand.getFloat(0, powerupArea.radius)
            radians = self.rand.getFloat(0, Math.piDouble)
            x = radius * Math.cos(radians)
            y = radius * Math.sin(radians)
            position.x += x
            position.y += y

        levelSegment = self.traversal.findLevelSegmentOrNone(self.gameData.collisionTree, position)
        if len(levelSegment.floors) != 1:
            raise Exception(f"Generated powerup position is out of segment floor: {position}.")
        floor = levelSegment.floors[0]
        position.z = floor.getZ(position.x, position.y)

        return position


def makePowerupPositionGenerator(resolver):
    return PowerupPositionGenerator(resolver.resolve(GameData), resolver.resolve(BSPTreeTraversal))
