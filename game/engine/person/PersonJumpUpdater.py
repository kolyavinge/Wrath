from game.engine.GameData import GameData
from game.model.person.PersonZState import PersonZState


class PersonJumpUpdater:

    def __init__(self, gameData: GameData):
        self.gameData = gameData

    def update(self):
        for person in self.gameData.allPerson:
            inputData = self.gameData.allPersonInputData[person]
            self.updateForPerson(person, inputData)

    def updateForPerson(self, person, inputData):
        isJumpAvailable = inputData.jump and (person.zState == PersonZState.onFloor or person.zState == PersonZState.jumping)

        if not isJumpAvailable:
            person.jumpingTime = 0
            person.jumpingValue = 0
            return

        if person.jumpingTime <= 1.0:
            person.jumpingTime += 0.1
        else:
            person.jumpingTime = 0

        person.jumpingValue = person.jumpingFunc.getValue(person.jumpingTime)
        person.hasMoved = True
