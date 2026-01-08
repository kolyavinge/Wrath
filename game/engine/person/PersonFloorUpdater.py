from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal
from game.engine.GameState import GameState
from game.lib.Query import Query
from game.model.level.NullFloor import NullFloor


class PersonFloorUpdater:

    def __init__(self, gameState: GameState, traversal: BSPTreeTraversal):
        self.gameState = gameState
        self.traversal = traversal

    def updatePlayerNextFloor(self):
        self.updateForPerson(self.gameState.player)

    def updateEnemyNextFloor(self):
        for enemy in self.gameState.enemies:
            self.updateForPerson(enemy)

    def updateForPerson(self, person):
        personPosition = person.nextCenterPoint
        levelSegment = self.traversal.findLevelSegmentOrNone(self.gameState.collisionTree, personPosition)
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

    def commitPlayerNextFloor(self):
        self.gameState.player.currentFloor = self.gameState.player.nextFloor

    def commitEnemyNextFloor(self):
        for enemy in self.gameState.enemies:
            enemy.currentFloor = enemy.nextFloor
