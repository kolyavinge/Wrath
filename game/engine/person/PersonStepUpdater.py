from game.anx.Events import Events
from game.anx.PersonConstants import PersonConstants
from game.engine.GameData import GameData
from game.lib.EventManager import EventManager
from game.model.level.Stair import Stair
from game.model.person.PersonStates import PersonZState


class PersonStepUpdater:

    def __init__(
        self,
        gameData: GameData,
        eventManager: EventManager,
    ):
        self.gameData = gameData
        self.eventManager = eventManager

    def update(self):
        for person in self.gameData.allPerson:
            if person.hasMoved:
                self.updateForPerson(person)

    def updateForPerson(self, person):
        doStep = False
        if person.zState == PersonZState.onFloor:
            person.stepTime += 1
            if isinstance(person.nextFloor, Stair):
                doStep = person.currentCenterPoint.z != person.nextCenterPoint.z
            else:
                doStep = person.stepTime > PersonConstants.stepTimeLimit

        if doStep:
            person.stepTime = 0
            self.eventManager.raiseEvent(Events.personStepDone, person)
