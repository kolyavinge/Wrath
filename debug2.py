from game.model.level.Level import *
from game.model.level.Floor import *
from game.model.level.Wall import *
from game.engine.bsp.BSPTreeBuilder import *
from game.engine.bsp.BSPTreeTraversal import *

wall1 = Wall()
wall1.startPoint = Vector3(0, 10, 0)
wall1.endPoint = Vector3(0, 20, 0)
wall1.orientation = WallOrientation.vertical
wall1.frontNormal = Vector3(1, 0, 0)

wall2 = Wall()
wall2.startPoint = Vector3(0, 20, 0)
wall2.endPoint = Vector3(10, 20, 0)
wall2.orientation = WallOrientation.horizontal
wall2.frontNormal = Vector3(0, -1, 0)

wall3 = Wall()
wall3.startPoint = Vector3(10, 20, 0)
wall3.endPoint = Vector3(10, 30, 0)
wall3.orientation = WallOrientation.vertical
wall3.frontNormal = Vector3(1, 0, 0)

wall4 = Wall()
wall4.startPoint = Vector3(10, 30, 0)
wall4.endPoint = Vector3(20, 30, 0)
wall4.orientation = WallOrientation.horizontal
wall4.frontNormal = Vector3(0, -1, 0)

wall5 = Wall()
wall5.startPoint = Vector3(20, 30, 0)
wall5.endPoint = Vector3(20, 0, 0)
wall5.orientation = WallOrientation.vertical
wall5.frontNormal = Vector3(-1, 0, 0)

wall6 = Wall()
wall6.startPoint = Vector3(20, 0, 0)
wall6.endPoint = Vector3(10, 0, 0)
wall6.orientation = WallOrientation.horizontal
wall6.frontNormal = Vector3(0, 1, 0)

wall7 = Wall()
wall7.startPoint = Vector3(10, 0, 0)
wall7.endPoint = Vector3(10, 10, 0)
wall7.orientation = WallOrientation.vertical
wall7.frontNormal = Vector3(1, 0, 0)

wall8 = Wall()
wall8.startPoint = Vector3(10, 10, 0)
wall8.endPoint = Vector3(0, 10, 0)
wall8.orientation = WallOrientation.horizontal
wall8.frontNormal = Vector3(0, 1, 0)

floor = Floor()
floor.walls = [wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8]

level = Level()
level.floors = [floor]
level.validate()

bspTreeBuilder = BSPTreeBuilder()
bspTreeBuilder.build(level)
bspTree = level.floors[0].bspTree
root = bspTree.root

allSegments = bspTree.getAllLevelSegments()

bspTreeTraversal = BSPTreeTraversal()
segment = bspTreeTraversal.findLevelSegmentOrNone(bspTree, Vector3(1, 1, 0))

i = 1
