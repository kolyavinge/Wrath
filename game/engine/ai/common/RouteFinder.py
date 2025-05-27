from game.calc.Vector3 import Vector3
from game.engine.ai.common.RouteCollisionDetector import RouteCollisionDetector
from game.engine.ai.common.RouteGraph import RouteGraph, Vertex
from game.engine.ai.common.RouteOptimizer import RouteOptimizer
from game.lib.Query import Query
from game.model.ai.Route import NullRoute, Route


class RouteFinder:

    def __init__(
        self,
        collisionDetector: RouteCollisionDetector,
        routeOptimizer: RouteOptimizer,
    ):
        self.collisionDetector = collisionDetector
        self.routeOptimizer = routeOptimizer
        self.stepLength = 2.0
        self.availableDirections = [
            Vector3(0, self.stepLength, 0),
            Vector3(0, -self.stepLength, 0),
            Vector3(-self.stepLength, 0, 0),
            Vector3(self.stepLength, 0, 0),
        ]

    def getRoute(self, startPoint, endPoint):
        if not self.collisionDetector.anyCollisions(startPoint, endPoint):
            return Route([endPoint])
        else:
            startVertex = Vertex(startPoint, 0)
            endVertex = Vertex(endPoint, None)
            route = NullRoute.instance
            if self.calculateRouteGraph(startVertex, endVertex):
                routePoints = self.getRoutePoints(startVertex, endVertex)
                self.routeOptimizer.optimizeRoutePoints(routePoints)
                route = Route(routePoints)

            return route

    def calculateRouteGraph(self, startVertex, endVertex):
        # поиск в ширину
        # идем во всех доступных направлениях из каждой точки
        # проверяем точки на соударение с препятствиями
        # как только дошли до конечной точки - заканчиваем поиск

        routeGraph = RouteGraph()
        routeGraph.addVertex(startVertex)
        routeGraph.addVertex(endVertex)
        endPoint = endVertex.point
        generationNumber = startVertex.generationNumber + 1
        currentVertices = [startVertex]
        nextVertices = []

        while len(currentVertices) > 0:
            currentVertex = currentVertices.pop()
            for direction in self.availableDirections:
                nextPoint = currentVertex.point.copy()
                nextPoint.add(direction)
                if self.collisionDetector.anyCollisions(currentVertex.point, nextPoint):
                    continue
                if self.isEndPoint(nextPoint, endPoint):
                    endVertex.generationNumber = generationNumber
                    routeGraph.connectVertices(currentVertex, endVertex)
                    return True
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

        return False

    def getRoutePoints(self, startVertex, endVertex):
        # собираем маршрут от конечной точки к начальной
        assert endVertex.generationNumber is not None
        routePoints = [endVertex.point]
        currentVertex = endVertex
        while currentVertex != startVertex:
            currentVertex = Query(currentVertex.connectedVertices).orderBy(lambda x: x.generationNumber).first()
            routePoints.insert(0, currentVertex.point)

        return routePoints

    def isEndPoint(self, point, endPoint):
        return point.getLengthTo(endPoint) <= self.stepLength
