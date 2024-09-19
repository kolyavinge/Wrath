from game.engine.bsp.BSPTree import BSPNode
from game.engine.bsp.SplitPlane import SplitPlanePosition
from game.model.level.LevelSegment import LevelSegment


class BSPTreeBuilder:

    def build(self, bspTree, level, splitPlanes):
        bspTree.root.levelSegment = LevelSegment()
        bspTree.root.levelSegment.walls = level.walls.copy()
        bspTree.root.levelSegment.floors = level.floors.copy()
        bspTree.root.levelSegment.ceilings = level.ceilings.copy()
        bspTree.root.levelSegment.lights = level.lights.copy()
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
            positionSet = self.getLevelItemPosition(node, wall)
            if SplitPlanePosition.front in positionSet:
                frontSegment.walls.append(wall)
            if SplitPlanePosition.back in positionSet:
                backSegment.walls.append(wall)

        for floor in node.levelSegment.floors:
            positionSet = self.getLevelItemPosition(node, floor)
            if SplitPlanePosition.front in positionSet:
                frontSegment.floors.append(floor)
            if SplitPlanePosition.back in positionSet:
                backSegment.floors.append(floor)

        for ceiling in node.levelSegment.ceilings:
            positionSet = self.getLevelItemPosition(node, ceiling)
            if SplitPlanePosition.front in positionSet:
                frontSegment.ceilings.append(ceiling)
            if SplitPlanePosition.back in positionSet:
                backSegment.ceilings.append(ceiling)

        for light in node.levelSegment.lights:
            position = self.getPointPosition(node, light.position)
            if position == SplitPlanePosition.front or position == SplitPlanePosition.on:
                frontSegment.lights.append(light)
            elif position == SplitPlanePosition.back:
                backSegment.lights.append(light)

        frontSplitPlanes = []
        backSplitPlanes = []
        for splitPlane in splitPlanes:
            position = self.getPointPosition(node, splitPlane.basePoint)
            if position == SplitPlanePosition.front or position == SplitPlanePosition.on:
                frontSplitPlanes.append(splitPlane)
            elif position == SplitPlanePosition.back:
                backSplitPlanes.append(splitPlane)

        frontSegment.commit()
        backSegment.commit()

        return (frontSegment, backSegment, frontSplitPlanes, backSplitPlanes)

    def getLevelItemPosition(self, node, levelItem):
        positionSet = set()
        for borderPoint in levelItem.getBorderPoints():
            position = self.getPointPosition(node, borderPoint)
            if position == SplitPlanePosition.front:
                positionSet.add(SplitPlanePosition.front)
            elif position == SplitPlanePosition.back:
                positionSet.add(SplitPlanePosition.back)
            # ignore SplitPlanePosition.on

        if len(positionSet) == 0:
            positionSet.add(SplitPlanePosition.front)

        return positionSet

    def getPointPosition(self, node, point):
        direction = node.basePoint.getDirectionTo(point)
        dotProduct = direction.dotProduct(node.frontNormal)
        if dotProduct > 0:
            return SplitPlanePosition.front
        elif dotProduct < 0:
            return SplitPlanePosition.back
        else:
            return SplitPlanePosition.on


def makeBSPTreeBuilder(resolver):
    return BSPTreeBuilder()
