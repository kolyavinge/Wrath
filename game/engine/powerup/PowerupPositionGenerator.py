from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal
from game.engine.GameData import GameData
from game.lib.Math import Math
from game.lib.Random import Random


class PowerupPositionGenerator:

    def __init__(
        self,
        gameData: GameData,
        traversal: BSPTreeTraversal,
    ):
        self.gameData = gameData
        self.traversal = traversal

    def getPosition(self):
        powerupArea = Random.getListItem(self.gameData.level.powerupAreas)

        if powerupArea.startPoint != powerupArea.endPoint:
            position = powerupArea.startPoint.getDirectionTo(powerupArea.endPoint)
            position.setLength(Random.getFloat(0, position.getLength()))
            position.add(powerupArea.startPoint)
        else:
            position = powerupArea.startPoint.copy()

        if powerupArea.radius != 0:
            radius = Random.getFloat(0, powerupArea.radius)
            radians = Random.getFloat(0, Math.piDouble)
            x = radius * Math.cos(radians)
            y = radius * Math.sin(radians)
            position.x += x
            position.y += y

        levelSegment = self.traversal.findLevelSegmentOrNone(self.gameData.collisionTree, position)
        if len(levelSegment.floors) == 0:
            raise Exception(f"No floors in segment. Cannot generate powerup position: {position}. PowerupArea is {powerupArea}.")

        position.z = 0
        for floor in levelSegment.floors:
            position.z = Math.max(floor.getZ(position.x, position.y), position.z)

        return position
