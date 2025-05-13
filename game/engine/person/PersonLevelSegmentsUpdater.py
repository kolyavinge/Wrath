from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal
from game.engine.GameData import GameData


class PersonLevelSegmentsUpdater:

    def __init__(
        self,
        gameData: GameData,
        traversal: BSPTreeTraversal,
    ):
        self.gameData = gameData
        self.traversal = traversal

    def updatePerson(self, person):
        self.updateCollisionLevelSegments(person)
        self.updateVisibilityLevelSegment(person)

    def updateCollisionLevelSegments(self, person):
        person.collisionLevelSegments = set()
        bspTree = self.gameData.collisionTree
        self.updateForBorder(person, bspTree, person.currentBorder.bottom)
        self.updateForBorder(person, bspTree, person.currentBorder.top)

    def updateForBorder(self, person, bspTree, border):
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
    return PersonLevelSegmentsUpdater(
        resolver.resolve(GameData),
        resolver.resolve(BSPTreeTraversal),
    )
