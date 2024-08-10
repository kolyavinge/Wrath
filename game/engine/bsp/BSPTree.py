class BSPNode:

    def __init__(self):
        self.front = None
        self.back = None
        self.basePoint = None
        self.frontNormal = None
        self.levelSegment = None
        self.isLeaf = False


class BSPTree:

    def __init__(self):
        self.root = BSPNode()

    def getAllLevelSegments(self):
        segments = []
        self.getAllLevelSegmentsRec(self.root, segments)

        return segments

    def getAllLevelSegmentsRec(self, node, segments):
        if node.isLeaf:
            segments.append(node.levelSegment)
        else:
            if node.front is not None:
                self.getAllLevelSegmentsRec(node.front, segments)
            if node.back is not None:
                self.getAllLevelSegmentsRec(node.back, segments)

    def getNodesForLevelSegment(self, levelSegment):
        nodes = []
        self.getNodesForLevelSegmentRec(self.root, levelSegment, nodes)

        return nodes

    def getNodesForLevelSegmentRec(self, node, levelSegment, nodes):
        if node is None:
            return False
        elif node.levelSegment == levelSegment:
            return True
        else:
            if self.getNodesForLevelSegmentRec(node.front, levelSegment, nodes) or self.getNodesForLevelSegmentRec(node.back, levelSegment, nodes):
                nodes.append(node)
                return True
            else:
                return False
