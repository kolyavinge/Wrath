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

    def onAimStateSwitched(self, args):
        self.player, self.aimState = args
        print(self.aimState)
        if type(self.aimState) == SniperAimState:
            self.updateFunc = self.updateFloating
        else:
            self.updateFunc = self.noUpdate

    def update(self):
        self.updateFunc()

    def updateFloating(self):
        aimState = self.aimState

        aimState.aFloatingParam += Random.getFloat(0.0, 1.0)
        aimState.bFloatingParam += Random.getFloat(0.0, 1.0)

        aFloatingValue = aimState.aFloatingFunc.getValue(aimState.aFloatingParam)
        bFloatingValue = aimState.bFloatingFunc.getValue(aimState.bFloatingParam)

        aDelta = aFloatingValue - aimState.aFloatingValue
        bDelta = bFloatingValue - aimState.bFloatingValue

        aimState.aFloatingValue = aFloatingValue
        aimState.bFloatingValue = bFloatingValue

        self.player.yawRadians += aDelta
        self.player.pitchRadians += bDelta

        self.personTurnLogic.calculateDirectionVectors(self.player)

    def noUpdate(self):
        pass
