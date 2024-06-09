from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal
from game.engine.GameData import GameData


class PlayerPositionUpdater:

    def __init__(self, gameData, traversal):
        self.gameData = gameData
        self.traversal = traversal

    def update(self):
        if self.gameData.player.hasMoved:
            self.updateLevelSegment()
            self.gameData.player.hasMoved = False

    def updateLevelSegment(self):
        playerFloor = self.gameData.level.floors[self.gameData.player.floorIndex]
        self.gameData.playerLevelSegment = self.traversal.findLevelSegmentOrNone(playerFloor.bspTree, self.gameData.player.centerPoint)
        assert self.gameData.playerLevelSegment is not None


def makePlayerPositionUpdater(resolver):
    return PlayerPositionUpdater(resolver.resolve(GameData), resolver.resolve(BSPTreeTraversal))
