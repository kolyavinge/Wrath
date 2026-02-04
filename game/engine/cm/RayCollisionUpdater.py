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
                self.processCollision(gameState, ray, collisionResult)

    def updateForConstructions(self, gameState):
        for ray in gameState.rays:
            collisionResult = self.rayCollisionDetector.getConstructionCollisionResultOrNone(ray, gameState.collisionTree)
            if collisionResult is not None:
                self.processCollision(gameState, ray, collisionResult)

    def processCollision(self, gameState, ray, collisionResult):
        target, collisionResultData = collisionResult
        if target == CollidedTarget.construction:
            self.processConstructionCollision(gameState, ray, collisionResultData)
        elif target == CollidedTarget.onePerson:
            self.processPersonCollision(gameState, ray, collisionResultData)

    def processConstructionCollision(self, gameState, ray, collisionResult):
        collisionPoint, construction = collisionResult
        ray.currentPosition = collisionPoint
        ray.damagedObject = construction
        visibilityLevelSegment = self.traversal.findLevelSegmentOrNone(gameState.visibilityTree, collisionPoint)
        self.bulletHoleLogic.makeHole(gameState, collisionPoint, construction.frontNormal, visibilityLevelSegment, ray.holeInfo)

    def processPersonCollision(self, gameState, ray, collisionResult):
        collisionPoint, person, target = collisionResult
        ray.damagedObject = person
        ray.currentPosition = collisionPoint
        personItems = gameState.allPersonItems[person]
        self.personDamageLogic.damageByRay(person, personItems, ray, gameState.collisionData)
