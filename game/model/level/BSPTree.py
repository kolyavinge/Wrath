from game.calc.Vector3 import Vector3


class BSPNode:

    def __init__(self):
        self.back = None
        self.front = None
        self.basePoint = None
        self.frontNormal = None
        self.levelSegment = None

    def isLeaf(self):
        return self.back is None and self.front is None


class BSPTree:

    def __init__(self):
        self.root = BSPNode()

    def getAllLevelSegments(self):
        segments = []
        self.getAllLevelSegmentsRec(self.root, segments)

        return segments

    def getAllLevelSegmentsRec(self, node, segments):
        if node.isLeaf():
            segments.append(node.levelSegment)
        else:
            self.getAllLevelSegmentsRec(node.back, segments)
            self.getAllLevelSegmentsRec(node.front, segments)
