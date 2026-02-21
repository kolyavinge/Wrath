from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal
from game.engine.cm.PersonCollisionDetector import PersonCollisionDetector
from game.engine.cm.PersonWallCollisionDetector import PersonWallCollisionDetector


class CollisionDetector:

    def __init__(
        self,
        personWallCollisionDetector: PersonWallCollisionDetector,
        personCollisionDetector: PersonCollisionDetector,
        traversal: BSPTreeTraversal,
    ):
        self.personWallCollisionDetector = personWallCollisionDetector
        self.personCollisionDetector = personCollisionDetector
        self.traversal = traversal

    def anyCollisions(self, bot, direction, collisionTree):
        nextCenterPoint = bot.currentFootRect.center.copy()
        nextCenterPoint.add(direction)
        nextCenterPointLevelSegment = self.traversal.findLevelSegment(collisionTree, nextCenterPoint)

        return (
            self.anyWallCollisions(bot, nextCenterPoint, nextCenterPointLevelSegment)
            or self.anyOtherPersonCollisions(bot, nextCenterPoint, nextCenterPointLevelSegment)
            or self.anyVoidCollisions(nextCenterPointLevelSegment)
        )

    def anyWallCollisions(self, bot, nextCenterPoint, nextCenterPointLevelSegment):
        for wall in bot.currentCenterPointLevelSegment.walls:
            if self.personWallCollisionDetector.isCollidedWall(wall, bot.currentFootRect.center, nextCenterPoint):
                return True

        if bot.currentCenterPointLevelSegment != nextCenterPointLevelSegment:
            for wall in nextCenterPointLevelSegment.walls:
                if self.personWallCollisionDetector.isCollidedWall(wall, bot.currentFootRect.center, nextCenterPoint):
                    return True

        return False

    def anyOtherPersonCollisions(self, bot, nextCenterPoint, nextCenterPointLevelSegment):
        for person in bot.currentCenterPointLevelSegment.allPerson:
            if person != bot:
                if self.personCollisionDetector.getCollisionLengthBetweenPointsOrNone(person.currentCenterPoint, nextCenterPoint) is not None:
                    return True

        if bot.currentCenterPointLevelSegment != nextCenterPointLevelSegment:
            for person in nextCenterPointLevelSegment.allPerson:
                if person != bot:
                    if self.personCollisionDetector.getCollisionLengthBetweenPointsOrNone(person.currentCenterPoint, nextCenterPoint) is not None:
                        return True

        return False

    def anyVoidCollisions(self, nextCenterPointLevelSegment):
        return len(nextCenterPointLevelSegment.floors) == 0
