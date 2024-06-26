from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal
from game.engine.GameData import GameData


class PlayerLevelSegmentsUpdater:

    def __init__(self, gameData, traversal):
        self.gameData = gameData
        self.traversal = traversal

    def update(self):
        player = self.gameData.player
        if player.hasMoved:
            bspTree = self.gameData.level.bspTree
            player.levelSegments = []
            border = player.nextBorder
            levelSegment = self.traversal.findLevelSegmentOrNone(bspTree, border.bottom.downLeft)
            self.appendLevelSegment(player, levelSegment)
            levelSegment = self.traversal.findLevelSegmentOrNone(bspTree, border.bottom.downRight)
            self.appendLevelSegment(player, levelSegment)
            levelSegment = self.traversal.findLevelSegmentOrNone(bspTree, border.bottom.upLeft)
            self.appendLevelSegment(player, levelSegment)
            levelSegment = self.traversal.findLevelSegmentOrNone(bspTree, border.bottom.upRight)
            self.appendLevelSegment(player, levelSegment)

    def appendLevelSegment(self, player, levelSegment):
        if levelSegment is not None:
            if levelSegment not in player.levelSegments:
                player.levelSegments.append(levelSegment)


def makePlayerLevelSegmentsUpdater(resolver):
    return PlayerLevelSegmentsUpdater(resolver.resolve(GameData), resolver.resolve(BSPTreeTraversal))
