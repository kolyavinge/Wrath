from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal
from game.engine.cm.CollidedTarget import CollidedTarget
from game.engine.cm.RayCollisionDetector import RayCollisionDetector
from game.engine.GameData import GameData
from game.engine.person.PersonDamageLogic import PersonDamageLogic
from game.engine.weapon.BulletHoleFactory import BulletHoleFactory
from game.engine.weapon.ExplosionLogic import ExplosionLogic
from game.lib.EventManager import EventManager, Events


class RayCollisionUpdater:

    def __init__(
        self,
        gameData: GameData,
        traversal: BSPTreeTraversal,
        rayCollisionDetector: RayCollisionDetector,
        bulletHoleFactory: BulletHoleFactory,
        personDamageLogic: PersonDamageLogic,
        explosionLogic: ExplosionLogic,
        eventManager: EventManager,
    ):
        self.gameData = gameData
        self.traversal = traversal
        self.rayCollisionDetector = rayCollisionDetector
        self.bulletHoleFactory = bulletHoleFactory
        self.personDamageLogic = personDamageLogic
        self.explosionLogic = explosionLogic
        self.eventManager = eventManager

    def update(self):
        for ray in self.gameData.rays:
            collisionResult = self.rayCollisionDetector.getCollisionResultOrNone(ray)
            if collisionResult is not None:
                self.processCollision(ray, collisionResult)

    def processCollision(self, ray, collisionResult):
        target, collisionResultData = collisionResult
        if target == CollidedTarget.construction:
            self.processConstructionCollision(ray, collisionResultData)
        elif target == CollidedTarget.onePerson:
            self.processPersonCollision(ray, collisionResultData)

    def processConstructionCollision(self, ray, collisionResult):
        collisionPoint, construction = collisionResult
        ray.endPosition = collisionPoint
        ray.damagedObject = construction
        # bspTree = self.gameData.visibilityTree
        # visibilityLevelSegment = self.traversal.findLevelSegmentOrNone(bspTree, collisionPoint)
        # bulletHole = self.bulletHoleFactory.make(collisionPoint, construction.frontNormal, visibilityLevelSegment, ray.holeInfo)
        # self.eventManager.raiseEvent(Events.bulletHoleAdded, bulletHole)

    def processPersonCollision(self, ray, collisionResult):
        collisionPoint, person, target = collisionResult
        ray.damagedObject = person
        ray.endPosition = collisionPoint
        self.personDamageLogic.damageByRay(person, ray)
