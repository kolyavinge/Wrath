from game.engine.GameState import GameState
from game.model.person.PersonStates import PersonZState


class PersonPositionUpdater:

    def __init__(self, gameState: GameState):
        self.gameState = gameState

    def movePlayerNextPosition(self):
        self.movePersonNextPosition(self.gameState.player)

    def moveEnemyNextPosition(self):
        for enemy in self.gameState.enemies:
            self.movePersonNextPosition(enemy)

    def movePersonNextPosition(self, person):
        if person.velocityValue > 0:
            person.hasMoved = True
            person.moveNextPositionBy(person.velocityVector)

    def commitPlayerNextPosition(self):
        if self.gameState.player.hasMoved:
            self.gameState.player.commitNextPosition()

    def commitEnemyNextPosition(self):
        for enemy in self.gameState.enemies:
            if enemy.hasMoved:
                enemy.commitNextPosition()

    def resetMovedAndTurned(self):
        for person in self.gameState.allPerson:
            person.hasTurned = False
            if person.hasMoved and person.zState == PersonZState.onFloor:
                person.hasMoved = False
