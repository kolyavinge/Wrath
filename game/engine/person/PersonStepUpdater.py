from game.anx.PersonConstants import PersonConstants
from game.engine.GameState import GameState
from game.lib.EventManager import EventManager, Events
from game.model.level.Stair import Stair
from game.model.person.PersonStates import PersonZState


class PersonStepUpdater:

    def __init__(
        self,
        gameData: GameState,
        eventManager: EventManager,
    ):
        self.gameData = gameData
        self.eventManager = eventManager

    def update(self):
        for person, personItems in self.gameData.allPersonItems.items():
            if person.hasMoved:
                self.updateForPerson(person, personItems)

    def updateForPerson(self, person, personItems):
        doStep = False
        if person.zState == PersonZState.onFloor:
            person.stepTime += 1.0 * personItems.currentWeapon.slowdownCoeff
            if isinstance(person.nextFloor, Stair):
                doStep = person.currentCenterPoint.z != person.nextCenterPoint.z
            else:
                doStep = person.stepTime > PersonConstants.stepTimeLimit

        if doStep:
            person.stepTime = 0
            self.eventManager.raiseEvent(Events.personStepDone, person)
