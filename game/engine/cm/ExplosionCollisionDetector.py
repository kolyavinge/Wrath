from game.engine.GameData import GameData
from game.model.person.PersonStates import LifeCycle


class ExplosionCollisionDetector:

    def __init__(self, gameData: GameData):
        self.gameData = gameData

    def getCollisionResult(self, explosion):
        return [
            person
            for person in explosion.collisionLevelSegment.allPerson
            if person.lifeCycle == LifeCycle.alive and explosion.position.getLengthTo(person.currentCenterPoint) <= explosion.radius
        ]
