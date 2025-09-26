from game.engine.GameData import GameData


class ExplosionCollisionDetector:

    def __init__(self, gameData: GameData):
        self.gameData = gameData

    def getCollisionResult(self, explosion):
        return [
            person
            for person in explosion.collisionLevelSegment.allPerson
            if explosion.position.getLengthTo(person.currentCenterPoint) <= explosion.radius
        ]
