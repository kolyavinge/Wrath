from game.anx.Events import Events
from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal
from game.engine.GameData import GameData
from game.lib.EventManager import EventManager
from game.model.person.PersonState import PersonState


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
        levelSegment = self.traversal.findLevelSegmentOrNone(self.gameData.collisionTree, player.nextCenterPoint)
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
            if player.state == PersonState.standing:
                player.setZ(z)
            elif player.state == PersonState.falling:
                player.setZ(z)
                player.fallingTime = 0
                player.state = PersonState.landing
                player.landingTime = 10 * 0.1
                self.eventManager.raiseEvent(Events.personLanded, player)
            elif player.state == PersonState.landing:
                player.landingTime -= 0.1
                if player.landingTime <= 0:
                    player.state = PersonState.standing
                    player.landingTime = 0
            else:
                raise Exception("Wrong player state.")
        else:
            player.state = PersonState.falling
            self.processPlayerFall()

    def processHole(self):
        self.gameData.player.state = PersonState.falling
        self.processPlayerFall()

    def processPlayerFall(self):
        player = self.gameData.player
        player.fallingTime += 0.1
        player.setZ(player.getZ() - player.fallingFunc.getValue(player.fallingTime))


def makePlayerZUpdater(resolver):
    return PlayerZUpdater(resolver.resolve(GameData), resolver.resolve(BSPTreeTraversal), resolver.resolve(EventManager))
