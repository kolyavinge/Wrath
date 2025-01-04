from game.calc.Vector3 import Vector3
from game.lib.Math import Math


class ConstructionVBOBuilder:

    def build(self, item, vboBuilder):
        if item.visualSize is not None:
            self.buildSplitted(item, vboBuilder)
        else:
            self.addVertices(vboBuilder, item, item.downLeft, item.downRight, item.upLeft, item.upRight)

    def buildSplitted(self, item, vboBuilder):
        leftDirectionLength = item.frontDownLeft.getLengthTo(item.frontUpLeft)
        rightDirectionLength = item.frontDownRight.getLengthTo(item.frontUpRight)
        stepLength = item.visualSize
        if leftDirectionLength > rightDirectionLength:
            leftStepLength = stepLength
            rightStepLength = stepLength * rightDirectionLength / leftDirectionLength
        elif rightDirectionLength > leftDirectionLength:
            leftStepLength = stepLength * leftDirectionLength / rightDirectionLength
            rightStepLength = stepLength
        else:
            leftStepLength = Math.min(leftDirectionLength, stepLength)
            rightStepLength = Math.min(rightDirectionLength, stepLength)

        leftPoints = Vector3.splitFromStartToEnd(item.frontDownLeft, item.frontUpLeft, leftStepLength)
        rightPoints = Vector3.splitFromStartToEnd(item.frontDownRight, item.frontUpRight, rightStepLength)
        assert len(leftPoints) == len(rightPoints)

        for i in range(1, len(leftPoints)):
            downPoints = Vector3.splitFromStartToEnd(leftPoints[i - 1], rightPoints[i - 1], stepLength)
            assert len(downPoints) > 1
            stepLength = leftPoints[i].getLengthTo(rightPoints[i]) / (len(downPoints) - 1)
            upPoints = Vector3.splitFromStartToEnd(leftPoints[i], rightPoints[i], stepLength)
            assert len(downPoints) == len(upPoints)
            for j in range(1, len(downPoints)):
                self.addVertices(vboBuilder, item, downPoints[j - 1], downPoints[j], upPoints[j - 1], upPoints[j])

    def addVertices(self, vboBuilder, item, downLeft, downRight, upLeft, upRight):
        vertexCount = vboBuilder.getVertexCount()

        vboBuilder.addVertex(downLeft)
        vboBuilder.addVertex(upLeft)
        vboBuilder.addVertex(downRight)
        vboBuilder.addVertex(upRight)

        vboBuilder.addNormal(item.frontNormal)
        vboBuilder.addNormal(item.frontNormal)
        vboBuilder.addNormal(item.frontNormal)
        vboBuilder.addNormal(item.frontNormal)

        vboBuilder.addTexCoord(0, 0)
        vboBuilder.addTexCoord(0, 1)
        vboBuilder.addTexCoord(1, 0)
        vboBuilder.addTexCoord(1, 1)

        vboBuilder.addFace(vertexCount, vertexCount + 3, vertexCount + 1)
        vboBuilder.addFace(vertexCount, vertexCount + 2, vertexCount + 3)


def makeConstructionVBOBuilder(resolver):
    return ConstructionVBOBuilder()
