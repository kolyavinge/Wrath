import numpy


class AdjacencyFormatConverter:

    def __init__(self):
        self.maxUint32 = numpy.iinfo(numpy.uint32).max

    def getFacesWithAdjacency(self, faces):
        adjacency = []
        for i in range(0, 2 * len(faces)):
            adjacency.append(self.maxUint32)

        # Copy and make room for adjacency info
        for i in range(0, len(faces), 3):
            adjacency[i * 2 + 0] = faces[i]
            adjacency[i * 2 + 1] = self.maxUint32
            adjacency[i * 2 + 2] = faces[i + 1]
            adjacency[i * 2 + 3] = self.maxUint32
            adjacency[i * 2 + 4] = faces[i + 2]
            adjacency[i * 2 + 5] = self.maxUint32

        # Find matching edges
        for i in range(0, len(adjacency), 6):
            a1 = adjacency[i]
            b1 = adjacency[i + 2]
            c1 = adjacency[i + 4]

            # Scan subsequent triangles
            for j in range(i + 6, len(adjacency), 6):
                a2 = adjacency[j]
                b2 = adjacency[j + 2]
                c2 = adjacency[j + 4]

                # Edge 1 == Edge 1
                if (a1 == a2 and b1 == b2) or (a1 == b2 and b1 == a2):
                    adjacency[i + 1] = c2
                    adjacency[j + 1] = c1
                # Edge 1 == Edge 2
                if (a1 == b2 and b1 == c2) or (a1 == c2 and b1 == b2):
                    adjacency[i + 1] = a2
                    adjacency[j + 3] = c1
                # Edge 1 == Edge 3
                if (a1 == c2 and b1 == a2) or (a1 == a2 and b1 == c2):
                    adjacency[i + 1] = b2
                    adjacency[j + 5] = c1
                # Edge 2 == Edge 1
                if (b1 == a2 and c1 == b2) or (b1 == b2 and c1 == a2):
                    adjacency[i + 3] = c2
                    adjacency[j + 1] = a1
                # Edge 2 == Edge 2
                if (b1 == b2 and c1 == c2) or (b1 == c2 and c1 == b2):
                    adjacency[i + 3] = a2
                    adjacency[j + 3] = a1
                # Edge 2 == Edge 3
                if (b1 == c2 and c1 == a2) or (b1 == a2 and c1 == c2):
                    adjacency[i + 3] = b2
                    adjacency[j + 5] = a1
                # Edge 3 == Edge 1
                if (c1 == a2 and a1 == b2) or (c1 == b2 and a1 == a2):
                    adjacency[i + 5] = c2
                    adjacency[j + 1] = b1
                # Edge 3 == Edge 2
                if (c1 == b2 and a1 == c2) or (c1 == c2 and a1 == b2):
                    adjacency[i + 5] = a2
                    adjacency[j + 3] = b1
                # Edge 3 == Edge 3
                if (c1 == c2 and a1 == a2) or (c1 == a2 and a1 == c2):
                    adjacency[i + 5] = b2
                    adjacency[j + 5] = b1

        # Look for any outside edges
        for i in range(0, len(adjacency), 6):
            if adjacency[i + 1] == self.maxUint32:
                adjacency[i + 1] = adjacency[i + 4]

            if adjacency[i + 3] == self.maxUint32:
                adjacency[i + 3] = adjacency[i]

            if adjacency[i + 5] == self.maxUint32:
                adjacency[i + 5] = adjacency[i + 2]

        return adjacency
