from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal
from game.engine.GameData import GameData


class PersonFloorUpdater:

    def __init__(self, gameData: GameData, traversal: BSPTreeTraversal):
        self.gameData = gameData
        self.traversal = traversal

    def updateNextFloor(self):
        for person in self.gameData.allPerson:
            self.updateForPerson(person)

    def updateForPerson(self, person):
        levelSegment = self.traversal.findLevelSegmentOrNone(self.gameData.collisionTree, person.nextCenterPoint)
        assert levelSegment is not None
        if len(levelSegment.floors) == 0:
            person.nextFloor = None
        elif len(levelSegment.floors) == 1:
            person.nextFloor = levelSegment.floors[0]
        else:
            raise Exception("Wrong floors count in segment. Segment can contain zero or one floor.")

    def commitNextFloor(self):
        for person in self.gameData.allPerson:
            person.currentFloor = person.nextFloor
