from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal


class PersonLevelSegmentsUpdater:

    def __init__(
        self,
        traversal: BSPTreeTraversal,
    ):
        self.traversal = traversal

    def updatePerson(self, person, collisionTree, visibilityTree):
        self.updateCollisionLevelSegments(person, collisionTree)
        self.updateVisibilityLevelSegment(person, visibilityTree)

    def updateCollisionLevelSegments(self, person, collisionTree):
        person.collisionLevelSegments = set()
        self.updateForBorder(person, collisionTree, person.currentBorder.bottom)
        self.updateForBorder(person, collisionTree, person.currentBorder.top)

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

    def updateVisibilityLevelSegment(self, person, visibilityTree):
        person.visibilityLevelSegment = self.traversal.findLevelSegmentOrNone(visibilityTree, person.currentCenterPoint)
        assert person.visibilityLevelSegment is not None
