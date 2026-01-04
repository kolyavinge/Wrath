from game.engine.GameState import GameState
from game.model.person.PersonStates import PersonZState


class PersonPositionUpdater:

    def __init__(self, gameData: GameState):
        self.gameData = gameData

    def moveNextPosition(self):
        for person in self.gameData.allPerson:
            if person.velocityValue > 0:
                person.hasMoved = True
                person.moveNextPositionBy(person.velocityVector)

    def commitNextPosition(self):
        for person in self.gameData.allPerson:
            if person.hasMoved:
                person.commitNextPosition()

    def resetMovedAndTurned(self):
        for person in self.gameData.allPerson:
            person.hasTurned = False
            if person.hasMoved and person.zState == PersonZState.onFloor:
                person.hasMoved = False
