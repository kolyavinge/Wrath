from game.anx.Events import Events
from game.engine.GameData import GameData
from game.lib.EventManager import EventManager
from game.model.person.PersonStates import PersonZState


class PersonJumpUpdater:

    def __init__(
        self,
        gameData: GameData,
        eventManager: EventManager,
    ):
        self.gameData = gameData
        self.eventManager = eventManager

    def update(self):
        for person, inputData in self.gameData.allPersonInputData.items():
            self.updateForPerson(person, inputData)

    def updateForPerson(self, person, inputData):
        isJumpAvailable = inputData.jump and (person.zState == PersonZState.onFloor or person.zState == PersonZState.jumping)

        if not isJumpAvailable:
            person.jumpingTime = 0
            person.jumpingValue = 0
            return

        if person.jumpingTime <= 1.0:
            person.jumpingTime += 0.1
            if person.jumpingTime == 0.5:
                self.eventManager.raiseEvent(Events.personJumped, person)
        else:
            person.jumpingTime = 0

        person.jumpingValue = person.jumpingFunc.getValue(person.jumpingTime)
        person.hasMoved = True
