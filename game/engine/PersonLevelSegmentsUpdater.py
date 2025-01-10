from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal
from game.engine.GameData import GameData


class PersonLevelSegmentsUpdater:

    def __init__(self, gameData, traversal):
        self.gameData = gameData
        self.traversal = traversal

    def updateIfMoved(self):
        for person in self.gameData.allPerson:
            if person.hasMoved:
                self.updatePerson(person)

    def update(self):
        for person in self.gameData.allPerson:
            self.updatePerson(person)

    def updatePerson(self, person):
        person.collisionLevelSegments = set()
        person.visibilityLevelSegments = set()
        self.updatePersonLevelSegments(self.gameData.collisionTree, person, person.collisionLevelSegments)
        self.updatePersonLevelSegments(self.gameData.visibilityTree, person, person.visibilityLevelSegments)

    def updatePersonLevelSegments(self, bspTree, person, personLevelSegments):
        border = person.nextBorder.bottom

        levelSegment = self.traversal.findLevelSegmentOrNone(bspTree, border.downLeft)
        assert levelSegment is not None
        personLevelSegments.add(levelSegment)

        levelSegment = self.traversal.findLevelSegmentOrNone(bspTree, border.downRight)
        assert levelSegment is not None
        personLevelSegments.add(levelSegment)

        levelSegment = self.traversal.findLevelSegmentOrNone(bspTree, border.upLeft)
        assert levelSegment is not None
        personLevelSegments.add(levelSegment)

        levelSegment = self.traversal.findLevelSegmentOrNone(bspTree, border.upRight)
        assert levelSegment is not None
        personLevelSegments.add(levelSegment)


def makePersonLevelSegmentsUpdater(resolver):
    return PersonLevelSegmentsUpdater(resolver.resolve(GameData), resolver.resolve(BSPTreeTraversal))
