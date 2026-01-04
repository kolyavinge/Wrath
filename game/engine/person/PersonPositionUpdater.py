from game.engine.GameState import GameState
from game.model.person.PersonStates import PersonZState


class PersonPositionUpdater:

    def __init__(self, gameState: GameState):
        self.gameState = gameState

    def moveNextPosition(self):
        for person in self.gameState.allPerson:
            if person.velocityValue > 0:
                person.hasMoved = True
                person.moveNextPositionBy(person.velocityVector)

    def commitNextPosition(self):
        for person in self.gameState.allPerson:
            if person.hasMoved:
                person.commitNextPosition()

    def resetMovedAndTurned(self):
        for person in self.gameState.allPerson:
            person.hasTurned = False
            if person.hasMoved and person.zState == PersonZState.onFloor:
                person.hasMoved = False
