class Face:

    def __init__(self, i1, i2, i3):
        self.i1 = i1
        self.i2 = i2
        self.i3 = i3


class Mesh:

    def __init__(self):
        self.vertices = []
        self.normals = []
        self.texCoords = []
        self.faces = []
        self.mainTexture = None

    def addVertex(self, vector):
        self.vertices.append(vector)

    def addNormal(self, vector):
        self.normals.append(vector)

    def addTexCoord(self, point):
        self.texCoords.append(point)

    def addFace(self, face):
        self.faces.append(face)

    def flipYZ(self):
        for vertex in self.vertices:
            t = vertex.y
            vertex.y = vertex.z
            vertex.z = t

        for normal in self.normals:
            t = normal.y
            normal.y = normal.z
            normal.z = t

    def mulAxes(self, x, y, z):
        for vertex in self.vertices:
            vertex.x *= x
            vertex.y *= y
            vertex.z *= z

        for normal in self.normals:
            normal.x *= x
            normal.y *= y
            normal.z *= z

    def centerBy(self, axes):
        x0 = 0
        y0 = 0
        z0 = 0

        if "x" in axes:
            minx = min([v.x for v in self.vertices])
            maxx = max([v.x for v in self.vertices])
            x0 = (maxx - minx) / 2 + minx

        if "y" in axes:
            miny = min([v.y for v in self.vertices])
            maxy = max([v.y for v in self.vertices])
            y0 = (maxy - miny) / 2 + miny

        if "z" in axes:
            minz = min([v.z for v in self.vertices])
            maxz = max([v.z for v in self.vertices])
            z0 = (maxz - minz) / 2 + minz

        for v in self.vertices:
            v.x -= x0
            v.y -= y0
            v.z -= z0
