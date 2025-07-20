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
                    startPoint,
                    info.doorway.startPosition,
                    info.frontNormal,
                    info.height,
                    info.material,
                    info.bottomBorder,
                    info.topBorder,
                    info.visualSize,
                )
                doorwayEndPosition = self.getDoorwayEndPosition(startPoint, info.doorway)
                self.makeWallAboveDoorway(doorwayEndPosition, info)
                self.makeSolidWall(
                    doorwayEndPosition,
                    info.position,
                    info.frontNormal,
                    info.height,
                    info.material,
                    info.bottomBorder,
                    info.topBorder,
                    info.visualSize,
                )
                if info.doorway.border is not None:
                    self.doorwayBorderBuilder.makeDoorwayBorder(info.frontNormal, doorwayEndPosition, info.doorway)
            else:
                self.makeSolidWall(
                    startPoint, info.position, info.frontNormal, info.height, info.material, info.bottomBorder, info.topBorder, info.visualSize
                )

            startPoint = info.position

    def makeSolidWall(self, startPoint, endPoint, frontNormal, height, material, bottomBorder=None, topBorder=None, visualSize=2.0):
        if bottomBorder is not None:
            startPoint = startPoint.copy()
            endPoint = endPoint.copy()
            startPoint.z += bottomBorder.height
            endPoint.z += bottomBorder.height
            height -= bottomBorder.height

        if topBorder is not None:
            height -= topBorder.height

        wall = self.makeWall(startPoint, endPoint, frontNormal, height, material, visualSize)

        if bottomBorder is not None:
            self.makeBottomBorder(wall, bottomBorder)
            self.zFightingDelta += 0.0001

        if topBorder is not None:
            self.makeTopBorder(wall, topBorder)
            self.zFightingDelta += 0.0001

    def makeWall(self, startPoint, endPoint, frontNormal, height, material, visualSize):
        wall = Wall()
        wall.startPoint = startPoint.copy()
        wall.endPoint = endPoint.copy()
        wall.frontNormal = frontNormal
        wall.height = height
        wall.material = material
        wall.visualSize = visualSize
        self.level.addWall(wall)

        return wall

    def makeBottomBorder(self, wall, bottomBorder):
        depthDirection = wall.frontNormal.copy()
        depthDirection.setLength(bottomBorder.depth)

        front = Wall()
        front.startPoint = wall.startPoint.copy()
        front.endPoint = wall.endPoint.copy()
        front.startPoint.z -= bottomBorder.height
        front.endPoint.z -= bottomBorder.height
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
        top.downLeft.z += self.zFightingDelta
        top.downRight.z += self.zFightingDelta
        top.upLeft.z += self.zFightingDelta
        top.upRight.z += self.zFightingDelta
        top.upLeft.add(depthDirection)
        top.upRight.add(depthDirection)
        top.frontNormal = CommonConstants.zAxis
        top.material = bottomBorder.sideMaterial
        self.level.addConstruction(top)

    def makeTopBorder(self, wall, topBorder):
        depthDirection = wall.frontNormal.copy()
        depthDirection.setLength(topBorder.depth)

        front = Construction()
        front.downLeft = wall.upLeft.copy()
        front.downRight = wall.upRight.copy()
        front.upLeft = wall.upLeft.copy()
        front.upRight = wall.upRight.copy()
        front.upLeft.z += topBorder.height
        front.upRight.z += topBorder.height
        front.downLeft.add(depthDirection)
        front.downRight.add(depthDirection)
        front.upLeft.add(depthDirection)
        front.upRight.add(depthDirection)
        front.frontNormal = wall.frontNormal
        front.material = topBorder.frontMaterial
        self.level.addConstruction(front)

        bottom = Construction()
        bottom.downLeft = wall.upLeft.copy()
        bottom.downRight = wall.upRight.copy()
        bottom.upLeft = wall.upLeft.copy()
        bottom.upRight = wall.upRight.copy()
        bottom.downLeft.z -= self.zFightingDelta
        bottom.downRight.z -= self.zFightingDelta
        bottom.upLeft.z -= self.zFightingDelta
        bottom.upRight.z -= self.zFightingDelta
        bottom.upLeft.add(depthDirection)
        bottom.upRight.add(depthDirection)
        bottom.frontNormal = Vector3(0, 0, -1)
        bottom.material = topBorder.sideMaterial
        self.level.addConstruction(bottom)

    def getDoorwayEndPosition(self, startPoint, doorway):
        endPosition = startPoint.getDirectionTo(doorway.startPosition)
        endPosition.setLength(doorway.width)
        endPosition.add(doorway.startPosition)

        return endPosition

    def makeWallAboveDoorway(self, doorwayEndPosition, info):
        doorwayHeight = info.doorway.height
        doorwayBorderTopHeight = 0
        if info.doorway is not None and info.doorway.border is not None:
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
