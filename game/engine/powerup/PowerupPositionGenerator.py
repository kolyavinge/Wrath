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
        position = powerupArea.getRandomPoint()
        levelSegment = self.traversal.findLevelSegmentOrNone(self.gameData.collisionTree, position)
        if len(levelSegment.floors) == 0:
            raise Exception(f"No floors in segment. Cannot generate powerup position: {position}. PowerupArea is {powerupArea}.")

        position.z = 0
        for floor in levelSegment.floors:
            position.z = Math.max(floor.getZ(position.x, position.y), position.z)

        return position
