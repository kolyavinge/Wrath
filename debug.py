from game.model.level.Level import *
from game.model.level.Floor import *
from game.model.level.Wall import *
from game.engine.level.BSPTreeBuilder import *
from game.engine.level.BSPTreeTraversal import *

wall1 = Wall()
wall1.id = 3
wall1.startPosition = Vector3(0, 0, 0)
wall1.endPosition = Vector3(0, 10, 0)
wall1.orientation = WallOrientation.vertical
wall1.frontNormal = Vector3(1, 0, 0)

wall2 = Wall()
wall2.id = 2
wall2.startPosition = Vector3(0, 10, 0)
wall2.endPosition = Vector3(10, 10, 0)
wall2.orientation = WallOrientation.horizontal
wall2.frontNormal = Vector3(0, -1, 0)

wall3 = Wall()
wall3.id = 1
wall3.startPosition = Vector3(10, 10, 0)
wall3.endPosition = Vector3(10, 0, 0)
wall3.orientation = WallOrientation.vertical
wall3.frontNormal = Vector3(-1, 0, 0)

wall4 = Wall()
wall4.id = 4
wall4.startPosition = Vector3(0, 0, 0)
wall4.endPosition = Vector3(10, 0, 0)
wall4.orientation = WallOrientation.horizontal
wall4.frontNormal = Vector3(0, 1, 0)

floor = Floor()
floor.walls = [wall1, wall2, wall3, wall4]

level = Level()
level.floors = [floor]
level.validate()

bspTreeBuilder = BSPTreeBuilder()
bspTreeBuilder.build(level)
bspTree = level.floors[0].bspTree
root = bspTree.root

bspTreeTraversal = BSPTreeTraversal()
segment = bspTreeTraversal.findLevelSegmentOrNone(bspTree, Vector3(-5, 5, 0))
