from game.engine.ai.common.RouteCollisionDetector import RouteCollisionDetector
from game.lib.List import List


class RouteOptimizer:

    def __init__(self, collisionDetector: RouteCollisionDetector):
        self.collisionDetector = collisionDetector

    def optimizeRoutePoints(self, routePoints):
        # пробуем распрямить отрезки маршрута
        # если они не попадают на препядствия
        middleIndex = int(len(routePoints) / 2)
        self.straighten(routePoints, 0, middleIndex)
        self.straighten(routePoints, middleIndex, len(routePoints) - 1)

        # начальную точку можно удалить. персонаж и так начнет с нее свое движение
        routePoints.remove(routePoints[0])

    def straighten(self, routePoints, startIndex, endIndex):
        if (endIndex - startIndex) < 4:  # короткий отрезок не обрабатываем
            return

        if self.collisionDetector.anyCollisions(routePoints[startIndex], routePoints[endIndex]):
            middleIndex = int((endIndex - startIndex) / 2 + startIndex)
            self.straighten(routePoints, startIndex, middleIndex)
            self.straighten(routePoints, middleIndex, endIndex)
        else:
            List.removeItemsBetween(routePoints, startIndex, endIndex)
