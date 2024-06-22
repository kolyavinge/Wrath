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
        bspTree = self.gameData.level.bspTree
        player.levelSegments = []
        levelSegment = self.traversal.findLevelSegmentOrNone(bspTree, player.currentBorder.bottom.downLeft)
        self.appendLevelSegment(player, levelSegment)
        levelSegment = self.traversal.findLevelSegmentOrNone(bspTree, player.currentBorder.bottom.downRight)
        self.appendLevelSegment(player, levelSegment)
        levelSegment = self.traversal.findLevelSegmentOrNone(bspTree, player.currentBorder.bottom.upLeft)
        self.appendLevelSegment(player, levelSegment)
        levelSegment = self.traversal.findLevelSegmentOrNone(bspTree, player.currentBorder.bottom.upRight)
        self.appendLevelSegment(player, levelSegment)

    def appendLevelSegment(self, player, levelSegment):
        assert levelSegment is not None
        if levelSegment not in player.levelSegments:
            player.levelSegments.append(levelSegment)


def makePlayerPositionUpdater(resolver):
    return PlayerPositionUpdater(resolver.resolve(GameData), resolver.resolve(BSPTreeTraversal))
