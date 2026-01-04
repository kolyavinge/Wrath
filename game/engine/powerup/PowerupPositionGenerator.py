from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal
from game.engine.GameState import GameState
from game.lib.Math import Math
from game.lib.Random import Random


class PowerupPositionGenerator:

    def __init__(
        self,
        gameState: GameState,
        traversal: BSPTreeTraversal,
    ):
        self.gameState = gameState
        self.traversal = traversal

    def getPosition(self):
        powerupArea = Random.getListItem(self.gameState.level.powerupAreas)
        position = powerupArea.getRandomPoint()
        levelSegment = self.traversal.findLevelSegmentOrNone(self.gameState.collisionTree, position)
        if len(levelSegment.floors) == 0:
            raise Exception(f"No floors in segment. Cannot generate powerup position: {position}. PowerupArea is {powerupArea}.")

        position.z = 0
        for floor in levelSegment.floors:
            position.z = Math.max(floor.getZ(position.x, position.y), position.z)

        return position
