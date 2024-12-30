from game.calc.Vector3 import Vector3
from game.model.level.Construction import Construction


class DoorwayBorderBuilder:

    def __init__(self, level):
        self.level = level

    def makeDoorwayBorder(self, frontNormal, doorwayEndPosition, doorway):
        doorwayStartPosition = doorway.startPosition
        doorwayWidthDirection = doorwayStartPosition.getDirectionTo(doorwayEndPosition)
        doorwayWidthDirection.setLength(doorway.width)
        borderWidthDirection = doorwayWidthDirection.copy()
        borderWidthDirection.setLength(doorway.border.width)
        borderDepthDirection = frontNormal.copy()
        borderDepthDirection.setLength(doorway.border.depth + 0.0001)

        left = Construction()
        left.downLeft = doorwayStartPosition.copy()
        left.downLeft.sub(borderWidthDirection)
        left.downRight = doorwayStartPosition.copy()
        left.upLeft = left.downLeft.copy()
        left.upLeft.z += doorway.height
        left.upRight = left.downRight.copy()
        left.upRight.z += doorway.height
        left.downLeft.add(borderDepthDirection)
        left.downRight.add(borderDepthDirection)
        left.upLeft.add(borderDepthDirection)
        left.upRight.add(borderDepthDirection)
        left.frontNormal = frontNormal
        left.material = doorway.border.frontMaterial
        left.defaultVisualSize = doorway.border.width
        self.level.addConstruction(left)

        right = Construction()
        right.downLeft = doorwayEndPosition.copy()
        right.downRight = doorwayEndPosition.copy()
        right.downRight.add(borderWidthDirection)
        right.upLeft = right.downLeft.copy()
        right.upLeft.z += doorway.height
        right.upRight = right.downRight.copy()
        right.upRight.z += doorway.height
        right.downLeft.add(borderDepthDirection)
        right.downRight.add(borderDepthDirection)
        right.upLeft.add(borderDepthDirection)
        right.upRight.add(borderDepthDirection)
        right.frontNormal = frontNormal
        right.material = doorway.border.frontMaterial
        right.defaultVisualSize = doorway.border.width
        self.level.addConstruction(right)

        top = Construction()
        top.downLeft = left.upLeft
        top.downRight = right.upRight
        top.upLeft = top.downLeft.copy()
        top.upLeft.z += doorway.border.width
        top.upRight = top.downRight.copy()
        top.upRight.z += doorway.border.width
        top.frontNormal = frontNormal
        top.material = doorway.border.frontMaterial
        self.level.addConstruction(top)

        outside = Construction()
        outside.downLeft = left.downLeft.copy()
        outside.downLeft.sub(borderDepthDirection)
        outside.downRight = left.downLeft.copy()
        outside.upLeft = top.upLeft.copy()
        outside.upLeft.sub(borderDepthDirection)
        outside.upRight = top.upLeft.copy()
        outside.frontNormal = doorwayEndPosition.getDirectionTo(doorwayStartPosition)
        outside.frontNormal.normalize()
        outside.material = doorway.border.frontMaterial
        outside.defaultVisualSize = doorway.border.depth
        self.level.addConstruction(outside)

        outside = Construction()
        outside.downLeft = right.downRight.copy()
        outside.downRight = right.downRight.copy()
        outside.downRight.sub(borderDepthDirection)
        outside.upLeft = top.upRight.copy()
        outside.upRight = top.upRight.copy()
        outside.upRight.sub(borderDepthDirection)
        outside.frontNormal = doorwayStartPosition.getDirectionTo(doorwayEndPosition)
        outside.frontNormal.normalize()
        outside.material = doorway.border.frontMaterial
        outside.defaultVisualSize = doorway.border.depth
        self.level.addConstruction(outside)

        inside = Construction()
        inside.downLeft = left.downRight.copy()
        inside.downRight = left.downRight.copy()
        inside.downRight.sub(borderDepthDirection)
        inside.upLeft = left.upRight.copy()
        inside.upRight = left.upRight.copy()
        inside.upRight.sub(borderDepthDirection)
        inside.frontNormal = doorwayStartPosition.getDirectionTo(doorwayEndPosition)
        inside.frontNormal.normalize()
        inside.material = doorway.border.frontMaterial
        inside.defaultVisualSize = doorway.border.depth
        self.level.addConstruction(inside)

        inside = Construction()
        inside.downLeft = right.downLeft.copy()
        inside.downLeft.sub(borderDepthDirection)
        inside.downRight = right.downLeft.copy()
        inside.upLeft = right.upLeft.copy()
        inside.upLeft.sub(borderDepthDirection)
        inside.upRight = right.upLeft.copy()
        inside.frontNormal = doorwayEndPosition.getDirectionTo(doorwayStartPosition)
        inside.frontNormal.normalize()
        inside.material = doorway.border.frontMaterial
        inside.defaultVisualSize = doorway.border.depth
        self.level.addConstruction(inside)

        inside = Construction()
        inside.downLeft = left.upRight.copy()
        inside.downLeft.sub(borderDepthDirection)
        inside.downRight = right.upLeft.copy()
        inside.downRight.sub(borderDepthDirection)
        inside.upLeft = left.upRight.copy()
        inside.upRight = right.upLeft.copy()
        inside.frontNormal = Vector3(0, 0, -1)
        inside.material = doorway.border.frontMaterial
        self.level.addConstruction(inside)

        outside = Construction()
        outside.downLeft = top.upLeft.copy()
        outside.downRight = top.upRight.copy()
        outside.upLeft = top.upLeft.copy()
        outside.upLeft.sub(borderDepthDirection)
        outside.upRight = top.upRight.copy()
        outside.upRight.sub(borderDepthDirection)
        outside.frontNormal = Vector3(0, 0, 1)
        outside.material = doorway.border.frontMaterial
        self.level.addConstruction(outside)
