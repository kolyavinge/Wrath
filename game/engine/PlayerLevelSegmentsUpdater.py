from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal
from game.engine.GameData import GameData


class PlayerLevelSegmentsUpdater:

    def __init__(self, gameData, traversal):
        self.gameData = gameData
        self.traversal = traversal

    def update(self):
        player = self.gameData.player
        if player.hasMoved:
            player.collisionLevelSegments = set()
            player.visibilityLevelSegments = set()
            self.updateLevelSegments(self.gameData.level.collisionTree, player.collisionLevelSegments)
            self.updateLevelSegments(self.gameData.level.visibilityTree, player.visibilityLevelSegments)

    def updateLevelSegments(self, bspTree, playerLevelSegments):
        player = self.gameData.player
        border = player.nextBorder

        levelSegment = self.traversal.findLevelSegmentOrNone(bspTree, border.bottom.downLeft)
        playerLevelSegments.add(levelSegment)

        levelSegment = self.traversal.findLevelSegmentOrNone(bspTree, border.bottom.downRight)
        playerLevelSegments.add(levelSegment)

        levelSegment = self.traversal.findLevelSegmentOrNone(bspTree, border.bottom.upLeft)
        playerLevelSegments.add(levelSegment)

        levelSegment = self.traversal.findLevelSegmentOrNone(bspTree, border.bottom.upRight)
        playerLevelSegments.add(levelSegment)


def makePlayerLevelSegmentsUpdater(resolver):
    return PlayerLevelSegmentsUpdater(resolver.resolve(GameData), resolver.resolve(BSPTreeTraversal))
