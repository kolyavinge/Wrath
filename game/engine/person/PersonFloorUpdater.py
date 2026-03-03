from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal
from game.lib.Query import Query
from game.model.level.NullFloor import NullFloor


class PersonFloorUpdater:

    def __init__(
        self,
        traversal: BSPTreeTraversal,
    ):
        self.traversal = traversal

    def updateAllPersonNextFloor(self, gameState):
        for person in gameState.allPerson:
            self.updateForPerson(person, gameState.collisionTree)

    def updatePlayerNextFloor(self, gameState):
        self.updateForPerson(gameState.player, gameState.collisionTree)

    def updateBotsNextFloor(self, gameState):
        for bot in gameState.bots:
            self.updateForPerson(bot, gameState.collisionTree)

    def updateForPerson(self, person, collisionTree):
        personPosition = person.nextCenterPoint
        levelSegment = self.traversal.findLevelSegment(collisionTree, personPosition)
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

    def commitAllPersonNextFloor(self, gameState):
        for person in gameState.allPerson:
            self.commitForPerson(person)

    def commitPlayerNextFloor(self, gameState):
        self.commitForPerson(gameState.player)

    def commitBotsNextFloor(self, gameState):
        for bot in gameState.bots:
            self.commitForPerson(bot)

    def commitForPerson(self, person):
        person.currentFloor = person.nextFloor
