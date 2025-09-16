from game.calc.Vector3 import Vector3


class BSPTreeNode:

    def __init__(self):
        self.items = []
        self.basePoint = None
        self.frontNormal = None
        self.leftNode = None
        self.rightNode = None
        self.isLeaf = False


class SplitPlane:

    def __init__(self, basePoint, frontNormal):
        self.basePoint = basePoint
        self.frontNormal = frontNormal


class BSPTree:

    def __init__(self, items, getPointFunc, splitPlanes):
        self.getPointFunc = getPointFunc

        def build(parent, splitPlanes):
            if len(splitPlanes) == 0:
                parent.isLeaf = True
                return

            splitPlane = splitPlanes[0]
            splitPlanes.remove(splitPlane)
            leftNodeSplitPlanes = []
            rightNodeSplitPlanes = []

            parent.basePoint = splitPlane.basePoint
            parent.frontNormal = splitPlane.frontNormal
            parent.leftNode = BSPTreeNode()
            parent.rightNode = BSPTreeNode()

            for item in parent.items:
                point = self.getPointFunc(item)
                dotProduct = Vector3.calcDirectionAndGetDotProduct(parent.basePoint, point, parent.frontNormal)
                if dotProduct >= 0:
                    parent.rightNode.items.append(item)
                else:
                    parent.leftNode.items.append(item)

            for splitPlane in splitPlanes:
                dotProduct = Vector3.calcDirectionAndGetDotProduct(parent.basePoint, splitPlane.basePoint, parent.frontNormal)
                if dotProduct > 0:
                    rightNodeSplitPlanes.append(splitPlane)
                elif dotProduct < 0:
                    leftNodeSplitPlanes.append(splitPlane)
                else:
                    raise Exception("Wrong split plane position.")

            build(parent.leftNode, leftNodeSplitPlanes)
            build(parent.rightNode, rightNodeSplitPlanes)

        self.root = BSPTreeNode()
        self.root.items = items
        build(self.root, splitPlanes.copy())

    def findNodeItemsByPoint(self, point):

        def findNode(parent, point):
            if parent.isLeaf:
                return parent
            else:
                dotProduct = Vector3.calcDirectionAndGetDotProduct(parent.basePoint, point, parent.frontNormal)
                if dotProduct >= 0:
                    return findNode(parent.rightNode, point)
                else:
                    return findNode(parent.leftNode, point)

        return findNode(self.root, point).items
