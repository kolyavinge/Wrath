from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal
from game.engine.GameData import GameData


class PersonLevelSegmentsUpdater:

    def __init__(self, gameData, traversal):
        self.gameData = gameData
        self.traversal = traversal

    def updatePerson(self, person):
        self.updateCollisionLevelSegments(person)
        self.updateVisibilityLevelSegment(person)

    def updateCollisionLevelSegments(self, person):
        border = person.nextBorder.bottom
        bspTree = self.gameData.collisionTree
        person.collisionLevelSegments = set()

        levelSegment = self.traversal.findLevelSegmentOrNone(bspTree, border.downLeft)
        assert levelSegment is not None
        person.collisionLevelSegments.add(levelSegment)

        levelSegment = self.traversal.findLevelSegmentOrNone(bspTree, border.downRight)
        assert levelSegment is not None
        person.collisionLevelSegments.add(levelSegment)

        levelSegment = self.traversal.findLevelSegmentOrNone(bspTree, border.upLeft)
        assert levelSegment is not None
        person.collisionLevelSegments.add(levelSegment)

        levelSegment = self.traversal.findLevelSegmentOrNone(bspTree, border.upRight)
        assert levelSegment is not None
        person.collisionLevelSegments.add(levelSegment)

    def updateVisibilityLevelSegment(self, person):
        person.visibilityLevelSegment = self.traversal.findLevelSegmentOrNone(self.gameData.visibilityTree, person.currentCenterPoint)
        assert person.visibilityLevelSegment is not None


def makePersonLevelSegmentsUpdater(resolver):
    return PersonLevelSegmentsUpdater(resolver.resolve(GameData), resolver.resolve(BSPTreeTraversal))
