from game.anx.CommonConstants import CommonConstants
from game.calc.Geometry import Geometry
from game.lib.Math import Math


class LampVBOBuilder:

    def build(self, lamp, vboBuilder):
        basePoints, frontPoints, normals = lamp.getPoints()
        self.makeEdge(basePoints, frontPoints, normals, vboBuilder)
        self.makeTop(lamp.position, basePoints, frontPoints, lamp.frontNormal, vboBuilder)

    def makeEdge(self, basePoints, frontPoints, normals, vboBuilder):
        for i in range(0, len(basePoints) - 1):
            basePoint = basePoints[i]
            frontPoint = frontPoints[i]
            nextBasePoint = basePoints[i + 1]
            nextFrontPoint = frontPoints[i + 1]
            normal = normals[i]

            vertexCount = vboBuilder.getVertexCount()

            vboBuilder.addVertex(basePoint)
            vboBuilder.addVertex(frontPoint)
            vboBuilder.addVertex(nextBasePoint)
            vboBuilder.addVertex(nextFrontPoint)

            vboBuilder.addNormal(normal)
            vboBuilder.addNormal(normal)
            vboBuilder.addNormal(normal)
            vboBuilder.addNormal(normal)

            vboBuilder.addTexCoord(0, 0)
            vboBuilder.addTexCoord(0, 1)
            vboBuilder.addTexCoord(1, 0)
            vboBuilder.addTexCoord(1, 1)

            vboBuilder.addFace(vertexCount, vertexCount + 3, vertexCount + 1)
            vboBuilder.addFace(vertexCount, vertexCount + 2, vertexCount + 3)

    def makeTop(self, center, basePoints, frontPoints, frontNormal, vboBuilder):
        centerVertex = vboBuilder.getVertexCount()
        vboBuilder.addVertex(center)
        vboBuilder.addNormal(frontNormal)
        vboBuilder.addTexCoord(0.5, 0.5)

        texCoords = self.makeTopTexCoords(center, basePoints, frontNormal)

        for i in range(0, len(frontPoints) - 1):
            frontPoint = frontPoints[i]
            nextFrontPoint = frontPoints[i + 1]
            texCoordX, texCoordY = texCoords[i]
            nextTexCoordX, nextTexCoordY = texCoords[i + 1]

            vertexCount = vboBuilder.getVertexCount()

            vboBuilder.addVertex(frontPoint)
            vboBuilder.addVertex(nextFrontPoint)

            vboBuilder.addNormal(frontNormal)
            vboBuilder.addNormal(frontNormal)

            vboBuilder.addTexCoord(texCoordX, texCoordY)
            vboBuilder.addTexCoord(nextTexCoordX, nextTexCoordY)

            vboBuilder.addFace(centerVertex, vertexCount, vertexCount + 1)

    def makeTopTexCoords(self, center, basePoints, frontNormal):
        xaxis = center.getDirectionTo(basePoints[0])
        xaxis.normalize()
        yaxis = Geometry.rotatePoint(xaxis, frontNormal, CommonConstants.axisOrigin, Math.piHalf)
        yaxis.normalize()
        result = []
        for point in basePoints:
            radius = center.getDirectionTo(point)
            radius.setLength(0.5)
            texX = xaxis.dotProduct(radius) + 0.5
            texY = yaxis.dotProduct(radius) + 0.5
            result.append((texX, texY))

        return result
