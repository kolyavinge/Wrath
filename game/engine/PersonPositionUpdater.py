from game.engine.GameData import GameData
from game.model.person.PersonState import PersonState


class PersonPositionUpdater:

    def __init__(self, gameData):
        self.gameData = gameData

    def moveNextPosition(self):
        for person in self.gameData.allPerson:
            if person.velocityValue > 0:
                person.hasMoved = True
                person.moveNextPositionBy(person.velocityVector)

    def commitNextPosition(self):
        for person in self.gameData.allPerson:
            person.hasTurned = False
            if person.hasMoved:
                person.commitNextPosition()
                if person.state == PersonState.standing:
                    person.hasMoved = False


def makePersonPositionUpdater(resolver):
    return PersonPositionUpdater(resolver.resolve(GameData))
