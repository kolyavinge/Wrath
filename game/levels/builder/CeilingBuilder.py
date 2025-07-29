from game.calc.Vector3 import Vector3
from game.model.level.Ceiling import Ceiling
from game.model.level.Construction import Construction
from game.model.level.Floor import Floor


class CeilingHole:

    def __init__(self, xLength, yLength):
        self.xLength = xLength
        self.yLength = yLength


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

    def buildCeilingWithHole(self, downLeft, xLength, yLength, material, hole, edgeHeight=0.2):
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

        edge = Construction()
        edge.downLeft = left.downRight
        edge.downRight = left.upRight
        edge.upLeft = edge.downLeft.copy()
        edge.upRight = edge.downRight.copy()
        edge.upLeft.z += edgeHeight
        edge.upRight.z += edgeHeight
        edge.frontNormal = left.downLeft.getDirectionTo(left.downRight)
        edge.frontNormal.normalize()
        edge.material = material
        self.level.addConstruction(edge)

        edge = Construction()
        edge.downLeft = right.upLeft
        edge.downRight = right.downLeft
        edge.upLeft = edge.downLeft.copy()
        edge.upRight = edge.downRight.copy()
        edge.upLeft.z += edgeHeight
        edge.upRight.z += edgeHeight
        edge.frontNormal = right.downRight.getDirectionTo(right.downLeft)
        edge.frontNormal.normalize()
        edge.material = material
        self.level.addConstruction(edge)

        edge = Construction()
        edge.downLeft = left.downRight
        edge.downRight = right.downLeft
        edge.upLeft = edge.downLeft.copy()
        edge.upRight = edge.downRight.copy()
        edge.upLeft.z += edgeHeight
        edge.upRight.z += edgeHeight
        edge.frontNormal = left.downRight.getDirectionTo(left.upRight)
        edge.frontNormal.normalize()
        edge.material = material
        self.level.addConstruction(edge)

        edge = Construction()
        edge.downLeft = left.upRight
        edge.downRight = right.upLeft
        edge.upLeft = edge.downLeft.copy()
        edge.upRight = edge.downRight.copy()
        edge.upLeft.z += edgeHeight
        edge.upRight.z += edgeHeight
        edge.frontNormal = left.upRight.getDirectionTo(left.downRight)
        edge.frontNormal.normalize()
        edge.material = material
        self.level.addConstruction(edge)

        bottomFloor = Floor()
        bottomFloor.downLeft = bottom.downLeft.copy()
        bottomFloor.downRight = bottom.downRight.copy()
        bottomFloor.upLeft = bottom.upLeft.copy()
        bottomFloor.upRight = bottom.upRight.copy()
        bottomFloor.downLeft.z += edgeHeight
        bottomFloor.downRight.z += edgeHeight
        bottomFloor.upLeft.z += edgeHeight
        bottomFloor.upRight.z += edgeHeight
        bottomFloor.material = material
        self.level.addFloor(bottomFloor)

        topFloor = Floor()
        topFloor.downLeft = top.downLeft.copy()
        topFloor.downRight = top.downRight.copy()
        topFloor.upLeft = top.upLeft.copy()
        topFloor.upRight = top.upRight.copy()
        topFloor.downLeft.z += edgeHeight
        topFloor.downRight.z += edgeHeight
        topFloor.upLeft.z += edgeHeight
        topFloor.upRight.z += edgeHeight
        topFloor.material = material
        self.level.addFloor(topFloor)

        leftFloor = Floor()
        leftFloor.downLeft = left.downLeft.copy()
        leftFloor.downRight = left.downRight.copy()
        leftFloor.upLeft = left.upLeft.copy()
        leftFloor.upRight = left.upRight.copy()
        leftFloor.downLeft.z += edgeHeight
        leftFloor.downRight.z += edgeHeight
        leftFloor.upLeft.z += edgeHeight
        leftFloor.upRight.z += edgeHeight
        leftFloor.material = material
        self.level.addFloor(leftFloor)

        rightFloor = Floor()
        rightFloor.downLeft = right.downLeft.copy()
        rightFloor.downRight = right.downRight.copy()
        rightFloor.upLeft = right.upLeft.copy()
        rightFloor.upRight = right.upRight.copy()
        rightFloor.downLeft.z += edgeHeight
        rightFloor.downRight.z += edgeHeight
        rightFloor.upLeft.z += edgeHeight
        rightFloor.upRight.z += edgeHeight
        rightFloor.material = material
        self.level.addFloor(rightFloor)
