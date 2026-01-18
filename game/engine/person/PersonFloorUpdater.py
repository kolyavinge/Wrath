from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal
from game.lib.Query import Query
from game.model.level.NullFloor import NullFloor


class PersonFloorUpdater:

    def __init__(
        self,
        traversal: BSPTreeTraversal,
    ):
        self.traversal = traversal

    def updatePlayerNextFloor(self, gameState):
        self.updateForPerson(gameState.player, gameState.collisionTree)

    def updateEnemyNextFloor(self, gameState):
        for enemy in gameState.enemies:
            self.updateForPerson(enemy, gameState.collisionTree)

    def updateForPerson(self, person, collisionTree):
        personPosition = person.nextCenterPoint
        levelSegment = self.traversal.findLevelSegmentOrNone(collisionTree, personPosition)
        assert levelSegment is not None
        if len(levelSegment.floors) == 0:
            person.nextFloor = NullFloor.instance
        elif len(levelSegment.floors) == 1:
            if levelSegment.floors[0].plane.withinBorder(personPosition):
                person.nextFloor = levelSegment.floors[0]
            else:
                person.nextFloor = NullFloor.instance
        else:
            person.nextFloor = (
                Query(levelSegment.floors)
                .where(lambda floor: floor.plane.withinBorder(personPosition))
                .orderByDesc(lambda floor: floor.getZ(personPosition.x, personPosition.y))
                .firstOrNone()
            ) or NullFloor.instance

    def commitPlayerNextFloor(self, gameState):
        gameState.player.currentFloor = gameState.player.nextFloor

    def commitEnemyNextFloor(self, gameState):
        for enemy in gameState.enemies:
            enemy.currentFloor = enemy.nextFloor
