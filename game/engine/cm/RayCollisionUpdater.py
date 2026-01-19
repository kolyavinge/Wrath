from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal
from game.engine.cm.CollidedTarget import CollidedTarget
from game.engine.cm.RayCollisionDetector import RayCollisionDetector
from game.engine.person.PersonDamageLogic import PersonDamageLogic
from game.engine.weapon.BulletHoleLogic import BulletHoleLogic
from game.engine.weapon.ExplosionLogic import ExplosionLogic


class RayCollisionUpdater:

    def __init__(
        self,
        traversal: BSPTreeTraversal,
        rayCollisionDetector: RayCollisionDetector,
        bulletHoleLogic: BulletHoleLogic,
        personDamageLogic: PersonDamageLogic,
        explosionLogic: ExplosionLogic,
    ):
        self.traversal = traversal
        self.rayCollisionDetector = rayCollisionDetector
        self.bulletHoleLogic = bulletHoleLogic
        self.personDamageLogic = personDamageLogic
        self.explosionLogic = explosionLogic

    def update(self, gameState):
        for ray in gameState.rays:
            collisionResult = self.rayCollisionDetector.getCollisionResultOrNone(ray, gameState.collisionTree)
            if collisionResult is not None:
                self.processCollision(ray, collisionResult, gameState.visibilityTree)

    def processCollision(self, ray, collisionResult, visibilityTree):
        target, collisionResultData = collisionResult
        if target == CollidedTarget.construction:
            self.processConstructionCollision(ray, collisionResultData, visibilityTree)
        elif target == CollidedTarget.onePerson:
            self.processPersonCollision(ray, collisionResultData)

    def processConstructionCollision(self, ray, collisionResult, visibilityTree):
        collisionPoint, construction = collisionResult
        ray.endPosition = collisionPoint
        ray.damagedObject = construction
        visibilityLevelSegment = self.traversal.findLevelSegmentOrNone(visibilityTree, collisionPoint)
        self.bulletHoleLogic.makeHole(collisionPoint, construction.frontNormal, visibilityLevelSegment, ray.holeInfo)

    def processPersonCollision(self, ray, collisionResult):
        collisionPoint, person, target = collisionResult
        ray.damagedObject = person
        ray.endPosition = collisionPoint
        self.personDamageLogic.damageByRay(person, ray)
