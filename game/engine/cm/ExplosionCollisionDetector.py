from game.engine.GameState import GameState
from game.model.person.PersonStates import LifeCycle


class ExplosionCollisionDetector:

    def __init__(self, gameState: GameState):
        self.gameState = gameState

    def getCollisionResult(self, explosion):
        return [
            person
            for person in explosion.collisionLevelSegment.allPerson
            if person.lifeCycle == LifeCycle.alive and explosion.position.getLengthTo(person.currentCenterPoint) <= explosion.radius
        ]
