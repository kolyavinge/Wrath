from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal
from game.engine.GameData import GameData
from game.model.PlayerState import PlayerState


class PlayerZUpdater:

    def __init__(self, gameData, traversal):
        self.gameData = gameData
        self.traversal = traversal

    def updateIfPlayerMoved(self):
        if self.gameData.player.hasMoved:
            self.update()

    def update(self):
        player = self.gameData.player
        bspTree = self.gameData.level.collisionTree
        levelSegment = self.traversal.findLevelSegmentOrNone(bspTree, player.nextCenterPoint)
        assert levelSegment is not None
        if len(levelSegment.floors) == 1:
            z = levelSegment.floors[0].getZ(player.nextCenterPoint.x, player.nextCenterPoint.y)
            if player.getZ() - z < 0.2:
                player.setZ(z)
                player.fallingTime = 0
                if player.state == PlayerState.fall:
                    player.state = PlayerState.land
                else:
                    player.state = PlayerState.stand
            else:
                player.state = PlayerState.fall
                self.processPlayerFall()
        elif len(levelSegment.floors) == 0:
            player.state = PlayerState.fall
            self.processPlayerFall()
        else:
            raise Exception()

    def processPlayerFall(self):
        player = self.gameData.player
        player.fallingTime += 0.1
        player.setZ(player.getZ() - player.fallingFunc.getValue(player.fallingTime))


def makePlayerZUpdater(resolver):
    return PlayerZUpdater(resolver.resolve(GameData), resolver.resolve(BSPTreeTraversal))
