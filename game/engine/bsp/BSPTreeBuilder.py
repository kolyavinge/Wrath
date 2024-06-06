from game.model.level.Wall import WallOrientation
from game.model.level.BSPTree import BSPNode
from game.model.level.LevelSegment import LevelSegment
from game.engine.bsp.SplitBorder import SplitBorder
from game.engine.bsp.WallFrontBackPosition import WallFrontBackPosition


class BSPTreeBuilder:

    def build(self, level):
        for floor in level.floors:
            maxX = max([w.getMaxX() for w in floor.walls])
            maxY = max([w.getMaxY() for w in floor.walls])
            splitBorder = SplitBorder(0, maxX, 0, maxY)
            self.buildRec(floor.bspTree.root, WallOrientation.vertical, splitBorder, floor.walls)

    def buildRec(self, node, splitOrientation, splitBorder, walls):
        splitWalls = [w for w in walls if w.orientation == splitOrientation]
        self.sortSplitWalls(splitWalls, splitOrientation)
        middleWall = splitWalls[int(len(splitWalls) / 2)]
        walls.remove(middleWall)
        node.basePoint = middleWall.startPosition
        node.frontNormal = middleWall.frontNormal
        frontWalls, backWalls = self.getFrontAndBackWalls(walls, node.basePoint, node.frontNormal)
        oppositeSplitOrientation = WallOrientation.getOpposite(splitOrientation)
        node.front = BSPNode()
        splitBorder = self.getFrontSplitBorder(splitBorder, node.basePoint, node.frontNormal)
        if frontWalls:
            self.buildRec(node.front, oppositeSplitOrientation, splitBorder, frontWalls)
        else:
            node.front.levelSegment = LevelSegment(splitBorder.minX, splitBorder.maxX, splitBorder.minY, splitBorder.maxY)
        if backWalls:
            node.back = BSPNode()
            splitBorder = self.getBackSplitBorder(splitBorder, node.basePoint, node.frontNormal)
            self.buildRec(node.back, oppositeSplitOrientation, splitBorder, backWalls)

    def getFrontSplitBorder(self, splitBorder, basePoint, frontNormal):
        if frontNormal.y == 1:
            return SplitBorder(splitBorder.minX, splitBorder.maxX, basePoint.y, splitBorder.maxY)
        elif frontNormal.y == -1:
            return SplitBorder(splitBorder.minX, splitBorder.maxX, splitBorder.minY, basePoint.y)
        elif frontNormal.x == 1:
            return SplitBorder(basePoint.x, splitBorder.maxX, splitBorder.minY, splitBorder.maxY)
        elif frontNormal.x == -1:
            return SplitBorder(splitBorder.minX, basePoint.x, splitBorder.minY, splitBorder.maxY)
        else:
            raise Exception()

    def getBackSplitBorder(self, splitBorder, basePoint, frontNormal):
        if frontNormal.y == 1:
            return SplitBorder(splitBorder.minX, splitBorder.maxX, splitBorder.minY, basePoint.y)
        elif frontNormal.y == -1:
            return SplitBorder(splitBorder.minX, splitBorder.maxX, basePoint.y, splitBorder.maxY)
        elif frontNormal.x == 1:
            return SplitBorder(splitBorder.minX, basePoint.x, splitBorder.minY, splitBorder.maxY)
        elif frontNormal.x == -1:
            return SplitBorder(basePoint.x, splitBorder.maxX, splitBorder.minY, splitBorder.maxY)
        else:
            raise Exception()

    def getFrontAndBackWalls(self, walls, basePoint, frontNormal):
        frontWalls = []
        backWalls = []
        for wall in walls:
            position = self.getWallFrontBackPosition(wall, basePoint, frontNormal)
            if position == WallFrontBackPosition.frontBack:
                frontWalls.append(wall)
                backWalls.append(wall)
            elif position == WallFrontBackPosition.front:
                frontWalls.append(wall)
            elif position == WallFrontBackPosition.back:
                backWalls.append(wall)
            else:  # WallFrontBackPosition.parallel
                pass  # ignore this wall

        return (frontWalls, backWalls)

    def getWallFrontBackPosition(self, wall, basePoint, frontNormal):
        wallDirection = wall.startPosition.getCopy()
        wallDirection.sub(basePoint)
        dotProductStart = wallDirection.dotProduct(frontNormal)

        wallDirection = wall.endPosition.getCopy()
        wallDirection.sub(basePoint)
        dotProductEnd = wallDirection.dotProduct(frontNormal)

        front = dotProductStart > 0 or dotProductEnd > 0
        back = dotProductStart < 0 or dotProductEnd < 0

        if front and back:
            return WallFrontBackPosition.frontBack
        elif front:
            return WallFrontBackPosition.front
        elif back:
            return WallFrontBackPosition.back
        else:
            return WallFrontBackPosition.parallel

    def sortSplitWalls(self, splitWalls, splitOrientation):
        if splitOrientation == WallOrientation.vertical:
            splitWalls.sort(key=lambda w: w.startPosition.x)
        else:
            splitWalls.sort(key=lambda w: w.startPosition.y)


def makeBSPTreeBuilder(resolver):
    return BSPTreeBuilder()
