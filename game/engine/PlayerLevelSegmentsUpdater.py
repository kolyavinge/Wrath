from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal
from game.engine.GameData import GameData


class PlayerLevelSegmentsUpdater:

    def __init__(self, gameData, traversal):
        self.gameData = gameData
        self.traversal = traversal

    def updateIfPlayerMoved(self):
        if self.gameData.player.hasMoved:
            self.update()

    def update(self):
        player = self.gameData.player
        player.collisionLevelSegments = set()
        player.visibilityLevelSegments = set()
        self.updateLevelSegments(self.gameData.collisionTree, player.collisionLevelSegments)
        self.updateLevelSegments(self.gameData.visibilityTree, player.visibilityLevelSegments)

    def updateLevelSegments(self, bspTree, playerLevelSegments):
        border = self.gameData.player.nextBorder

        levelSegment = self.traversal.findLevelSegmentOrNone(bspTree, border.bottom.downLeft)
        assert levelSegment is not None
        playerLevelSegments.add(levelSegment)

        levelSegment = self.traversal.findLevelSegmentOrNone(bspTree, border.bottom.downRight)
        assert levelSegment is not None
        playerLevelSegments.add(levelSegment)

        levelSegment = self.traversal.findLevelSegmentOrNone(bspTree, border.bottom.upLeft)
        assert levelSegment is not None
        playerLevelSegments.add(levelSegment)

        levelSegment = self.traversal.findLevelSegmentOrNone(bspTree, border.bottom.upRight)
        assert levelSegment is not None
        playerLevelSegments.add(levelSegment)


def makePlayerLevelSegmentsUpdater(resolver):
    return PlayerLevelSegmentsUpdater(resolver.resolve(GameData), resolver.resolve(BSPTreeTraversal))
