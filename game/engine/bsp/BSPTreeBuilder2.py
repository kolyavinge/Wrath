from game.engine.bsp.BSPTree import BSPNode
from game.engine.bsp.SplitPlanePosition import SplitPlanePosition
from game.model.level.LevelSegment import LevelSegment


class BSPTreeBuilder2:

    def build(self, bspTree, splitPlanes):
        self.buildRec(bspTree.root, splitPlanes)

    def buildRec(self, node, splitPlanes):
        splitPlane = splitPlanes[0]
        splitPlanes.remove(splitPlane)
        node.basePoint = splitPlane.basePoint
        node.frontNormal = splitPlane.frontNormal
        frontSegment, backSegment, frontSplitPlanes, backSplitPlanes = self.getFrontAndBackSegments(node, splitPlanes)
        node.front = BSPNode()
        node.front.levelSegment = frontSegment
        if frontSplitPlanes:
            self.buildRec(node.front, frontSplitPlanes)
        else:
            node.front.isLeaf = True
        node.back = BSPNode()
        node.back.levelSegment = backSegment
        if backSplitPlanes:
            self.buildRec(node.back, backSplitPlanes)
        else:
            node.back.isLeaf = True

    def getFrontAndBackSegments(self, node, splitPlanes):
        frontSegment = LevelSegment()
        backSegment = LevelSegment()

        for wall in node.levelSegment.walls:
            positionSet = self.getSplitPlanePositionSet(node, wall)
            if SplitPlanePosition.front in positionSet:
                frontSegment.walls.append(wall)
                if wall.checkSegmentVisibility:
                    frontSegment.checkSegmentVisibilityWalls.append(wall)
            if SplitPlanePosition.back in positionSet:
                backSegment.walls.append(wall)
                if wall.checkSegmentVisibility:
                    backSegment.checkSegmentVisibilityWalls.append(wall)

        for floor in node.levelSegment.floors:
            positionSet = self.getSplitPlanePositionSet(node, floor)
            if SplitPlanePosition.front in positionSet:
                frontSegment.floors.append(floor)
            if SplitPlanePosition.back in positionSet:
                backSegment.floors.append(floor)

        for ceiling in node.levelSegment.ceilings:
            positionSet = self.getSplitPlanePositionSet(node, ceiling)
            if SplitPlanePosition.front in positionSet:
                frontSegment.ceilings.append(ceiling)
            if SplitPlanePosition.back in positionSet:
                backSegment.ceilings.append(ceiling)

        frontSplitPlanes = []
        backSplitPlanes = []
        for splitPlane in splitPlanes:
            if self.toFront(node, splitPlane.basePoint):
                frontSplitPlanes.append(splitPlane)
            else:
                backSplitPlanes.append(splitPlane)

        return (frontSegment, backSegment, frontSplitPlanes, backSplitPlanes)

    def getSplitPlanePositionSet(self, node, levelItem):
        positionSet = set()
        for borderPoint in levelItem.getBorderPoints():
            if self.toFront(node, borderPoint):
                positionSet.add(SplitPlanePosition.front)
            else:
                positionSet.add(SplitPlanePosition.back)

    def toFront(self, node, point):
        direction = node.basePoint.getDirectionTo(point)
        dotProduct = direction.dotProduct(node.frontNormal)

        return dotProduct >= 0


def makeBSPTreeBuilder2(resolver):
    return BSPTreeBuilder2()
