from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal
from game.engine.cm.PersonCollisionDetector import PersonCollisionDetector
from game.engine.cm.PersonWallCollisionDetector import PersonWallCollisionDetector


class EnemyCollisionDetector:

    def __init__(
        self,
        personWallCollisionDetector: PersonWallCollisionDetector,
        personCollisionDetector: PersonCollisionDetector,
        traversal: BSPTreeTraversal,
    ):
        self.personWallCollisionDetector = personWallCollisionDetector
        self.personCollisionDetector = personCollisionDetector
        self.traversal = traversal

    def anyCollisions(self, enemy, direction, collisionTree):
        nextCenterPoint = enemy.currentFootRect.center.copy()
        nextCenterPoint.add(direction)
        nextCenterPointLevelSegment = self.traversal.findLevelSegmentOrNone(collisionTree, nextCenterPoint)

        return (
            self.anyWallCollisions(enemy, nextCenterPoint, nextCenterPointLevelSegment)
            or self.anyOtherPersonCollisions(enemy, nextCenterPoint, nextCenterPointLevelSegment)
            or self.anyVoidCollisions(nextCenterPointLevelSegment)
        )

    def anyWallCollisions(self, enemy, nextCenterPoint, nextCenterPointLevelSegment):
        for wall in enemy.currentCenterPointLevelSegment.walls:
            if self.personWallCollisionDetector.isCollidedWall(wall, enemy.currentFootRect.center, nextCenterPoint):
                return True

        if enemy.currentCenterPointLevelSegment != nextCenterPointLevelSegment:
            for wall in nextCenterPointLevelSegment.walls:
                if self.personWallCollisionDetector.isCollidedWall(wall, enemy.currentFootRect.center, nextCenterPoint):
                    return True

        return False

    def anyOtherPersonCollisions(self, enemy, nextCenterPoint, nextCenterPointLevelSegment):
        for person in enemy.currentCenterPointLevelSegment.allPerson:
            if person != enemy:
                if self.personCollisionDetector.getCollisionLengthBetweenPointsOrNone(person.currentCenterPoint, nextCenterPoint) is not None:
                    return True

        if enemy.currentCenterPointLevelSegment != nextCenterPointLevelSegment:
            for person in nextCenterPointLevelSegment.allPerson:
                if person != enemy:
                    if self.personCollisionDetector.getCollisionLengthBetweenPointsOrNone(person.currentCenterPoint, nextCenterPoint) is not None:
                        return True

        return False

    def anyVoidCollisions(self, nextCenterPointLevelSegment):
        return len(nextCenterPointLevelSegment.floors) == 0
