from game.calc.Vector3 import Vector3


class BSPNode:

    def __init__(self):
        self.back = None
        self.front = None
        self.basePoint = None
        self.frontNormal = None
        self.levelSegment = None

    def isLeaf(self):
        return self.back == None and self.front == None


class BSPTree:

    def __init__(self):
        self.root = BSPNode()
