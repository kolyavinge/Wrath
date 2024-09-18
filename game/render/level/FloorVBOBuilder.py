from game.calc.Vector3 import Vector3


class FloorVBOBuilder:

    def build(self, floor, vboBuilder):
        leftDirectionLength = Vector3.getLengthBetween(floor.downLeft, floor.upLeft)
        rightDirectionLength = Vector3.getLengthBetween(floor.downRight, floor.upRight)
        stepLength = 10
        if leftDirectionLength > rightDirectionLength:
            leftStepLength = stepLength
            rightStepLength = stepLength * rightDirectionLength / leftDirectionLength
        elif rightDirectionLength > leftDirectionLength:
            leftStepLength = stepLength * leftDirectionLength / rightDirectionLength
            rightStepLength = stepLength
        else:
            leftStepLength = stepLength
            rightStepLength = stepLength

        leftPoints = Vector3.splitFromStartToEnd(floor.downLeft, floor.upLeft, leftStepLength)
        rightPoints = Vector3.splitFromStartToEnd(floor.downRight, floor.upRight, rightStepLength)
        assert len(leftPoints) == len(rightPoints)

        for i in range(1, len(leftPoints)):
            downPoints = Vector3.splitFromStartToEnd(leftPoints[i - 1], rightPoints[i - 1], stepLength)
            stepLength = Vector3.getLengthBetween(leftPoints[i], rightPoints[i]) / (len(downPoints) - 1)
            upPoints = Vector3.splitFromStartToEnd(leftPoints[i], rightPoints[i], stepLength)
            assert len(downPoints) == len(upPoints)
            for j in range(1, len(downPoints)):
                self.addVertices(vboBuilder, floor, downPoints[j - 1], downPoints[j], upPoints[j - 1], upPoints[j])

    def addVertices(self, vboBuilder, floor, downLeft, downRight, upLeft, upRight):
        vertexCount = vboBuilder.getVertexCount()

        vboBuilder.addVertex(downLeft)
        vboBuilder.addVertex(upLeft)
        vboBuilder.addVertex(downRight)
        vboBuilder.addVertex(upRight)

        vboBuilder.addNormal(floor.upNormal)
        vboBuilder.addNormal(floor.upNormal)
        vboBuilder.addNormal(floor.upNormal)
        vboBuilder.addNormal(floor.upNormal)

        vboBuilder.addTexCoord(0, 0)
        vboBuilder.addTexCoord(0, 1)
        vboBuilder.addTexCoord(1, 0)
        vboBuilder.addTexCoord(1, 1)

        vboBuilder.addFace(vertexCount, vertexCount + 3, vertexCount + 1)
        vboBuilder.addFace(vertexCount, vertexCount + 2, vertexCount + 3)


def makeFloorVBOBuilder(resolver):
    return FloorVBOBuilder()
