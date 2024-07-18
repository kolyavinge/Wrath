from game.calc.Vector3Utils import Vector3Utils
from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal


class LevelSegmentFloorAnalyzer:

    def __init__(self, traversal):
        self.traversal = traversal

    def analyzeFloors(self, level, bspTree):
        for floor in level.floors:
            self.analyzeDirection(bspTree, floor, floor.downLeft, floor.upRight)
            self.analyzeDirection(bspTree, floor, floor.upLeft, floor.downRight)

            direction = floor.upRight.getDirectionTo(floor.downLeft)
            direction.setLength(0.1)

            from1 = floor.downLeft.getCopy()
            from1.add(direction)
            self.analyzeDirection(bspTree, floor, from1, floor.upLeft)
            self.analyzeDirection(bspTree, floor, from1, floor.downRight)

            from1 = floor.upRight.getCopy()
            from1.sub(direction)
            self.analyzeDirection(bspTree, floor, from1, floor.upLeft)
            self.analyzeDirection(bspTree, floor, from1, floor.downRight)

    def analyzeDirection(self, bspTree, floor, startPoint, endPoint):
        direction = endPoint.getDirectionTo(startPoint)
        direction.setLength(0.1)
        startPoint = startPoint.getCopy()
        endPoint = endPoint.getCopy()
        startPoint.add(direction)
        endPoint.sub(direction)

        def checkPoint(point):
            point.z = floor.getZ(point.x, point.y)
            levelSegment = self.traversal.findLevelSegmentOrNone(bspTree, point)
            if floor not in levelSegment.floors:
                levelSegment.floors.append(floor)

        Vector3Utils.fromStartToEnd(startPoint, endPoint, 0.1, checkPoint)


def makeLevelSegmentFloorAnalyzer(resolver):
    return LevelSegmentFloorAnalyzer(resolver.resolve(BSPTreeTraversal))
