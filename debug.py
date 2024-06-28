import time

from game.engine.bsp.BSPTreeBuilder import *
from game.engine.bsp.BSPTreeTraversal import *
from game.model.level.Level import *
from game.model.level.Wall import *

wall1 = Wall()
wall1.startPoint = Vector3(0, 0, 0)
wall1.endPoint = Vector3(0, 10, 0)
wall1.orientation = Orientation.vertical
wall1.frontNormal = Vector3(1, 0, 0)

wall2 = Wall()
wall2.startPoint = Vector3(0, 10, 0)
wall2.endPoint = Vector3(20, 10, 0)
wall2.orientation = Orientation.horizontal
wall2.frontNormal = Vector3(0, -1, 0)

wall3 = Wall()
wall3.startPoint = Vector3(20, 10, 0)
wall3.endPoint = Vector3(20, 15, 0)
wall3.orientation = Orientation.vertical
wall3.frontNormal = Vector3(1, 0, 0)

wall4 = Wall()
wall4.startPoint = Vector3(20, 15, 0)
wall4.endPoint = Vector3(30, 15, 0)
wall4.orientation = Orientation.horizontal
wall4.frontNormal = Vector3(0, -1, 0)

wall5 = Wall()
wall5.startPoint = Vector3(30, 15, 0)
wall5.endPoint = Vector3(30, 5, 0)
wall5.orientation = Orientation.vertical
wall5.frontNormal = Vector3(-1, 0, 0)

wall6 = Wall()
wall6.startPoint = Vector3(30, 5, 0)
wall6.endPoint = Vector3(10, 5, 0)
wall6.orientation = Orientation.horizontal
wall6.frontNormal = Vector3(0, 1, 0)

wall7 = Wall()
wall7.startPoint = Vector3(10, 5, 0)
wall7.endPoint = Vector3(10, 0, 0)
wall7.orientation = Orientation.vertical
wall7.frontNormal = Vector3(-1, 0, 0)

wall8 = Wall()
wall8.startPoint = Vector3(10, 0, 0)
wall8.endPoint = Vector3(0, 0, 0)
wall8.orientation = Orientation.horizontal
wall8.frontNormal = Vector3(0, 1, 0)

level = Level()
level.walls = [wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8]
level.validate()

bspTreeBuilder = BSPTreeBuilder()
bspTreeBuilder.build(level)
bspTree = level.collisionTree
root = bspTree.root

allSegments = bspTree.getAllLevelSegments()

bspTreeTraversal = BSPTreeTraversal()
segment = bspTreeTraversal.findLevelSegmentOrNone(bspTree, Vector3(1, 1, 0))

# start = time.time()
# n = 0
# while n < 100000:
#     segment = bspTreeTraversal.findLevelSegmentOrNone(bspTree, Vector3(1, 1, 0))
#     n += 1
# end = time.time()
# print(f"Time {end-start} seconds")

i = 1
