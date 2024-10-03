class StairVBOBuilder:

    def build(self, stair, vboBuilder):
        for stepNumber in range(0, stair.stepsCount):
            frontFacePoints, topFacePoints = stair.getFrontAndTopFacePoints(stepNumber)
            self.addFrontFaceVertices(vboBuilder, stair, frontFacePoints)
            self.addTopFaceVertices(vboBuilder, stair, topFacePoints)

    def addFrontFaceVertices(self, vboBuilder, item, frontFacePoints):
        downLeft, downRight, upLeft, upRight = frontFacePoints
        vertexCount = vboBuilder.getVertexCount()

        self.addVertices(vboBuilder, downLeft, downRight, upLeft, upRight)

        vboBuilder.addNormal(item.frontNormal)
        vboBuilder.addNormal(item.frontNormal)
        vboBuilder.addNormal(item.frontNormal)
        vboBuilder.addNormal(item.frontNormal)

        vboBuilder.addTexCoord(0.0, 0.0)
        vboBuilder.addTexCoord(0.0, 0.5)
        vboBuilder.addTexCoord(1.0, 0.0)
        vboBuilder.addTexCoord(1.0, 0.5)

        self.addFaces(vboBuilder, vertexCount)

    def addTopFaceVertices(self, vboBuilder, item, topFacePoints):
        downLeft, downRight, upLeft, upRight = topFacePoints
        vertexCount = vboBuilder.getVertexCount()

        self.addVertices(vboBuilder, downLeft, downRight, upLeft, upRight)

        vboBuilder.addNormal(item.topNormal)
        vboBuilder.addNormal(item.topNormal)
        vboBuilder.addNormal(item.topNormal)
        vboBuilder.addNormal(item.topNormal)

        vboBuilder.addTexCoord(0.0, 0.5)
        vboBuilder.addTexCoord(0.0, 1.0)
        vboBuilder.addTexCoord(1.0, 0.5)
        vboBuilder.addTexCoord(1.0, 1.0)

        self.addFaces(vboBuilder, vertexCount)

    def addVertices(self, vboBuilder, downLeft, downRight, upLeft, upRight):
        vboBuilder.addVertex(downLeft)
        vboBuilder.addVertex(upLeft)
        vboBuilder.addVertex(downRight)
        vboBuilder.addVertex(upRight)

    def addFaces(self, vboBuilder, vertexCount):
        vboBuilder.addFace(vertexCount, vertexCount + 3, vertexCount + 1)
        vboBuilder.addFace(vertexCount, vertexCount + 2, vertexCount + 3)


def makeStairVBOBuilder(resolver):
    return StairVBOBuilder()
