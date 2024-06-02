from game.model.level.Wall import WallOrientation
from game.model.level.BSPTree import BSPNode
from game.model.level.LevelSegment import LevelSegment


class SplitBorder:

    def __init__(self, minX, maxX, minY, maxY):
        self.minX = minX
        self.maxX = maxX
        self.minY = minY
        self.maxY = maxY


class BSPTreeBuilder:

    def build(self, level):
        for floor in level.floors:
            maxX = max([w.getMaxX() for w in floor.walls])
            maxY = max([w.getMaxY() for w in floor.walls])
            splitBorder = SplitBorder(0, maxX, 0, maxY)
            self.buildRec(floor.bspTree.root, WallOrientation.vertical, splitBorder, floor.walls)

    def buildRec(self, parentNode, splitOrientation, splitBorder, walls):
        if not walls:
            parentNode.levelSegment = LevelSegment(splitBorder.minX, splitBorder.maxX, splitBorder.minY, splitBorder.maxY)
            return
        splitWalls = [w for w in walls if w.orientation == splitOrientation]
        self.sortSplitWalls(splitWalls, splitOrientation)
        middleWall = splitWalls[int(len(splitWalls) / 2)]
        print(middleWall.id)
        walls.remove(middleWall)
        parentNode.basePoint = middleWall.startPosition
        parentNode.frontNormal = middleWall.frontNormal
        backWalls, frontWalls = self.getBackAndFrontWalls(walls, parentNode.basePoint, parentNode.frontNormal)
        oppositeSplitOrientation = WallOrientation.getOpposite(splitOrientation)
        parentNode.front = BSPNode()
        splitBorder = self.getFrontSplitBorder(splitBorder, parentNode.basePoint, parentNode.frontNormal)
        self.buildRec(parentNode.front, oppositeSplitOrientation, splitBorder, frontWalls)
        if backWalls:
            parentNode.back = BSPNode()
            splitBorder = self.getBackSplitBorder(splitBorder, parentNode.basePoint, parentNode.frontNormal)
            self.buildRec(parentNode.back, oppositeSplitOrientation, splitBorder, backWalls)

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

    def getBackAndFrontWalls(self, walls, basePoint, frontNormal):
        backWalls = []
        frontWalls = []
        for wall in walls:
            if self.isWallInFront(wall, basePoint, frontNormal):
                frontWalls.append(wall)
            else:
                backWalls.append(wall)

        return (backWalls, frontWalls)

    def isWallInFront(self, wall, basePoint, frontNormal):
        wallDirection = wall.startPosition.getCopy()
        wallDirection.sub(basePoint)
        if wallDirection.dotProduct(frontNormal) > 0:
            return True

        wallDirection = wall.endPosition.getCopy()
        wallDirection.sub(basePoint)
        if wallDirection.dotProduct(frontNormal) > 0:
            return True

    def sortSplitWalls(self, splitWalls, splitOrientation):
        if splitOrientation == WallOrientation.vertical:
            splitWalls.sort(key=lambda w: w.startPosition.x)
        else:
            splitWalls.sort(key=lambda w: w.startPosition.y)


def makeBSPTreeBuilder(resolver):
    return BSPTreeBuilder()
