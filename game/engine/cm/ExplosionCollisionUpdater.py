from game.engine.cm.ExplosionCollisionDetector import ExplosionCollisionDetector
from game.engine.person.PersonDamageLogic import PersonDamageLogic


class ExplosionCollisionUpdater:

    def __init__(
        self,
        explosionCollisionDetector: ExplosionCollisionDetector,
        personDamageLogic: PersonDamageLogic,
    ):
        self.explosionCollisionDetector = explosionCollisionDetector
        self.personDamageLogic = personDamageLogic

    def update(self, gameState):
        for explosion in gameState.explosions:
            if explosion.damagePercent > 0:
                collisionResult = self.explosionCollisionDetector.getCollisionResult(explosion)
                for person in collisionResult:
                    self.personDamageLogic.damageByExplosion(person, explosion)
