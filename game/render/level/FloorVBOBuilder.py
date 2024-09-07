from game.calc.Vector3Utils import Vector3Utils


class FloorVBOBuilder:

    def build(self, floor, vboBuilder):
        leftDirectionLength = floor.downLeft.getDirectionTo(floor.upLeft).getLength()
        rightDirectionLength = floor.downRight.getDirectionTo(floor.upRight).getLength()
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

        leftPoints = Vector3Utils.splitFromStartToEnd(floor.downLeft, floor.upLeft, leftStepLength)
        rightPoints = Vector3Utils.splitFromStartToEnd(floor.downRight, floor.upRight, rightStepLength)
        assert len(leftPoints) == len(rightPoints)

        for i in range(1, len(leftPoints)):
            downPoints = Vector3Utils.splitFromStartToEnd(leftPoints[i - 1], rightPoints[i - 1], stepLength)
            stepLength = leftPoints[i].getDirectionTo(rightPoints[i]).getLength() / (len(downPoints) - 1)
            upPoints = Vector3Utils.splitFromStartToEnd(leftPoints[i], rightPoints[i], stepLength)
            assert len(downPoints) == len(upPoints)
            for j in range(1, len(downPoints)):
                self.addVertices(vboBuilder, floor, downPoints[j - 1], downPoints[j], upPoints[j - 1], upPoints[j])

    def addVertices(self, vboBuilder, floor, downLeft, downRight, upLeft, upRight):
        vertexCount = vboBuilder.getVertexCount()

        vboBuilder.addVertex(downLeft)
        vboBuilder.addVertex(upLeft)
        vboBuilder.addVertex(upRight)
        vboBuilder.addVertex(downRight)

        vboBuilder.addNormal(floor.upNormal)
        vboBuilder.addNormal(floor.upNormal)
        vboBuilder.addNormal(floor.upNormal)
        vboBuilder.addNormal(floor.upNormal)

        vboBuilder.addTexCoord(0, 0)
        vboBuilder.addTexCoord(0, 1)
        vboBuilder.addTexCoord(1, 1)
        vboBuilder.addTexCoord(1, 0)

        vboBuilder.addFace(vertexCount, vertexCount + 1, vertexCount + 2)
        vboBuilder.addFace(vertexCount, vertexCount + 2, vertexCount + 3)


def makeFloorVBOBuilder(resolver):
    return FloorVBOBuilder()
