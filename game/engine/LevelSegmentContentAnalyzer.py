from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal


class LevelSegmentContentAnalyzer:

    def __init__(self, traversal):
        self.traversal = traversal

    def analyze(self, level):
        for floor in level.floors:
            self.analyzeWalls(floor.bspTree, floor.walls)

    def analyzeWalls(self, bspTree, walls):
        for wall in walls:
            levelSegment = self.traversal.findLevelSegmentOrNone(bspTree, wall.startPosition)
            if levelSegment is None:
                levelSegment = self.traversal.findLevelSegmentOrNone(bspTree, wall.endPosition)
            assert levelSegment is not None
            levelSegment.walls.append(wall)


def makeLevelSegmentContentAnalyzer(resolver):
    return LevelSegmentContentAnalyzer(resolver.resolve(BSPTreeTraversal))
