from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal
from game.engine.GameState import GameState
from game.lib.Query import Query
from game.model.level.NullFloor import NullFloor


class PersonFloorUpdater:

    def __init__(self, gameData: GameState, traversal: BSPTreeTraversal):
        self.gameData = gameData
        self.traversal = traversal

    def updateNextFloor(self):
        for person in self.gameData.allPerson:
            self.updateForPerson(person)

    def updateForPerson(self, person):
        personPosition = person.nextCenterPoint
        levelSegment = self.traversal.findLevelSegmentOrNone(self.gameData.collisionTree, personPosition)
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

    def commitNextFloor(self):
        for person in self.gameData.allPerson:
            person.currentFloor = person.nextFloor
