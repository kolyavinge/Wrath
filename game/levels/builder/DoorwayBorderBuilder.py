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
        outside.downLeft = doorwayStartPosition.copy()
        outside.downLeft.sub(borderWidthDirection)
        outside.downRight = doorwayStartPosition.copy()
        outside.downRight.sub(borderWidthDirection)
        outside.downRight.add(borderDepthDirection)
        outside.upLeft = outside.downLeft.copy()
        outside.upRight = outside.downRight.copy()
        outside.upLeft.z = top.upLeft.z
        outside.upRight.z = top.upRight.z
        outside.frontNormal = doorwayEndPosition.getDirectionTo(doorwayStartPosition)
        outside.frontNormal.normalize()
        outside.material = doorway.border.frontMaterial
        outside.defaultVisualSize = doorway.border.depth
        self.level.addConstruction(outside)

        outside = Construction()
        outside.downLeft = doorwayEndPosition.copy()
        outside.downLeft.add(borderWidthDirection)
        outside.downLeft.add(borderDepthDirection)
        outside.downRight = doorwayEndPosition.copy()
        outside.downRight.add(borderWidthDirection)
        outside.upLeft = outside.downLeft.copy()
        outside.upRight = outside.downRight.copy()
        outside.upLeft.z = top.upLeft.z
        outside.upRight.z = top.upRight.z
        outside.frontNormal = doorwayStartPosition.getDirectionTo(doorwayEndPosition)
        outside.frontNormal.normalize()
        outside.material = doorway.border.frontMaterial
        outside.defaultVisualSize = doorway.border.depth
        self.level.addConstruction(outside)

        inside = Construction()
        inside.downLeft = doorwayStartPosition.copy()
        inside.downLeft.add(borderDepthDirection)
        inside.downRight = doorwayStartPosition.copy()
        inside.upLeft = inside.downLeft.copy()
        inside.upRight = inside.downRight.copy()
        inside.upLeft.z = top.downLeft.z
        inside.upRight.z = top.downRight.z
        inside.frontNormal = doorwayStartPosition.getDirectionTo(doorwayEndPosition)
        inside.frontNormal.normalize()
        inside.material = doorway.border.frontMaterial
        inside.defaultVisualSize = doorway.border.depth
        self.level.addConstruction(inside)

        inside = Construction()
        inside.downLeft = doorwayEndPosition.copy()
        inside.downRight = doorwayEndPosition.copy()
        inside.downRight.add(borderDepthDirection)
        inside.upLeft = inside.downLeft.copy()
        inside.upRight = inside.downRight.copy()
        inside.upLeft.z = top.downLeft.z
        inside.upRight.z = top.downRight.z
        inside.frontNormal = doorwayEndPosition.getDirectionTo(doorwayStartPosition)
        inside.frontNormal.normalize()
        inside.material = doorway.border.frontMaterial
        inside.defaultVisualSize = doorway.border.depth
        self.level.addConstruction(inside)

        inside = Construction()
        inside.downLeft = doorwayStartPosition.copy()
        inside.downLeft.z += doorway.height
        inside.downRight = doorwayEndPosition.copy()
        inside.downRight.z += doorway.height
        inside.upLeft = inside.downLeft.copy()
        inside.upRight = inside.downRight.copy()
        inside.upLeft.add(borderDepthDirection)
        inside.upRight.add(borderDepthDirection)
        inside.frontNormal = Vector3(0, 0, -1)
        inside.material = doorway.border.frontMaterial
        self.level.addConstruction(inside)

        outside = Construction()
        outside.downLeft = doorwayStartPosition.copy()
        outside.downLeft.sub(borderWidthDirection)
        outside.downLeft.z = top.upLeft.z
        outside.downRight = doorwayEndPosition.copy()
        outside.downRight.add(borderWidthDirection)
        outside.downRight.z = top.upRight.z
        outside.upLeft = outside.downLeft.copy()
        outside.upRight = outside.downRight.copy()
        outside.upLeft.add(borderDepthDirection)
        outside.upRight.add(borderDepthDirection)
        outside.frontNormal = Vector3(0, 0, 1)
        outside.material = doorway.border.frontMaterial
        self.level.addConstruction(outside)
