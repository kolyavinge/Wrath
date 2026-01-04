from game.engine.GameState import GameState
from game.engine.person.PersonTurnLogic import PersonTurnLogic
from game.lib.EventManager import EventManager, Events
from game.lib.Random import Random
from game.model.person.AimState import SniperAimState


class SniperAimFloatingUpdater:

    def __init__(
        self,
        gameState: GameState,
        personTurnLogic: PersonTurnLogic,
        eventManager: EventManager,
    ):
        self.gameState = gameState
        self.personTurnLogic = personTurnLogic
        self.updateFunc = self.noUpdate
        eventManager.attachToEvent(Events.aimStateSwitched, self.onAimStateSwitched)

    def onAimStateSwitched(self, aimState):
        if type(aimState) == SniperAimState:
            self.updateFunc = self.updateFloating
        else:
            self.updateFunc = self.noUpdate

    def update(self):
        self.updateFunc()

    def updateFloating(self):
        aimState = self.gameState.aimState

        aimState.aFloatingParam += Random.getFloat(0.0, 1.0)
        aimState.bFloatingParam += Random.getFloat(0.0, 1.0)

        aFloatingValue = aimState.aFloatingFunc.getValue(aimState.aFloatingParam)
        bFloatingValue = aimState.bFloatingFunc.getValue(aimState.bFloatingParam)

        aDelta = aFloatingValue - aimState.aFloatingValue
        bDelta = bFloatingValue - aimState.bFloatingValue

        aimState.aFloatingValue = aFloatingValue
        aimState.bFloatingValue = bFloatingValue

        player = self.gameState.player
        player.yawRadians += aDelta
        player.pitchRadians += bDelta

        self.personTurnLogic.calculateDirectionVectors(player)

    def noUpdate(self):
        pass
