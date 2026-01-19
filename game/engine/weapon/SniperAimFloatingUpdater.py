from game.engine.person.PersonTurnLogic import PersonTurnLogic
from game.lib.EventManager import EventManager, Events
from game.lib.Random import Random
from game.model.person.AimState import SniperAimState


class SniperAimFloatingUpdater:

    def __init__(
        self,
        personTurnLogic: PersonTurnLogic,
        eventManager: EventManager,
    ):
        self.personTurnLogic = personTurnLogic
        self.updateFunc = self.noUpdate
        eventManager.attachToEvent(Events.aimStateSwitched, self.onAimStateSwitched)

    def onAimStateSwitched(self, player):
        if type(player.aimState) == SniperAimState:
            self.updateFunc = lambda: self.updateFloating(player)
        else:
            self.updateFunc = self.noUpdate

    def update(self):
        self.updateFunc()

    def updateFloating(self, player):
        aimState = player.aimState

        aimState.aFloatingParam += Random.getFloat(0.0, 1.0)
        aimState.bFloatingParam += Random.getFloat(0.0, 1.0)

        aFloatingValue = aimState.aFloatingFunc.getValue(aimState.aFloatingParam)
        bFloatingValue = aimState.bFloatingFunc.getValue(aimState.bFloatingParam)

        aDelta = aFloatingValue - aimState.aFloatingValue
        bDelta = bFloatingValue - aimState.bFloatingValue

        aimState.aFloatingValue = aFloatingValue
        aimState.bFloatingValue = bFloatingValue

        player.yawRadians += aDelta
        player.pitchRadians += bDelta

        self.personTurnLogic.calculateDirectionVectors(player)

    def noUpdate(self):
        pass
