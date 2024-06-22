from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal


class LevelSegmentContentAnalyzer:

    def __init__(self, traversal):
        self.traversal = traversal

    def analyze(self, level):
        for floor in level.floors:
            self.analyzeWalls(level.bspTree, floor.walls)

    def analyzeWalls(self, bspTree, walls):
        for wall in walls:
            self.analyzeWall(bspTree, wall)

    def analyzeWall(self, bspTree, wall):
        wallStep = wall.endPoint.getCopy()
        wallStep.sub(wall.startPoint)
        wallStep.setLength(0.1)
        startPoint = wall.startPoint.getCopy()
        startPoint.add(wallStep)
        endPoint = wall.endPoint.getCopy()
        endPoint.sub(wallStep)
        startSegment = self.traversal.findLevelSegmentOrNone(bspTree, startPoint)
        endSegment = self.traversal.findLevelSegmentOrNone(bspTree, endPoint)
        assert startSegment is not None
        assert endSegment is not None
        self.analyzeWallRec(bspTree, wall, startPoint, endPoint, startSegment, endSegment)

    def analyzeWallRec(self, bspTree, wall, startPoint, endPoint, startSegment, endSegment):
        if startSegment == endSegment:
            if wall not in startSegment.walls:
                startSegment.walls.append(wall)
        else:
            middlePoint = endPoint.getCopy()
            middlePoint.sub(startPoint)
            middlePoint.div(2)
            if middlePoint.getLength() > 0.1:
                middlePoint.add(startPoint)
                middleSegment = self.traversal.findLevelSegmentOrNone(bspTree, middlePoint)
                assert middleSegment is not None
                self.analyzeWallRec(bspTree, wall, startPoint, middlePoint, startSegment, middleSegment)
                self.analyzeWallRec(bspTree, wall, middlePoint, endPoint, middleSegment, endSegment)


def makeLevelSegmentContentAnalyzer(resolver):
    return LevelSegmentContentAnalyzer(resolver.resolve(BSPTreeTraversal))
