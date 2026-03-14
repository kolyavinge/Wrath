from game.anx.BulletIdLogic import BulletIdLogic
from game.anx.CommonConstants import CommonConstants
from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal
from game.lib.Random import Random


class GrenadeLogic:

    def __init__(
        self,
        traversal: BSPTreeTraversal,
        bulletIdLogic: BulletIdLogic,
    ):
        self.traversal = traversal
        self.bulletIdLogic = bulletIdLogic

    def makeGrenade(self, gameState, person, weapon, id=None, randomSeed=None):
        grenade = weapon.makeGrenade(person)
        grenade.id = id or self.bulletIdLogic.getBulletId(person.id)
        if randomSeed is not None:
            grenade.randomSeed = randomSeed or Random.getInt(0, CommonConstants.maxBulletSeed)
        gameState.grenades.append(grenade)
        grenade.currentLevelSegment = self.traversal.findLevelSegment(gameState.collisionTree, grenade.currentPosition)
        grenade.nextLevelSegment = grenade.currentLevelSegment

        visibilityLevelSegment = self.traversal.findLevelSegment(gameState.visibilityTree, grenade.currentPosition)
        grenade.currentVisibilityLevelSegment = visibilityLevelSegment
        visibilityLevelSegment.grenades.append(grenade)

        return grenade
