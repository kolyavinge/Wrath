from game.calc.Vector3 import Vector3
from game.model.level.Ceiling import Ceiling


class CeilingHole:

    def __init__(self, xLength, yLength, material):
        self.xLength = xLength
        self.yLength = yLength
        self.material = material


class CeilingBuilder:

    def __init__(self, level):
        self.level = level

    def buildCeiling(self, downLeft, xLength, yLength, material, hole=None):
        if hole is not None:
            self.buildCeilingWithHole(downLeft, xLength, yLength, material, hole)
        else:
            self.buildFlatCeiling(downLeft, xLength, yLength, material)

    def buildFlatCeiling(self, downLeft, xLength, yLength, material):
        ceiling = Ceiling()
        ceiling.downLeft = downLeft
        ceiling.downRight = Vector3(downLeft.x + xLength, downLeft.y, downLeft.z)
        ceiling.upLeft = Vector3(downLeft.x, downLeft.y + yLength, downLeft.z)
        ceiling.upRight = Vector3(downLeft.x + xLength, downLeft.y + yLength, downLeft.z)
        ceiling.material = material
        self.level.addCeiling(ceiling)

    def buildCeilingWithHole(self, downLeft, xLength, yLength, material, hole):
        xLengthHalf = (xLength - hole.xLength) / 2
        yLengthHalf = (yLength - hole.yLength) / 2

        bottom = Ceiling()
        bottom.downLeft = downLeft
        bottom.downRight = Vector3(downLeft.x + xLength, downLeft.y, downLeft.z)
        bottom.upLeft = Vector3(downLeft.x, downLeft.y + yLengthHalf, downLeft.z)
        bottom.upRight = Vector3(downLeft.x + xLength, downLeft.y + yLengthHalf, downLeft.z)
        bottom.material = material
        self.level.addCeiling(bottom)

        top = Ceiling()
        top.downLeft = Vector3(downLeft.x, downLeft.y + yLengthHalf + hole.yLength, downLeft.z)
        top.downRight = Vector3(downLeft.x + xLength, downLeft.y + yLengthHalf + hole.yLength, downLeft.z)
        top.upLeft = Vector3(downLeft.x, downLeft.y + yLength, downLeft.z)
        top.upRight = Vector3(downLeft.x + xLength, downLeft.y + yLength, downLeft.z)
        top.material = material
        self.level.addCeiling(top)

        left = Ceiling()
        left.downLeft = Vector3(downLeft.x, downLeft.y + yLengthHalf, downLeft.z)
        left.downRight = Vector3(downLeft.x + xLengthHalf, downLeft.y + yLengthHalf, downLeft.z)
        left.upLeft = Vector3(downLeft.x, downLeft.y + yLengthHalf + hole.yLength, downLeft.z)
        left.upRight = Vector3(downLeft.x + xLengthHalf, downLeft.y + yLengthHalf + hole.yLength, downLeft.z)
        left.material = material
        self.level.addCeiling(left)

        right = Ceiling()
        right.downLeft = Vector3(downLeft.x + xLengthHalf + hole.xLength, downLeft.y + yLengthHalf, downLeft.z)
        right.downRight = Vector3(downLeft.x + xLength, downLeft.y + yLengthHalf, downLeft.z)
        right.upLeft = Vector3(downLeft.x + xLengthHalf + hole.xLength, downLeft.y + yLengthHalf + hole.yLength, downLeft.z)
        right.upRight = Vector3(downLeft.x + xLength, downLeft.y + yLengthHalf + hole.yLength, downLeft.z)
        right.material = material
        self.level.addCeiling(right)
