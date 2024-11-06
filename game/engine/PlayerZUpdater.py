from game.anx.Events import Events
from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal
from game.engine.GameData import GameData
from game.lib.EventManager import EventManager
from game.model.player.PlayerState import PlayerState


class PlayerZUpdater:

    def __init__(self, gameData, traversal, eventManager):
        self.gameData = gameData
        self.traversal = traversal
        self.eventManager = eventManager

    def updateIfPlayerMoved(self):
        if self.gameData.player.hasMoved:
            self.update()

    def update(self):
        player = self.gameData.player
        bspTree = self.gameData.level.collisionTree
        levelSegment = self.traversal.findLevelSegmentOrNone(bspTree, player.nextCenterPoint)
        assert levelSegment is not None
        if len(levelSegment.floors) == 1:
            self.processFloor(levelSegment)
        elif len(levelSegment.floors) == 0:
            self.processHole()
        else:
            raise Exception("Wrong floors count in segment.")

    def processFloor(self, levelSegment):
        player = self.gameData.player
        floor = levelSegment.floors[0]
        player.currentFloor = floor
        z = floor.getZ(player.nextCenterPoint.x, player.nextCenterPoint.y)
        playerOnFloor = player.getZ() - z < 1 or player.getZ() < z
        if playerOnFloor:
            if player.state == PlayerState.standing:
                player.setZ(z)
            elif player.state == PlayerState.falling:
                player.setZ(z)
                player.fallingTime = 0
                player.state = PlayerState.landing
                player.landingTime = 10 * 0.1
                self.eventManager.raiseEvent(Events.personLanded, player)
            elif player.state == PlayerState.landing:
                player.landingTime -= 0.1
                if player.landingTime <= 0:
                    player.state = PlayerState.standing
                    player.landingTime = 0
            else:
                raise Exception("Wrong player state.")
        else:
            player.state = PlayerState.falling
            self.processPlayerFall()

    def processHole(self):
        self.gameData.player.state = PlayerState.falling
        self.processPlayerFall()

    def processPlayerFall(self):
        player = self.gameData.player
        player.fallingTime += 0.1
        player.setZ(player.getZ() - player.fallingFunc.getValue(player.fallingTime))


def makePlayerZUpdater(resolver):
    return PlayerZUpdater(resolver.resolve(GameData), resolver.resolve(BSPTreeTraversal), resolver.resolve(EventManager))
