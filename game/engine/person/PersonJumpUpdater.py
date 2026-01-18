from game.lib.EventManager import EventManager, Events
from game.model.person.PersonStates import PersonZState


class PersonJumpUpdater:

    def __init__(
        self,
        eventManager: EventManager,
    ):
        self.eventManager = eventManager

    def updateForPlayer(self, gameState):
        self.updateForPerson(gameState.player, gameState.playerInputData)

    def updateForEnemies(self, gameState):
        for enemy, inputData in gameState.enemyInputData.items():
            self.updateForPerson(enemy, inputData)

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
