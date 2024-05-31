from game.calc.Vector3 import Vector3
from game.model.level.Wall import WallOrientation
from game.model.level.BSPTree import BSPNode
from game.model.level.LevelSegment import LevelSegment


class BSPTreeBuilder:

    def build(self, level):
        for floor in level.floors:
            maxX = self.getMaxX(floor.walls)
            maxY = self.getMaxY(floor.walls)
            self.buildRec(floor.bspTree.root, WallOrientation.vertical, 0, maxX, 0, maxY, floor.walls)

    def buildRec(self, parentNode, splitOrientation, minX, maxX, minY, maxY, walls):
        if parentNode is None:
            return

        splitWalls = [w for w in walls if w.orientation == splitOrientation]
        if not splitWalls:
            parentNode.levelSegment = LevelSegment(minX, maxX, minY, maxY)
            return

        self.sortSplitWalls(splitWalls, splitOrientation)
        middleWall = splitWalls[int(len(splitWalls) / 2)]
        walls.remove(middleWall)
        parentNode.basePoint = middleWall.startPosition
        parentNode.frontNormal = Vector3(1, 0, 0) if splitOrientation == WallOrientation.vertical else Vector3(0, 1, 0)
        backWalls, frontWalls = self.getBackAndFrontWalls(walls, parentNode.basePoint, parentNode.frontNormal)
        parentNode.back = BSPNode()
        parentNode.front = BSPNode()
        oppositeSplitOrientation = WallOrientation.getOpposite(splitOrientation)
        if splitOrientation == WallOrientation.vertical:
            self.buildRec(parentNode.back, oppositeSplitOrientation, minX, middleWall.startPosition.x, minY, maxY, backWalls)
            self.buildRec(parentNode.front, oppositeSplitOrientation, middleWall.startPosition.x, maxX, minY, maxY, frontWalls)
        else:
            self.buildRec(parentNode.back, oppositeSplitOrientation, minX, maxX, minY, middleWall.startPosition.y, backWalls)
            self.buildRec(parentNode.front, oppositeSplitOrientation, minX, maxX, middleWall.startPosition.y, maxY, frontWalls)

    def getBackAndFrontWalls(self, walls, basePoint, frontNormal):
        backWalls = []
        frontWalls = []
        for wall in walls:
            wallDirection = wall.startPosition.getCopy()
            wallDirection.sub(basePoint)
            if wallDirection.dotProduct(frontNormal) > 0:
                frontWalls.append(wall)
            else:
                wallDirection = wall.endPosition.getCopy()
                wallDirection.sub(basePoint)
                if wallDirection.dotProduct(frontNormal) > 0:
                    frontWalls.append(wall)
                else:
                    backWalls.append(wall)

        return (backWalls, frontWalls)

    def sortSplitWalls(self, splitWalls, splitOrientation):
        if splitOrientation == WallOrientation.vertical:
            splitWalls.sort(key=lambda w: w.startPosition.x)
        else:
            splitWalls.sort(key=lambda w: w.startPosition.y)

    def getMaxX(self, walls):
        return max([w.startPosition.x for w in walls] + [w.endPosition.x for w in walls])

    def getMaxY(self, walls):
        return max([w.startPosition.y for w in walls] + [w.endPosition.y for w in walls])
