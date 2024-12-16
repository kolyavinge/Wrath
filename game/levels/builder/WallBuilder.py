from game.anx.CommonConstants import CommonConstants
from game.calc.Vector3 import Vector3
from game.levels.builder.DoorwayBorderBuilder import DoorwayBorderBuilder
from game.model.level.Construction import Construction
from game.model.level.Wall import Wall


class WallBuilder:

    def __init__(self, level):
        self.level = level
        self.zFightingDelta = 0
        self.doorwayBorderBuilder = DoorwayBorderBuilder(level)

    def buildWalls(self, startPoint, *wallBuildInfoList):
        for info in wallBuildInfoList:
            if info.doorway is not None:
                self.makeSolidWall(
                    startPoint, info.doorway.startPosition, info.frontNormal, info.height, info.material, info.bottomBorder, info.topBorder
                )
                doorwayEndPosition = self.getDoorwayEndPosition(startPoint, info.doorway)
                self.makeWallAboveDoorway(doorwayEndPosition, info)
                self.makeSolidWall(doorwayEndPosition, info.position, info.frontNormal, info.height, info.material, info.bottomBorder, info.topBorder)
                self.doorwayBorderBuilder.makeDoorwayBorder(info.frontNormal, doorwayEndPosition, info.doorway)
            else:
                self.makeSolidWall(startPoint, info.position, info.frontNormal, info.height, info.material, info.bottomBorder, info.topBorder)

            startPoint = info.position

    def makeSolidWall(self, startPoint, endPoint, frontNormal, height, material, bottomBorder=None, topBorder=None):
        wall = self.makeWall(startPoint, endPoint, frontNormal, height, material)

        if bottomBorder is not None:
            self.makeBottomBorder(wall, bottomBorder)
            self.zFightingDelta += 0.001

        if topBorder is not None:
            self.makeTopBorder(wall, topBorder)
            self.zFightingDelta += 0.001

    def makeWall(self, startPoint, endPoint, frontNormal, height, material):
        wall = Wall()
        wall.startPoint = startPoint.copy()
        wall.endPoint = endPoint.copy()
        wall.frontNormal = frontNormal
        wall.height = height
        wall.material = material
        self.level.addWall(wall)

        return wall

    def makeBottomBorder(self, wall, bottomBorder):
        depthDirection = wall.frontNormal.copy()
        depthDirection.setLength(bottomBorder.depth)

        front = Wall()
        front.startPoint = wall.startPoint.copy()
        front.endPoint = wall.endPoint.copy()
        front.startPoint.add(depthDirection)
        front.endPoint.add(depthDirection)
        front.frontNormal = wall.frontNormal
        front.height = bottomBorder.height
        front.material = bottomBorder.frontMaterial
        self.level.addWall(front)

        top = Construction()
        top.downLeft = wall.downLeft.copy()
        top.downRight = wall.downRight.copy()
        top.upLeft = wall.downLeft.copy()
        top.upRight = wall.downRight.copy()
        top.downLeft.z += bottomBorder.height + self.zFightingDelta
        top.downRight.z += bottomBorder.height + self.zFightingDelta
        top.upLeft.z += bottomBorder.height + self.zFightingDelta
        top.upRight.z += bottomBorder.height + self.zFightingDelta
        top.upLeft.add(depthDirection)
        top.upRight.add(depthDirection)
        top.frontNormal = CommonConstants.zAxis
        top.material = bottomBorder.sideMaterial
        self.level.addConstruction(top)

        wall.startPoint.z += bottomBorder.height
        wall.endPoint.z += bottomBorder.height
        wall.height -= bottomBorder.height

    def makeTopBorder(self, wall, topBorder):
        depthDirection = wall.frontNormal.copy()
        depthDirection.setLength(topBorder.depth)

        front = Wall()
        front.startPoint = wall.upLeft.copy()
        front.endPoint = wall.upRight.copy()
        front.startPoint.add(depthDirection)
        front.endPoint.add(depthDirection)
        front.startPoint.z -= topBorder.height
        front.endPoint.z -= topBorder.height
        front.frontNormal = wall.frontNormal
        front.height = topBorder.height
        front.material = topBorder.frontMaterial
        self.level.addWall(front)

        bottom = Construction()
        bottom.downLeft = wall.upLeft.copy()
        bottom.downRight = wall.upRight.copy()
        bottom.upLeft = wall.upLeft.copy()
        bottom.upRight = wall.upRight.copy()
        bottom.downLeft.z -= topBorder.height - self.zFightingDelta
        bottom.downRight.z -= topBorder.height - self.zFightingDelta
        bottom.upLeft.z -= topBorder.height - self.zFightingDelta
        bottom.upRight.z -= topBorder.height - self.zFightingDelta
        bottom.upLeft.add(depthDirection)
        bottom.upRight.add(depthDirection)
        bottom.frontNormal = Vector3(0, 0, -1)
        bottom.material = topBorder.sideMaterial
        self.level.addConstruction(bottom)

        wall.height -= topBorder.height

    def getDoorwayEndPosition(self, startPoint, doorway):
        endPosition = startPoint.getDirectionTo(doorway.startPosition)
        endPosition.setLength(doorway.width)
        endPosition.add(doorway.startPosition)

        return endPosition

    def makeWallAboveDoorway(self, doorwayEndPosition, info):
        doorwayHeight = info.doorway.height
        doorwayBorderTopHeight = 0
        if info.doorway is not None:
            doorwayBorderTopHeight = info.doorway.border.width
        doorwayStartPosition = info.doorway.startPosition
        self.makeSolidWall(
            Vector3(doorwayStartPosition.x, doorwayStartPosition.y, doorwayStartPosition.z + doorwayHeight + doorwayBorderTopHeight),
            Vector3(doorwayEndPosition.x, doorwayEndPosition.y, doorwayEndPosition.z + doorwayHeight + doorwayBorderTopHeight),
            info.frontNormal,
            info.height - doorwayHeight - doorwayBorderTopHeight,
            info.doorway.topMaterial,
            None,
            info.topBorder,
        )