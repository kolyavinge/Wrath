from game.engine.cm.ExplosionCollisionDetector import ExplosionCollisionDetector
from game.engine.GameData import GameData
from game.engine.person.PersonDamageLogic import PersonDamageLogic


class ExplosionCollisionUpdater:

    def __init__(
        self,
        gameData: GameData,
        explosionCollisionDetector: ExplosionCollisionDetector,
        personDamageLogic: PersonDamageLogic,
    ):
        self.gameData = gameData
        self.explosionCollisionDetector = explosionCollisionDetector
        self.personDamageLogic = personDamageLogic

    def update(self):
        for explosion in self.gameData.explosions:
            if explosion.damagePercent > 0:
                collisionResult = self.explosionCollisionDetector.getCollisionResult(explosion)
                for person in collisionResult:
                    self.personDamageLogic.damageByExplosion(person, explosion)
