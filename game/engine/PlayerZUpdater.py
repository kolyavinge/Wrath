from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal
from game.engine.GameData import GameData


class PlayerZUpdater:

    def __init__(self, gameData, traversal):
        self.gameData = gameData
        self.traversal = traversal

    def update(self):
        player = self.gameData.player
        if player.hasMoved:
            bspTree = self.gameData.level.collisionTree
            levelSegment = self.traversal.findLevelSegmentOrNone(bspTree, player.nextCenterPoint)
            assert levelSegment is not None
            z = levelSegment.floor.getZ(player.nextCenterPoint.x, player.nextCenterPoint.y)
            player.setZ(z)


def makePlayerZUpdater(resolver):
    return PlayerZUpdater(resolver.resolve(GameData), resolver.resolve(BSPTreeTraversal))
