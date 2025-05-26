class Vertex:

    def __init__(self, point, generationNumber):
        self.point = point
        self.generationNumber = generationNumber
        self.connectedVertices = []


class RouteGraph:

    def __init__(self):
        self.vertices = []
        self.verticesByPoints = {}

    def addVertex(self, vertex):
        self.vertices.append(vertex)
        self.verticesByPoints[vertex.point] = vertex

    def connectVertices(self, vertex1, vertex2):
        vertex1.connectedVertices.append(vertex2)
        vertex2.connectedVertices.append(vertex1)

    def getVertexWithPointOrNone(self, point):
        return self.verticesByPoints[point] if point in self.verticesByPoints else None
