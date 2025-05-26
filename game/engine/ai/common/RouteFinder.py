from game.calc.Vector3 import Vector3
from game.engine.ai.common.RouteCollisionDetector import RouteCollisionDetector
from game.engine.ai.common.RouteGraph import RouteGraph, Vertex
from game.engine.GameData import GameData
from game.lib.Query import Query
from game.model.ai.Route import Route


class RouteFinder:

    def __init__(
        self,
        gameData: GameData,
        collisionDetector: RouteCollisionDetector,
    ):
        self.gameData = gameData
        self.collisionDetector = collisionDetector
        self.stepLength = 3.0
        self.directions = [
            Vector3(0, self.stepLength, 0),
            Vector3(0, -self.stepLength, 0),
            Vector3(-self.stepLength, 0, 0),
            Vector3(self.stepLength, 0, 0),
        ]

    def getRoute(self, startPoint, endPoint):
        startVertex = Vertex(startPoint, 0)
        endVertex = Vertex(endPoint, None)
        self.calculateRouteGraph(startVertex, endVertex)
        route = self.collectRoute(startVertex, endVertex)

        return route

    def calculateRouteGraph(self, startVertex, endVertex):
        routeGraph = RouteGraph()
        routeGraph.addVertex(startVertex)
        routeGraph.addVertex(endVertex)
        endPoint = endVertex.point
        generationNumber = 1
        currentVertices = [startVertex]
        nextVertices = []

        while len(currentVertices) > 0:
            currentVertex = currentVertices.pop()
            if not self.collisionDetector.anyCollisions(currentVertex.point, endPoint):
                routeGraph.connectVertices(currentVertex, endVertex)
                return
            for direction in self.directions:
                nextPoint = currentVertex.point.copy()
                nextPoint.add(direction)
                if self.collisionDetector.anyCollisions(currentVertex.point, nextPoint):
                    continue
                if self.isEndPoint(nextPoint, endPoint):
                    routeGraph.connectVertices(currentVertex, endVertex)
                    return
                else:
                    nextVertex = routeGraph.getVertexWithPointOrNone(nextPoint)
                    if nextVertex is None:
                        nextVertex = Vertex(nextPoint, generationNumber)
                        routeGraph.addVertex(nextVertex)
                        nextVertices.append(nextVertex)
                    routeGraph.connectVertices(currentVertex, nextVertex)

            currentVertices = nextVertices
            nextVertices = []
            generationNumber += 1

    def collectRoute(self, startVertex, endVertex):
        route = Route()
        route.addPoint(endVertex.point)
        generationNumber = Query(endVertex.connectedVertices).min(lambda x: x.generationNumber)
        currentVertex = endVertex
        while currentVertex != startVertex:
            currentVertex = Query(currentVertex.connectedVertices).first(lambda x: x.generationNumber == generationNumber)
            route.addPointToStart(currentVertex.point)
            generationNumber -= 1

        return route

    def isEndPoint(self, point, endPoint):
        return point.getLengthTo(endPoint) <= self.stepLength
