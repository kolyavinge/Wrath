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
            self.gameData.player.commitNextPosition()

    def updateLevelSegment(self):
        player = self.gameData.player
        playerFloor = self.gameData.level.floors[player.floorIndex]
        player.levelSegment = self.traversal.findLevelSegmentOrNone(playerFloor.bspTree, player.currentCenterPoint)
        assert player.levelSegment is not None


def makePlayerPositionUpdater(resolver):
    return PlayerPositionUpdater(resolver.resolve(GameData), resolver.resolve(BSPTreeTraversal))
