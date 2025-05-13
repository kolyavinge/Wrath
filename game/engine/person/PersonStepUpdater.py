from game.anx.Events import Events
from game.engine.GameData import GameData
from game.lib.EventManager import EventManager
from game.model.level.Stair import Stair


class PersonStepUpdater:

    def __init__(
        self,
        gameData: GameData,
        eventManager: EventManager,
    ):
        self.gameData = gameData
        self.eventManager = eventManager

    def update(self):
        doStep = False
        player = self.gameData.player
        if isinstance(player.currentFloor, Stair):
            doStep = player.currentCenterPoint.z != player.nextCenterPoint.z
        else:
            doStep = (
                player.prevPrevSwingValue < 0
                and player.prevSwingValue < 0
                and player.currentSwingValue < 0
                and player.prevPrevSwingValue > player.prevSwingValue
                and player.currentSwingValue > player.prevSwingValue
            )

        if doStep:
            self.eventManager.raiseEvent(Events.personStepDone, player)
