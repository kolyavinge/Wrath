from game.anx.CommonConstants import CommonConstants
from game.calc.Geometry import Geometry
from game.calc.Vector3 import Vector3
from game.engine.bsp.SplitPlane import SplitPlane
from game.lib.Math import Math
from game.model.level.Ceiling import Ceiling
from game.model.level.Floor import Floor
from game.model.level.Level import Level
from game.model.level.LevelSegmentJoinLine import LevelSegmentJoinLine
from game.model.level.PowerupArea import PowerupArea
from game.model.level.Stair import Stair
from game.model.level.Wall import Wall
from game.model.light.Lamp import Lamp
from game.model.light.Spot import Spot
from game.model.Material import Material
from game.model.Orientation import Orientation


class TestLevel(Level):

    def __init__(self):
        super().__init__()
        self.makeRoom1()
        self.makeRoom2()
        self.makeRoom3()
        self.makePass1()
        self.makePass2()
        self.makePass3()
        self.makePass4()
        self.makePass5()
        self.makeJoinLines()
        self.makePowerupAreas()
        self.setPlayerPosition()

    def makeRoom1(self):
        secondFloorHeight = 0.8
        wallHeight = 8 - secondFloorHeight
        z = 0

        wall = Wall()
        wall.startPoint = Vector3(70, 30, z)
        wall.endPoint = Vector3(70, 40, z)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(1, 0, 0)
        wall.height = wallHeight
        wall.material = Material.wallMetal1
        wall.canCastShadow = True
        wall.info = "room 1"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(70, 30, z)
        wall.endPoint = Vector3(90, 10, z)
        wall.orientation = Orientation.diagonal
        wall.frontNormal = Vector3(1, 1, 0)
        wall.frontNormal.normalize()
        wall.height = wallHeight
        wall.material = Material.wallMetal1
        wall.info = "room 1"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(90, 10, z)
        wall.endPoint = Vector3(100, 10, z)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, 1, 0)
        wall.height = wallHeight
        wall.material = Material.wallMetal1
        wall.info = "room 1"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(100, 10, z)
        wall.endPoint = Vector3(120, 10, z)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, 1, 0)
        wall.height = wallHeight
        wall.material = Material.wallMetal1
        wall.info = "room 1"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(120, 10, z)
        wall.endPoint = Vector3(130, 10, z)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, 1, 0)
        wall.height = wallHeight
        wall.material = Material.wallMetal1
        wall.info = "room 1"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(130, 10, z)
        wall.endPoint = Vector3(150, 30, z)
        wall.orientation = Orientation.diagonal
        wall.frontNormal = Vector3(-1, 1, 0)
        wall.frontNormal.normalize()
        wall.height = wallHeight
        wall.material = Material.wallMetal1
        wall.info = "room 1"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(150, 30, z)
        wall.endPoint = Vector3(150, 40, z)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(-1, 0, 0)
        wall.height = wallHeight
        wall.material = Material.wallMetal1
        wall.canCastShadow = True
        wall.info = "room 1"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(150, 40, 4)
        wall.endPoint = Vector3(150, 50, 4)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(-1, 0, 0)
        wall.height = wallHeight - 4
        wall.material = Material.wallMetal8
        wall.canCastShadow = True
        wall.info = "room 1"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(150, 50, z)
        wall.endPoint = Vector3(150, 60, z)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(-1, 0, 0)
        wall.height = wallHeight
        wall.material = Material.wallMetal1
        wall.canCastShadow = True
        wall.info = "room 1"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(130, 80, z)
        wall.endPoint = Vector3(150, 60, z)
        wall.orientation = Orientation.diagonal
        wall.frontNormal = Vector3(-1, -1, 0)
        wall.frontNormal.normalize()
        wall.height = wallHeight
        wall.material = Material.wallMetal1
        wall.info = "room 1"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(110, 80, z)
        wall.endPoint = Vector3(130, 80, z)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, -1, 0)
        wall.height = wallHeight
        wall.material = Material.wallMetal1
        wall.canCastShadow = True
        wall.info = "room 1"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(100, 80, 4)
        wall.endPoint = Vector3(110, 80, 4)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, -1, 0)
        wall.height = wallHeight - 4
        wall.material = Material.wallMetal8
        wall.canCastShadow = True
        wall.info = "room 1"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(90, 80, z)
        wall.endPoint = Vector3(100, 80, z)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, -1, 0)
        wall.height = wallHeight
        wall.material = Material.wallMetal1
        wall.canCastShadow = True
        wall.info = "room 1"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(70, 60, z)
        wall.endPoint = Vector3(90, 80, z)
        wall.orientation = Orientation.diagonal
        wall.frontNormal = Vector3(1, -1, 0)
        wall.frontNormal.normalize()
        wall.height = wallHeight
        wall.material = Material.wallMetal1
        wall.info = "room 1"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(70, 40, z)
        wall.endPoint = Vector3(70, 50, z)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(1, 0, 0)
        wall.height = wallHeight
        wall.material = Material.wallMetal1
        wall.canCastShadow = True
        wall.info = "room 1"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(70, 50, z)
        wall.endPoint = Vector3(70, 60, z)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(1, 0, 0)
        wall.height = wallHeight
        wall.material = Material.wallMetal1
        wall.canCastShadow = True
        wall.info = "room 1"
        self.addWall(wall)

        # pole 1

        wall = Wall()
        wall.startPoint = Vector3(92, 32, z)
        wall.endPoint = Vector3(98, 32, z)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, -1, 0)
        wall.height = 12
        wall.material = Material.wallMetal6
        wall.canCastShadow = True
        wall.info = "room 1"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(92, 32, z)
        wall.endPoint = Vector3(92, 38, z)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(-1, 0, 0)
        wall.height = 12
        wall.material = Material.wallMetal6
        wall.canCastShadow = True
        wall.info = "room 1"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(92, 38, z)
        wall.endPoint = Vector3(98, 38, z)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, 1, 0)
        wall.height = 12
        wall.material = Material.wallMetal6
        wall.canCastShadow = True
        wall.info = "room 1"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(98, 32, z)
        wall.endPoint = Vector3(98, 38, z)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(1, 0, 0)
        wall.height = 12
        wall.material = Material.wallMetal6
        wall.canCastShadow = True
        wall.info = "room 1"
        self.addWall(wall)

        # pole 2

        wall = Wall()
        wall.startPoint = Vector3(122, 52, z)
        wall.endPoint = Vector3(128, 52, z)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, -1, 0)
        wall.height = 12
        wall.material = Material.wallMetal6
        wall.canCastShadow = True
        wall.info = "room 1"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(122, 52, z)
        wall.endPoint = Vector3(122, 58, z)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(-1, 0, 0)
        wall.height = 12
        wall.material = Material.wallMetal6
        wall.canCastShadow = True
        wall.info = "room 1"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(122, 58, z)
        wall.endPoint = Vector3(128, 58, z)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, 1, 0)
        wall.height = 12
        wall.material = Material.wallMetal6
        wall.canCastShadow = True
        wall.info = "room 1"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(128, 52, z)
        wall.endPoint = Vector3(128, 58, z)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(1, 0, 0)
        wall.height = 12
        wall.material = Material.wallMetal6
        wall.canCastShadow = True
        wall.info = "room 1"
        self.addWall(wall)

        floor = Floor()
        floor.downLeft = Vector3(70, 10, z)
        floor.downRight = Vector3(150, 10, z)
        floor.upLeft = Vector3(70, 80, z)
        floor.upRight = Vector3(150, 80, z)
        floor.material = Material.floorConcrete1
        self.addFloor(floor)

        # second floor

        z = 8
        wallHeight = 4

        wall = Wall()
        wall.startPoint = Vector3(70, 30, z)
        wall.endPoint = Vector3(70, 40, z)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(1, 0, 0)
        wall.height = wallHeight
        wall.material = Material.wallMetal2
        wall.canCastShadow = True
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(70, 30, z)
        wall.endPoint = Vector3(90, 10, z)
        wall.orientation = Orientation.diagonal
        wall.frontNormal = Vector3(1, 1, 0)
        wall.frontNormal.normalize()
        wall.height = wallHeight
        wall.material = Material.wallMetal2
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(90, 10, z)
        wall.endPoint = Vector3(130, 10, z)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, 1, 0)
        wall.height = wallHeight
        wall.material = Material.wallMetal2
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(130, 10, z)
        wall.endPoint = Vector3(150, 30, z)
        wall.orientation = Orientation.diagonal
        wall.frontNormal = Vector3(-1, 1, 0)
        wall.frontNormal.normalize()
        wall.height = wallHeight
        wall.material = Material.wallMetal2
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(150, 30, z)
        wall.endPoint = Vector3(150, 40, z)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(-1, 0, 0)
        wall.height = wallHeight
        wall.material = Material.wallMetal2
        wall.canCastShadow = True
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(150, 40, z)
        wall.endPoint = Vector3(150, 50, z)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(-1, 0, 0)
        wall.height = wallHeight
        wall.material = Material.wallMetal2
        wall.canCastShadow = True
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(150, 50, z)
        wall.endPoint = Vector3(150, 60, z)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(-1, 0, 0)
        wall.height = wallHeight
        wall.material = Material.wallMetal2
        wall.canCastShadow = True
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(130, 80, z)
        wall.endPoint = Vector3(150, 60, z)
        wall.orientation = Orientation.diagonal
        wall.frontNormal = Vector3(-1, -1, 0)
        wall.frontNormal.normalize()
        wall.height = wallHeight
        wall.material = Material.wallMetal2
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(110, 80, z)
        wall.endPoint = Vector3(130, 80, z)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, -1, 0)
        wall.height = wallHeight
        wall.material = Material.wallMetal2
        wall.canCastShadow = True
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(100, 80, z)
        wall.endPoint = Vector3(110, 80, z)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, -1, 0)
        wall.height = wallHeight
        wall.material = Material.wallMetal2
        wall.canCastShadow = True
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(90, 80, z)
        wall.endPoint = Vector3(100, 80, z)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, -1, 0)
        wall.height = wallHeight
        wall.material = Material.wallMetal2
        wall.canCastShadow = True
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(70, 60, z)
        wall.endPoint = Vector3(90, 80, z)
        wall.orientation = Orientation.diagonal
        wall.frontNormal = Vector3(1, -1, 0)
        wall.frontNormal.normalize()
        wall.height = wallHeight
        wall.material = Material.wallMetal2
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(70, 50, z)
        wall.endPoint = Vector3(70, 60, z)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(1, 0, 0)
        wall.height = wallHeight
        wall.material = Material.wallMetal2
        wall.canCastShadow = True
        self.addWall(wall)

        floor = Floor()
        floor.downLeft = Vector3(70, 60, z)
        floor.downRight = Vector3(70, 30, z)
        floor.upLeft = Vector3(80, 60, z)
        floor.upRight = Vector3(80, 30, z)
        floor.visualSize = 10.0
        floor.material = Material.floorMetal2
        floor.canCastShadow = True
        self.addFloor(floor)

        floor = Floor()
        floor.downLeft = Vector3(70, 30, z)
        floor.downRight = Vector3(90, 10, z)
        floor.upLeft = Vector3(80, 30, z)
        floor.upRight = Vector3(90, 20, z)
        floor.visualSize = 10.0
        floor.material = Material.floorMetal2
        floor.canCastShadow = True
        self.addFloor(floor)

        floor = Floor()
        floor.downLeft = Vector3(90, 10, z)
        floor.downRight = Vector3(130, 10, z)
        floor.upLeft = Vector3(90, 20, z)
        floor.upRight = Vector3(130, 20, z)
        floor.visualSize = 10.0
        floor.material = Material.floorMetal2
        floor.canCastShadow = True
        self.addFloor(floor)

        floor = Floor()
        floor.downLeft = Vector3(130, 10, z)
        floor.downRight = Vector3(150, 30, z)
        floor.upLeft = Vector3(130, 20, z)
        floor.upRight = Vector3(140, 30, z)
        floor.visualSize = 10.0
        floor.material = Material.floorMetal2
        floor.canCastShadow = True
        self.addFloor(floor)

        floor = Floor()
        floor.downLeft = Vector3(150, 30, z)
        floor.downRight = Vector3(150, 60, z)
        floor.upLeft = Vector3(140, 30, z)
        floor.upRight = Vector3(140, 60, z)
        floor.visualSize = 10.0
        floor.material = Material.floorMetal2
        floor.canCastShadow = True
        self.addFloor(floor)

        floor = Floor()
        floor.downLeft = Vector3(150, 60, z)
        floor.downRight = Vector3(130, 80, z)
        floor.upLeft = Vector3(140, 60, z)
        floor.upRight = Vector3(130, 70, z)
        floor.visualSize = 10.0
        floor.material = Material.floorMetal2
        floor.canCastShadow = True
        self.addFloor(floor)

        floor = Floor()
        floor.downLeft = Vector3(90, 70, z)
        floor.downRight = Vector3(130, 70, z)
        floor.upLeft = Vector3(90, 80, z)
        floor.upRight = Vector3(130, 80, z)
        floor.visualSize = 10.0
        floor.material = Material.floorMetal2
        floor.canCastShadow = True
        self.addFloor(floor)

        floor = Floor()
        floor.downLeft = Vector3(90, 80, z)
        floor.downRight = Vector3(70, 60, z)
        floor.upLeft = Vector3(90, 70, z)
        floor.upRight = Vector3(80, 60, z)
        floor.visualSize = 10.0
        floor.material = Material.floorMetal2
        floor.canCastShadow = True
        self.addFloor(floor)

        z -= secondFloorHeight

        ceiling = Ceiling()
        ceiling.downLeft = Vector3(70, 60, z)
        ceiling.downRight = Vector3(70, 30, z)
        ceiling.upLeft = Vector3(80, 60, z)
        ceiling.upRight = Vector3(80, 30, z)
        ceiling.material = Material.floorMetal2
        ceiling.canCastShadow = True
        self.addCeiling(ceiling)

        ceiling = Ceiling()
        ceiling.downLeft = Vector3(70, 30, z)
        ceiling.downRight = Vector3(90, 10, z)
        ceiling.upLeft = Vector3(80, 30, z)
        ceiling.upRight = Vector3(90, 20, z)
        ceiling.material = Material.floorMetal2
        ceiling.canCastShadow = True
        self.addCeiling(ceiling)

        ceiling = Ceiling()
        ceiling.downLeft = Vector3(90, 10, z)
        ceiling.downRight = Vector3(130, 10, z)
        ceiling.upLeft = Vector3(90, 20, z)
        ceiling.upRight = Vector3(130, 20, z)
        ceiling.material = Material.floorMetal2
        ceiling.canCastShadow = True
        self.addCeiling(ceiling)

        ceiling = Ceiling()
        ceiling.downLeft = Vector3(130, 10, z)
        ceiling.downRight = Vector3(150, 30, z)
        ceiling.upLeft = Vector3(130, 20, z)
        ceiling.upRight = Vector3(140, 30, z)
        ceiling.material = Material.floorMetal2
        ceiling.canCastShadow = True
        self.addCeiling(ceiling)

        ceiling = Ceiling()
        ceiling.downLeft = Vector3(150, 30, z)
        ceiling.downRight = Vector3(150, 60, z)
        ceiling.upLeft = Vector3(140, 30, z)
        ceiling.upRight = Vector3(140, 60, z)
        ceiling.material = Material.floorMetal2
        ceiling.canCastShadow = True
        self.addCeiling(ceiling)

        ceiling = Ceiling()
        ceiling.downLeft = Vector3(150, 60, z)
        ceiling.downRight = Vector3(130, 80, z)
        ceiling.upLeft = Vector3(140, 60, z)
        ceiling.upRight = Vector3(130, 70, z)
        ceiling.material = Material.floorMetal2
        ceiling.canCastShadow = True
        self.addCeiling(ceiling)

        ceiling = Ceiling()
        ceiling.downLeft = Vector3(90, 70, z)
        ceiling.downRight = Vector3(130, 70, z)
        ceiling.upLeft = Vector3(90, 80, z)
        ceiling.upRight = Vector3(130, 80, z)
        ceiling.material = Material.floorMetal2
        ceiling.canCastShadow = True
        self.addCeiling(ceiling)

        ceiling = Ceiling()
        ceiling.downLeft = Vector3(90, 80, z)
        ceiling.downRight = Vector3(70, 60, z)
        ceiling.upLeft = Vector3(90, 70, z)
        ceiling.upRight = Vector3(80, 60, z)
        ceiling.material = Material.floorMetal2
        ceiling.canCastShadow = True
        self.addCeiling(ceiling)

        wall = Wall()
        wall.startPoint = Vector3(80, 30, z)
        wall.endPoint = Vector3(80, 60, z)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(1, 0, 0)
        wall.height = secondFloorHeight
        wall.material = Material.edgeMetal1
        wall.canCastShadow = True
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(80, 60, z)
        wall.endPoint = Vector3(90, 70, z)
        wall.orientation = Orientation.diagonal
        wall.frontNormal = Vector3(1, -1, 0)
        wall.frontNormal.normalize()
        wall.height = secondFloorHeight
        wall.material = Material.edgeMetal1
        wall.canCastShadow = True
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(90, 70, z)
        wall.endPoint = Vector3(130, 70, z)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, -1, 0)
        wall.height = secondFloorHeight
        wall.material = Material.edgeMetal1
        wall.canCastShadow = True
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(130, 70, z)
        wall.endPoint = Vector3(140, 60, z)
        wall.orientation = Orientation.diagonal
        wall.frontNormal = Vector3(-1, -1, 0)
        wall.frontNormal.normalize()
        wall.height = secondFloorHeight
        wall.material = Material.edgeMetal1
        wall.canCastShadow = True
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(140, 30, z)
        wall.endPoint = Vector3(140, 60, z)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(-1, 0, 0)
        wall.height = secondFloorHeight
        wall.material = Material.edgeMetal1
        wall.canCastShadow = True
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(130, 20, z)
        wall.endPoint = Vector3(140, 30, z)
        wall.orientation = Orientation.diagonal
        wall.frontNormal = Vector3(-1, 1, 0)
        wall.frontNormal.normalize()
        wall.height = secondFloorHeight
        wall.material = Material.edgeMetal1
        wall.canCastShadow = True
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(90, 20, z)
        wall.endPoint = Vector3(130, 20, z)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, 1, 0)
        wall.height = secondFloorHeight
        wall.material = Material.edgeMetal1
        wall.canCastShadow = True
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(80, 30, z)
        wall.endPoint = Vector3(90, 20, z)
        wall.orientation = Orientation.diagonal
        wall.frontNormal = Vector3(1, 1, 0)
        wall.frontNormal.normalize()
        wall.height = secondFloorHeight
        wall.material = Material.edgeMetal1
        wall.canCastShadow = True
        self.addWall(wall)

        wallHeight = 12

        ceiling = Ceiling()
        ceiling.downLeft = Vector3(70, 10, wallHeight)
        ceiling.downRight = Vector3(150, 10, wallHeight)
        ceiling.upLeft = Vector3(70, 80, wallHeight)
        ceiling.upRight = Vector3(150, 80, wallHeight)
        ceiling.material = Material.ceilingMetal1
        self.addCeiling(ceiling)

        light = Lamp()
        light.position = Vector3(90, 45, wallHeight - 0.1)
        light.color.mul(2)
        self.addLight(light)

    def makeRoom2(self):
        wallHeight = 9
        z = 3
        secondFloorHeight = 0.8

        wall = Wall()
        wall.startPoint = Vector3(170, 110, z)
        wall.endPoint = Vector3(170, 120, z)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(1, 0, 0)
        wall.height = wallHeight
        wall.material = Material.wallMetal7
        wall.info = "room 2"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(170, 110, z)
        wall.endPoint = Vector3(190, 90, z)
        wall.orientation = Orientation.diagonal
        wall.frontNormal = Vector3(1, 1, 0)
        wall.frontNormal.normalize()
        wall.height = wallHeight
        wall.material = Material.wallMetal7
        wall.info = "room 2"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(190, 90, z)
        wall.endPoint = Vector3(210, 90, z)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, 1, 0)
        wall.height = wallHeight
        wall.material = Material.wallMetal7
        wall.info = "room 2"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(210, 90, 7)
        wall.endPoint = Vector3(220, 90, 7)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, 1, 0)
        wall.height = wallHeight
        wall.material = Material.wallMetal8
        wall.info = "room 2"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(220, 90, z)
        wall.endPoint = Vector3(250, 90, z)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, 1, 0)
        wall.height = wallHeight
        wall.material = Material.wallMetal7
        wall.info = "room 2"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(250, 90, z)
        wall.endPoint = Vector3(270, 110, z)
        wall.orientation = Orientation.diagonal
        wall.frontNormal = Vector3(-1, 1, 0)
        wall.frontNormal.normalize()
        wall.height = wallHeight
        wall.material = Material.wallMetal7
        wall.info = "room 2"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(270, 110, z)
        wall.endPoint = Vector3(270, 140, z)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(-1, 0, 0)
        wall.height = wallHeight
        wall.material = Material.wallMetal7
        wall.info = "room 2"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(250, 160, z)
        wall.endPoint = Vector3(270, 140, z)
        wall.orientation = Orientation.diagonal
        wall.frontNormal = Vector3(-1, -1, 0)
        wall.frontNormal.normalize()
        wall.height = wallHeight
        wall.material = Material.wallMetal7
        wall.info = "room 2"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(240, 160, z)
        wall.endPoint = Vector3(250, 160, z)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, -1, 0)
        wall.height = wallHeight
        wall.material = Material.wallMetal7
        wall.info = "room 2"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(230, 160, z)
        wall.endPoint = Vector3(240, 160, z)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, -1, 0)
        wall.height = wallHeight
        wall.material = Material.wallMetal7
        wall.info = "room 2"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(190, 160, z)
        wall.endPoint = Vector3(230, 160, z)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, -1, 0)
        wall.height = wallHeight
        wall.material = Material.wallMetal7
        wall.info = "room 2"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(170, 140, z)
        wall.endPoint = Vector3(190, 160, z)
        wall.orientation = Orientation.diagonal
        wall.frontNormal = Vector3(1, -1, 0)
        wall.frontNormal.normalize()
        wall.height = wallHeight
        wall.material = Material.wallMetal7
        wall.info = "room 2"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(170, 130, z)
        wall.endPoint = Vector3(170, 140, z)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(1, 0, 0)
        wall.height = wallHeight
        wall.material = Material.wallMetal7
        wall.info = "room 2"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(170, 120, 7)
        wall.endPoint = Vector3(170, 130, 7)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(1, 0, 0)
        wall.height = wallHeight - 4 - 0.8
        wall.material = Material.wallMetal8
        wall.info = "room 2"
        self.addWall(wall)

        floor = Floor()
        floor.downLeft = Vector3(170, 90, z)
        floor.downRight = Vector3(185, 90, z)
        floor.upLeft = Vector3(170, 160, z)
        floor.upRight = Vector3(185, 160, z)
        floor.material = Material.floorConcrete1
        self.addFloor(floor)

        floor = Floor()
        floor.downLeft = Vector3(255, 90, z)
        floor.downRight = Vector3(270, 90, z)
        floor.upLeft = Vector3(255, 160, z)
        floor.upRight = Vector3(270, 160, z)
        floor.material = Material.floorConcrete1
        self.addFloor(floor)

        floor = Floor()
        floor.downLeft = Vector3(185, 145, z)
        floor.downRight = Vector3(255, 145, z)
        floor.upLeft = Vector3(185, 160, z)
        floor.upRight = Vector3(255, 160, z)
        floor.material = Material.floorConcrete1
        self.addFloor(floor)

        floor = Floor()
        floor.downLeft = Vector3(185, 90, z)
        floor.downRight = Vector3(255, 90, z)
        floor.upLeft = Vector3(185, 105, z)
        floor.upRight = Vector3(255, 105, z)
        floor.material = Material.floorConcrete1
        self.addFloor(floor)

        lowerFloorHeight = 0.5
        lowerFloorZ = z - lowerFloorHeight

        floor = Floor()
        floor.downLeft = Vector3(185, 105, lowerFloorZ)
        floor.downRight = Vector3(255, 105, lowerFloorZ)
        floor.upLeft = Vector3(185, 145, lowerFloorZ)
        floor.upRight = Vector3(255, 145, lowerFloorZ)
        floor.z = lowerFloorZ
        floor.visualSize = 10.0
        floor.material = Material.floorMetal4
        self.addFloor(floor)

        wall = Wall()
        wall.startPoint = Vector3(185, 105, lowerFloorZ)
        wall.endPoint = Vector3(185, 145, lowerFloorZ)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(1, 0, 0)
        wall.height = lowerFloorHeight
        wall.material = Material.edgeMetal2
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(255, 105, lowerFloorZ)
        wall.endPoint = Vector3(255, 145, lowerFloorZ)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(-1, 0, 0)
        wall.height = lowerFloorHeight
        wall.material = Material.edgeMetal2
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(185, 105, lowerFloorZ)
        wall.endPoint = Vector3(255, 105, lowerFloorZ)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, 1, 0)
        wall.height = lowerFloorHeight
        wall.material = Material.edgeMetal2
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(185, 145, lowerFloorZ)
        wall.endPoint = Vector3(255, 145, lowerFloorZ)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, -1, 0)
        wall.height = lowerFloorHeight
        wall.material = Material.edgeMetal2
        self.addWall(wall)

        poleHeight = wallHeight - secondFloorHeight

        # pole 1

        wall = Wall()
        wall.startPoint = Vector3(204, 124, lowerFloorZ)
        wall.endPoint = Vector3(206, 124, lowerFloorZ)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, -1, 0)
        wall.height = poleHeight
        wall.material = Material.ceilingMetal3
        wall.canCastShadow = True
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(204, 124, lowerFloorZ)
        wall.endPoint = Vector3(204, 126, lowerFloorZ)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(-1, 0, 0)
        wall.height = poleHeight
        wall.material = Material.ceilingMetal3
        wall.canCastShadow = True
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(204, 126, lowerFloorZ)
        wall.endPoint = Vector3(206, 126, lowerFloorZ)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, 1, 0)
        wall.height = poleHeight
        wall.material = Material.ceilingMetal3
        wall.canCastShadow = True
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(206, 124, lowerFloorZ)
        wall.endPoint = Vector3(206, 126, lowerFloorZ)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(1, 0, 0)
        wall.height = poleHeight
        wall.material = Material.ceilingMetal3
        wall.canCastShadow = True
        self.addWall(wall)

        # pole 2

        wall = Wall()
        wall.startPoint = Vector3(234, 124, lowerFloorZ)
        wall.endPoint = Vector3(236, 124, lowerFloorZ)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, -1, 0)
        wall.height = poleHeight
        wall.material = Material.ceilingMetal3
        wall.canCastShadow = True
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(234, 124, lowerFloorZ)
        wall.endPoint = Vector3(234, 126, lowerFloorZ)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(-1, 0, 0)
        wall.height = poleHeight
        wall.material = Material.ceilingMetal3
        wall.canCastShadow = True
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(234, 126, lowerFloorZ)
        wall.endPoint = Vector3(236, 126, lowerFloorZ)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, 1, 0)
        wall.height = poleHeight
        wall.material = Material.ceilingMetal3
        wall.canCastShadow = True
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(236, 124, lowerFloorZ)
        wall.endPoint = Vector3(236, 126, lowerFloorZ)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(1, 0, 0)
        wall.height = poleHeight
        wall.material = Material.ceilingMetal3
        wall.canCastShadow = True
        self.addWall(wall)

        # pole 3

        wall = Wall()
        wall.startPoint = Vector3(185, 124, lowerFloorZ)
        wall.endPoint = Vector3(187, 124, lowerFloorZ)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, -1, 0)
        wall.height = poleHeight
        wall.material = Material.ceilingMetal3
        wall.canCastShadow = True
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(185, 124, lowerFloorZ)
        wall.endPoint = Vector3(185, 126, lowerFloorZ)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(-1, 0, 0)
        wall.height = poleHeight
        wall.material = Material.ceilingMetal3
        wall.canCastShadow = True
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(185, 126, lowerFloorZ)
        wall.endPoint = Vector3(187, 126, lowerFloorZ)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, 1, 0)
        wall.height = poleHeight
        wall.material = Material.ceilingMetal3
        wall.canCastShadow = True
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(187, 124, lowerFloorZ)
        wall.endPoint = Vector3(187, 126, lowerFloorZ)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(1, 0, 0)
        wall.height = poleHeight
        wall.material = Material.ceilingMetal3
        wall.canCastShadow = True
        self.addWall(wall)

        # pole 4

        wall = Wall()
        wall.startPoint = Vector3(253, 124, lowerFloorZ)
        wall.endPoint = Vector3(255, 124, lowerFloorZ)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, -1, 0)
        wall.height = poleHeight
        wall.material = Material.ceilingMetal3
        wall.canCastShadow = True
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(253, 124, lowerFloorZ)
        wall.endPoint = Vector3(253, 126, lowerFloorZ)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(-1, 0, 0)
        wall.height = poleHeight
        wall.material = Material.ceilingMetal3
        wall.canCastShadow = True
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(253, 126, lowerFloorZ)
        wall.endPoint = Vector3(255, 126, lowerFloorZ)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, 1, 0)
        wall.height = poleHeight
        wall.material = Material.ceilingMetal3
        wall.canCastShadow = True
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(255, 124, lowerFloorZ)
        wall.endPoint = Vector3(255, 126, lowerFloorZ)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(1, 0, 0)
        wall.height = poleHeight
        wall.material = Material.ceilingMetal3
        wall.canCastShadow = True
        self.addWall(wall)

        # pole 5

        wall = Wall()
        wall.startPoint = Vector3(204, 99, z)
        wall.endPoint = Vector3(206, 99, z)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, -1, 0)
        wall.height = poleHeight
        wall.material = Material.ceilingMetal3
        wall.canCastShadow = True
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(204, 99, z)
        wall.endPoint = Vector3(204, 101, z)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(-1, 0, 0)
        wall.height = poleHeight
        wall.material = Material.ceilingMetal3
        wall.canCastShadow = True
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(204, 101, z)
        wall.endPoint = Vector3(206, 101, z)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, 1, 0)
        wall.height = poleHeight
        wall.material = Material.ceilingMetal3
        wall.canCastShadow = True
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(206, 99, z)
        wall.endPoint = Vector3(206, 101, z)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(1, 0, 0)
        wall.height = poleHeight
        wall.material = Material.ceilingMetal3
        wall.canCastShadow = True
        self.addWall(wall)

        # pole 6

        wall = Wall()
        wall.startPoint = Vector3(204, 149, z)
        wall.endPoint = Vector3(206, 149, z)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, -1, 0)
        wall.height = poleHeight
        wall.material = Material.ceilingMetal3
        wall.canCastShadow = True
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(204, 149, z)
        wall.endPoint = Vector3(204, 151, z)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(-1, 0, 0)
        wall.height = poleHeight
        wall.material = Material.ceilingMetal3
        wall.canCastShadow = True
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(204, 151, z)
        wall.endPoint = Vector3(206, 151, z)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, 1, 0)
        wall.height = poleHeight
        wall.material = Material.ceilingMetal3
        wall.canCastShadow = True
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(206, 149, z)
        wall.endPoint = Vector3(206, 151, z)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(1, 0, 0)
        wall.height = poleHeight
        wall.material = Material.ceilingMetal3
        wall.canCastShadow = True
        self.addWall(wall)

        # pole 7

        wall = Wall()
        wall.startPoint = Vector3(234, 149, z)
        wall.endPoint = Vector3(236, 149, z)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, -1, 0)
        wall.height = poleHeight
        wall.material = Material.ceilingMetal3
        wall.canCastShadow = True
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(234, 149, z)
        wall.endPoint = Vector3(234, 151, z)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(-1, 0, 0)
        wall.height = poleHeight
        wall.material = Material.ceilingMetal3
        wall.canCastShadow = True
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(234, 151, z)
        wall.endPoint = Vector3(236, 151, z)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, 1, 0)
        wall.height = poleHeight
        wall.material = Material.ceilingMetal3
        wall.canCastShadow = True
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(236, 149, z)
        wall.endPoint = Vector3(236, 151, z)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(1, 0, 0)
        wall.height = poleHeight
        wall.material = Material.ceilingMetal3
        wall.canCastShadow = True
        self.addWall(wall)

        # pole 8

        wall = Wall()
        wall.startPoint = Vector3(234, 99, z)
        wall.endPoint = Vector3(236, 99, z)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, -1, 0)
        wall.height = poleHeight
        wall.material = Material.ceilingMetal3
        wall.canCastShadow = True
        wall.info = "pole"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(234, 99, z)
        wall.endPoint = Vector3(234, 101, z)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(-1, 0, 0)
        wall.height = poleHeight
        wall.material = Material.ceilingMetal3
        wall.canCastShadow = True
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(234, 101, z)
        wall.endPoint = Vector3(236, 101, z)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, 1, 0)
        wall.height = poleHeight
        wall.material = Material.ceilingMetal3
        wall.canCastShadow = True
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(236, 99, z)
        wall.endPoint = Vector3(236, 101, z)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(1, 0, 0)
        wall.height = poleHeight
        wall.material = Material.ceilingMetal3
        wall.canCastShadow = True
        self.addWall(wall)

        # second floor

        z = 12
        wallHeight = 4

        wall = Wall()
        wall.startPoint = Vector3(170, 110, z)
        wall.endPoint = Vector3(170, 140, z)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(1, 0, 0)
        wall.height = wallHeight
        wall.material = Material.wallMetal9
        wall.info = "room 2"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(170, 110, z)
        wall.endPoint = Vector3(190, 90, z)
        wall.orientation = Orientation.diagonal
        wall.frontNormal = Vector3(1, 1, 0)
        wall.frontNormal.normalize()
        wall.height = wallHeight
        wall.material = Material.wallMetal9
        wall.info = "room 2"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(190, 90, z)
        wall.endPoint = Vector3(210, 90, z)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, 1, 0)
        wall.height = wallHeight
        wall.material = Material.wallMetal9
        wall.info = "room 2"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(220, 90, z)
        wall.endPoint = Vector3(250, 90, z)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, 1, 0)
        wall.height = wallHeight
        wall.material = Material.wallMetal9
        wall.info = "room 2"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(250, 90, z)
        wall.endPoint = Vector3(270, 110, z)
        wall.orientation = Orientation.diagonal
        wall.frontNormal = Vector3(-1, 1, 0)
        wall.frontNormal.normalize()
        wall.height = wallHeight
        wall.material = Material.wallMetal9
        wall.info = "room 2"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(270, 110, z)
        wall.endPoint = Vector3(270, 140, z)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(-1, 0, 0)
        wall.height = wallHeight
        wall.material = Material.wallMetal9
        wall.info = "room 2"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(250, 160, z)
        wall.endPoint = Vector3(270, 140, z)
        wall.orientation = Orientation.diagonal
        wall.frontNormal = Vector3(-1, -1, 0)
        wall.frontNormal.normalize()
        wall.height = wallHeight
        wall.material = Material.wallMetal9
        wall.info = "room 2"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(190, 160, z)
        wall.endPoint = Vector3(230, 160, z)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, -1, 0)
        wall.height = wallHeight
        wall.material = Material.wallMetal9
        wall.info = "room 2"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(240, 160, z)
        wall.endPoint = Vector3(250, 160, z)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, -1, 0)
        wall.height = wallHeight
        wall.material = Material.wallMetal9
        wall.info = "room 2"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(170, 140, z)
        wall.endPoint = Vector3(190, 160, z)
        wall.orientation = Orientation.diagonal
        wall.frontNormal = Vector3(1, -1, 0)
        wall.frontNormal.normalize()
        wall.height = wallHeight
        wall.material = Material.wallMetal9
        wall.info = "room 2"
        self.addWall(wall)

        floor = Floor()
        floor.downLeft = Vector3(230, 90, z)
        floor.downRight = Vector3(240, 90, z)
        floor.upLeft = Vector3(230, 160, z)
        floor.upRight = Vector3(240, 160, z)
        floor.visualSize = 10.0
        floor.material = Material.wallMetal3
        floor.canCastShadow = True
        self.addFloor(floor)

        floor = Floor()
        floor.downLeft = Vector3(200, 90, z)
        floor.downRight = Vector3(210, 90, z)
        floor.upLeft = Vector3(200, 160, z)
        floor.upRight = Vector3(210, 160, z)
        floor.visualSize = 10.0
        floor.material = Material.wallMetal3
        floor.canCastShadow = True
        self.addFloor(floor)

        floor = Floor()
        floor.downLeft = Vector3(210, 120, z)
        floor.downRight = Vector3(230, 120, z)
        floor.upLeft = Vector3(210, 130, z)
        floor.upRight = Vector3(230, 130, z)
        floor.visualSize = 10.0
        floor.material = Material.wallMetal3
        floor.canCastShadow = True
        self.addFloor(floor)

        floor = Floor()
        floor.downLeft = Vector3(170, 120, z)
        floor.downRight = Vector3(200, 120, z)
        floor.upLeft = Vector3(170, 130, z)
        floor.upRight = Vector3(200, 130, z)
        floor.visualSize = 10.0
        floor.material = Material.wallMetal3
        floor.canCastShadow = True
        self.addFloor(floor)

        floor = Floor()
        floor.downLeft = Vector3(240, 120, z)
        floor.downRight = Vector3(270, 120, z)
        floor.upLeft = Vector3(240, 130, z)
        floor.upRight = Vector3(270, 130, z)
        floor.visualSize = 10.0
        floor.material = Material.wallMetal3
        floor.canCastShadow = True
        self.addFloor(floor)

        z -= secondFloorHeight

        ceiling = Ceiling()
        ceiling.downLeft = Vector3(230, 90, z)
        ceiling.downRight = Vector3(240, 90, z)
        ceiling.upLeft = Vector3(230, 160, z)
        ceiling.upRight = Vector3(240, 160, z)
        ceiling.material = Material.wallMetal3
        ceiling.canCastShadow = True
        self.addCeiling(ceiling)

        ceiling = Ceiling()
        ceiling.downLeft = Vector3(200, 90, z)
        ceiling.downRight = Vector3(210, 90, z)
        ceiling.upLeft = Vector3(200, 160, z)
        ceiling.upRight = Vector3(210, 160, z)
        ceiling.material = Material.wallMetal3
        ceiling.canCastShadow = True
        self.addCeiling(ceiling)

        ceiling = Ceiling()
        ceiling.downLeft = Vector3(210, 120, z)
        ceiling.downRight = Vector3(230, 120, z)
        ceiling.upLeft = Vector3(210, 130, z)
        ceiling.upRight = Vector3(230, 130, z)
        ceiling.material = Material.wallMetal3
        ceiling.canCastShadow = True
        self.addCeiling(ceiling)

        ceiling = Ceiling()
        ceiling.downLeft = Vector3(170, 120, z)
        ceiling.downRight = Vector3(200, 120, z)
        ceiling.upLeft = Vector3(170, 130, z)
        ceiling.upRight = Vector3(200, 130, z)
        ceiling.z = z
        ceiling.material = Material.wallMetal3
        ceiling.canCastShadow = True
        self.addCeiling(ceiling)

        ceiling = Ceiling()
        ceiling.downLeft = Vector3(240, 120, z)
        ceiling.downRight = Vector3(270, 120, z)
        ceiling.upLeft = Vector3(240, 130, z)
        ceiling.upRight = Vector3(270, 130, z)
        ceiling.z = z
        ceiling.material = Material.wallMetal3
        ceiling.canCastShadow = True
        self.addCeiling(ceiling)

        wall = Wall()
        wall.startPoint = Vector3(200, 90, z)
        wall.endPoint = Vector3(200, 160, z)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(-1, 0, 0)
        wall.height = secondFloorHeight
        wall.material = Material.edgeMetal3
        wall.canCastShadow = True
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(210, 90, z)
        wall.endPoint = Vector3(210, 160, z)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(1, 0, 0)
        wall.height = secondFloorHeight
        wall.material = Material.edgeMetal3
        wall.canCastShadow = True
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(230, 90, z)
        wall.endPoint = Vector3(230, 160, z)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(-1, 0, 0)
        wall.height = secondFloorHeight
        wall.material = Material.edgeMetal3
        wall.canCastShadow = True
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(240, 90, z)
        wall.endPoint = Vector3(240, 160, z)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(1, 0, 0)
        wall.height = secondFloorHeight
        wall.material = Material.edgeMetal3
        wall.canCastShadow = True
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(210, 120, z)
        wall.endPoint = Vector3(230, 120, z)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, -1, 0)
        wall.height = secondFloorHeight
        wall.material = Material.edgeMetal3
        wall.canCastShadow = True
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(210, 130, z)
        wall.endPoint = Vector3(230, 130, z)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, 1, 0)
        wall.height = secondFloorHeight
        wall.material = Material.edgeMetal3
        wall.canCastShadow = True
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(170, 120, z)
        wall.endPoint = Vector3(200, 120, z)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, -1, 0)
        wall.height = secondFloorHeight
        wall.material = Material.edgeMetal3
        wall.canCastShadow = True
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(170, 130, z)
        wall.endPoint = Vector3(200, 130, z)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, 1, 0)
        wall.height = secondFloorHeight
        wall.material = Material.edgeMetal3
        wall.canCastShadow = True
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(240, 120, z)
        wall.endPoint = Vector3(270, 120, z)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, -1, 0)
        wall.height = secondFloorHeight
        wall.material = Material.edgeMetal3
        wall.canCastShadow = True
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(240, 130, z)
        wall.endPoint = Vector3(270, 130, z)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, 1, 0)
        wall.height = secondFloorHeight
        wall.material = Material.edgeMetal3
        wall.canCastShadow = True
        self.addWall(wall)

        z += secondFloorHeight

        ceiling = Ceiling()
        ceiling.downLeft = Vector3(170, 90, z + wallHeight)
        ceiling.downRight = Vector3(270, 90, z + wallHeight)
        ceiling.upLeft = Vector3(170, 160, z + wallHeight)
        ceiling.upRight = Vector3(270, 160, z + wallHeight)
        ceiling.material = Material.ceilingMetal3
        self.addCeiling(ceiling)

        light = Lamp()
        light.color.mul(3)
        light.position = Vector3(220, 125, z + wallHeight - 0.1)
        self.addLight(light)

    def makeRoom3(self):
        wallHeight = 4
        z = 0

        wall = Wall()
        wall.startPoint = Vector3(70, 100, z)
        wall.endPoint = Vector3(70, 110, z)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(1, 0, 0)
        wall.height = wallHeight
        wall.material = Material.wallMetal1
        wall.info = "room 3"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(70, 100, z)
        wall.endPoint = Vector3(100, 100, z)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, 1, 0)
        wall.height = wallHeight
        wall.material = Material.wallMetal1
        wall.info = "room 3"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(110, 100, z)
        wall.endPoint = Vector3(110, 120, z)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(-1, 0, 0)
        wall.height = wallHeight
        wall.material = Material.wallMetal1
        wall.info = "room 3"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(110, 120, z)
        wall.endPoint = Vector3(140, 120, z)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, 1, 0)
        wall.height = wallHeight
        wall.material = Material.wallMetal1
        wall.info = "room 3"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(140, 130, z)
        wall.endPoint = Vector3(140, 160, z)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(-1, 0, 0)
        wall.height = wallHeight
        wall.material = Material.wallMetal1
        wall.info = "room 3"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(100, 160, z)
        wall.endPoint = Vector3(130, 160, z)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, -1, 0)
        wall.height = wallHeight
        wall.material = Material.wallMetal1
        wall.info = "room 3"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(90, 150, z)
        wall.endPoint = Vector3(100, 160, z)
        wall.orientation = Orientation.diagonal
        wall.frontNormal = Vector3(1, -1, 0)
        wall.frontNormal.normalize()
        wall.height = wallHeight
        wall.material = Material.wallMetal1
        wall.info = "room 3"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(90, 130, z)
        wall.endPoint = Vector3(90, 150, z)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(1, 0, 0)
        wall.height = wallHeight
        wall.material = Material.wallMetal1
        wall.info = "room 3"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(70, 130, z)
        wall.endPoint = Vector3(90, 130, z)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, -1, 0)
        wall.height = wallHeight
        wall.material = Material.wallMetal1
        wall.info = "room 3"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(70, 120, z)
        wall.endPoint = Vector3(70, 130, z)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(1, 0, 0)
        wall.height = wallHeight
        wall.material = Material.wallMetal1
        wall.info = "room 3"
        self.addWall(wall)

        floor = Floor()
        floor.downLeft = Vector3(70, 100, z)
        floor.downRight = Vector3(110, 100, z)
        floor.upLeft = Vector3(70, 130, z)
        floor.upRight = Vector3(110, 130, z)
        floor.material = Material.floorConcrete1
        self.addFloor(floor)

        floor = Floor()
        floor.downLeft = Vector3(90, 130, z)
        floor.downRight = Vector3(140, 130, z)
        floor.upLeft = Vector3(90, 160, z)
        floor.upRight = Vector3(140, 160, z)
        floor.material = Material.floorConcrete1
        self.addFloor(floor)

        floor = Floor()
        floor.downLeft = Vector3(110, 120, z)
        floor.downRight = Vector3(140, 120, z)
        floor.upLeft = Vector3(110, 130, z)
        floor.upRight = Vector3(140, 130, z)
        floor.material = Material.floorConcrete1
        self.addFloor(floor)

        ceiling = Ceiling()
        ceiling.downLeft = Vector3(70, 100, wallHeight + z)
        ceiling.downRight = Vector3(140, 100, wallHeight + z)
        ceiling.upLeft = Vector3(70, 160, wallHeight + z)
        ceiling.upRight = Vector3(140, 160, wallHeight + z)
        ceiling.material = Material.ceilingMetal1
        self.addCeiling(ceiling)

        light = Lamp()
        light.position = Vector3(115, 140, wallHeight + z - 0.1)
        light.color.mul(2)
        light.joinGroup = "room3"
        self.addLight(light)

    def makePass1(self):
        wallHeight = 4

        wall = Wall()
        wall.startPoint = Vector3(150, 40, 0)
        wall.endPoint = Vector3(190, 40, 2)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, 1, 0)
        wall.height = wallHeight
        wall.material = Material.wallMetal1
        wall.info = "pass 1"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(190, 40, 2)
        wall.endPoint = Vector3(220, 70, 2)
        wall.orientation = Orientation.diagonal
        wall.frontNormal = Vector3(-1, 1, 0)
        wall.frontNormal.normalize()
        wall.height = wallHeight
        wall.material = Material.wallMetal1
        wall.info = "pass 1"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(220, 70, 2)
        wall.endPoint = Vector3(220, 80, 2.5)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(-1, 0, 0)
        wall.height = wallHeight
        wall.material = Material.wallMetal1
        wall.info = "pass 1"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(220, 80, 2.5)
        wall.endPoint = Vector3(220, 90, 3)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(-1, 0, 0)
        wall.height = wallHeight
        wall.material = Material.wallMetal1
        wall.info = "pass 1"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(150, 50, 0)
        wall.endPoint = Vector3(190, 50, 2)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, -1, 0)
        wall.height = wallHeight
        wall.material = Material.wallMetal1
        wall.info = "pass 1"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(190, 50, 2)
        wall.endPoint = Vector3(210, 70, 2)
        wall.orientation = Orientation.diagonal
        wall.frontNormal = Vector3(1, -1, 0)
        wall.frontNormal.normalize()
        wall.height = wallHeight
        wall.material = Material.wallMetal1
        wall.info = "pass 1"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(210, 70, 2)
        wall.endPoint = Vector3(210, 80, 2.5)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(1, 0, 0)
        wall.height = wallHeight
        wall.material = Material.wallMetal1
        wall.info = "pass 1"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(210, 80, 2.5)
        wall.endPoint = Vector3(210, 90, 3)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(1, 0, 0)
        wall.height = wallHeight
        wall.material = Material.wallMetal1
        wall.info = "pass 1"
        self.addWall(wall)

        floor = Floor()
        floor.downLeft = Vector3(150, 40, 0)
        floor.downRight = Vector3(190, 40, 2)
        floor.upLeft = Vector3(150, 50, 0)
        floor.upRight = Vector3(190, 50, 2)
        v = floor.upLeft.getDirectionTo(floor.upRight)
        floor.frontNormal = Geometry.rotatePoint(v, Vector3(0, -1, 0), CommonConstants.axisOrigin, Math.piHalf)
        floor.frontNormal.normalize()
        floor.material = Material.floorConcrete1
        floor.commit()
        self.addFloor(floor)

        floor = Floor()
        floor.downLeft = Vector3(190, 40, 2)
        floor.downRight = Vector3(220, 40, 2)
        floor.upLeft = Vector3(190, 70, 2)
        floor.upRight = Vector3(220, 70, 2)
        floor.z = 2
        floor.material = Material.floorConcrete1
        self.addFloor(floor)

        floor = Floor()
        floor.downLeft = Vector3(210, 70, 2)
        floor.downRight = Vector3(220, 70, 2)
        floor.upLeft = Vector3(210, 80, 2.5)
        floor.upRight = Vector3(220, 80, 2.5)
        v = floor.downRight.getDirectionTo(floor.upRight)
        floor.frontNormal = Geometry.rotatePoint(v, Vector3(1, 0, 0), CommonConstants.axisOrigin, Math.piHalf)
        floor.frontNormal.normalize()
        floor.material = Material.floorConcrete1
        floor.commit()
        self.addFloor(floor)

        floor = Floor()
        floor.downLeft = Vector3(210, 80, 2.5)
        floor.downRight = Vector3(220, 80, 2.5)
        floor.upLeft = Vector3(210, 90, 3)
        floor.upRight = Vector3(220, 90, 3)
        v = floor.downRight.getDirectionTo(floor.upRight)
        floor.frontNormal = Geometry.rotatePoint(v, Vector3(1, 0, 0), CommonConstants.axisOrigin, Math.piHalf)
        floor.frontNormal.normalize()
        floor.material = Material.floorConcrete1
        floor.commit()
        self.addFloor(floor)

        ceiling = Ceiling()
        ceiling.downLeft = Vector3(150, 40, wallHeight)
        ceiling.downRight = Vector3(190, 40, wallHeight + 2)
        ceiling.upLeft = Vector3(150, 50, wallHeight)
        ceiling.upRight = Vector3(190, 50, wallHeight + 2)
        v = ceiling.upLeft.getDirectionTo(ceiling.upRight)
        ceiling.frontNormal = Geometry.rotatePoint(v, Vector3(0, 1, 0), CommonConstants.axisOrigin, Math.piHalf)
        ceiling.frontNormal.normalize()
        ceiling.material = Material.ceilingMetal1
        self.addCeiling(ceiling)

        ceiling = Ceiling()
        ceiling.downLeft = Vector3(190, 40, wallHeight + 2)
        ceiling.downRight = Vector3(220, 40, wallHeight + 2)
        ceiling.upLeft = Vector3(190, 70, wallHeight + 2)
        ceiling.upRight = Vector3(220, 70, wallHeight + 2)
        ceiling.material = Material.ceilingMetal1
        self.addCeiling(ceiling)

        ceiling = Ceiling()
        ceiling.downLeft = Vector3(210, 70, wallHeight + 2)
        ceiling.downRight = Vector3(220, 70, wallHeight + 2)
        ceiling.upLeft = Vector3(210, 80, wallHeight + 2.5)
        ceiling.upRight = Vector3(220, 80, wallHeight + 2.5)
        v = ceiling.downRight.getDirectionTo(ceiling.upRight)
        ceiling.frontNormal = Geometry.rotatePoint(v, Vector3(-1, 0, 0), CommonConstants.axisOrigin, Math.piHalf)
        ceiling.frontNormal.normalize()
        ceiling.material = Material.ceilingMetal1
        self.addCeiling(ceiling)

        ceiling = Ceiling()
        ceiling.downLeft = Vector3(210, 80, wallHeight + 2.5)
        ceiling.downRight = Vector3(220, 80, wallHeight + 2.5)
        ceiling.upLeft = Vector3(210, 90, wallHeight + 3)
        ceiling.upRight = Vector3(220, 90, wallHeight + 3)
        v = ceiling.downRight.getDirectionTo(ceiling.upRight)
        ceiling.frontNormal = Geometry.rotatePoint(v, Vector3(-1, 0, 0), CommonConstants.axisOrigin, Math.piHalf)
        ceiling.frontNormal.normalize()
        ceiling.material = Material.ceilingMetal1
        self.addCeiling(ceiling)

        light = Lamp()
        light.position = Vector3(170, 45, wallHeight + 1 - 0.1)
        light.color.mul(1.5)
        self.addLight(light)

        light = Lamp()
        light.position = Vector3(205, 60, wallHeight + 2 - 0.1)
        light.color.mul(1.5)
        light.joinGroup = "pass1"
        self.addLight(light)

        light = Lamp()
        light.position = Vector3(215, 85, wallHeight + 3 - 0.1)
        light.color.mul(1)
        light.joinGroup = "pass1"
        self.addLight(light)

    def makePass2(self):
        wallHeight = 4

        wall = Wall()
        wall.startPoint = Vector3(40, 120, 4)
        wall.endPoint = Vector3(50, 120, 4)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, -1, 0)
        wall.height = wallHeight
        wall.material = Material.wallMetal4
        wall.info = "pass 2"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(50, 120, 4)
        wall.endPoint = Vector3(70, 120, 0)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, -1, 0)
        wall.height = wallHeight
        wall.material = Material.wallMetal4
        wall.info = "pass 2"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(40, 40, 4)
        wall.endPoint = Vector3(40, 80, 4)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(1, 0, 0)
        wall.height = wallHeight
        wall.material = Material.wallMetal4
        wall.info = "pass 2"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(40, 80, 4)
        wall.endPoint = Vector3(40, 90, 4)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(1, 0, 0)
        wall.height = wallHeight
        wall.material = Material.wallMetal4
        wall.info = "pass 2"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(40, 90, 4)
        wall.endPoint = Vector3(40, 120, 4)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(1, 0, 0)
        wall.height = wallHeight
        wall.material = Material.wallMetal4
        wall.info = "pass 2"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(40, 40, 4)
        wall.endPoint = Vector3(50, 40, 4)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, 1, 0)
        wall.height = wallHeight
        wall.material = Material.wallMetal4
        wall.info = "pass 2"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(50, 40, 4)
        wall.endPoint = Vector3(70, 40, 8)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, 1, 0)
        wall.height = wallHeight
        wall.material = Material.wallMetal4
        wall.info = "pass 2"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(50, 110, 4)
        wall.endPoint = Vector3(70, 110, 0)
        wall.orientation = Orientation.horizontal
        wall.height = wallHeight
        wall.frontNormal = Vector3(0, 1, 0)
        wall.material = Material.wallMetal4
        wall.info = "pass 2"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(50, 50, 4)
        wall.endPoint = Vector3(50, 80, 4)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(-1, 0, 0)
        wall.height = wallHeight
        wall.material = Material.wallMetal4
        wall.info = "pass 2"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(50, 80, 4)
        wall.endPoint = Vector3(50, 90, 4)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(-1, 0, 0)
        wall.height = wallHeight
        wall.material = Material.wallMetal4
        wall.info = "pass 2"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(50, 90, 4)
        wall.endPoint = Vector3(50, 110, 4)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(-1, 0, 0)
        wall.height = wallHeight
        wall.material = Material.wallMetal4
        wall.info = "pass 2"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(50, 50, 4)
        wall.endPoint = Vector3(70, 50, 8)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, -1, 0)
        wall.height = wallHeight
        wall.material = Material.wallMetal4
        wall.info = "pass 2"
        self.addWall(wall)

        stair = Stair()
        stair.downLeft = Vector3(50, 110, 4)
        stair.downRight = Vector3(70, 110, 0)
        stair.upLeft = Vector3(50, 120, 4)
        stair.upRight = Vector3(70, 120, 0)
        stair.startBasePoint = Vector3(70, 110, 0)
        stair.endBasePoint = Vector3(50, 110, 4)
        stair.stepsCount = 7
        stair.stepWidth = 10
        stair.material = Material.wallMetal5
        stair.commit()
        self.addFloor(stair)

        floor = Floor()
        floor.downLeft = Vector3(40, 40, 4)
        floor.downRight = Vector3(50, 40, 4)
        floor.upLeft = Vector3(40, 80, 4)
        floor.upRight = Vector3(50, 80, 4)
        floor.z = 4
        floor.material = Material.floorConcrete1
        self.addFloor(floor)

        floor = Floor()
        floor.downLeft = Vector3(40, 80, 4)
        floor.downRight = Vector3(50, 80, 4)
        floor.upLeft = Vector3(40, 90, 4)
        floor.upRight = Vector3(50, 90, 4)
        floor.z = 4
        floor.material = Material.floorConcrete1
        self.addFloor(floor)

        floor = Floor()
        floor.downLeft = Vector3(40, 90, 4)
        floor.downRight = Vector3(50, 90, 4)
        floor.upLeft = Vector3(40, 120, 4)
        floor.upRight = Vector3(50, 120, 4)
        floor.z = 4
        floor.material = Material.floorConcrete1
        self.addFloor(floor)

        stair = Stair()
        stair.downLeft = Vector3(50, 40, 4)
        stair.downRight = Vector3(70, 40, 8)
        stair.upLeft = Vector3(50, 50, 4)
        stair.upRight = Vector3(70, 50, 8)
        stair.startBasePoint = Vector3(50, 50, 4)
        stair.endBasePoint = Vector3(70, 50, 8)
        stair.stepsCount = 7
        stair.stepWidth = 10
        stair.material = Material.wallMetal1
        stair.commit()
        self.addFloor(stair)

        ceiling = Ceiling()
        ceiling.downLeft = Vector3(50, 110, wallHeight + 4)
        ceiling.downRight = Vector3(70, 110, wallHeight)
        ceiling.upLeft = Vector3(50, 120, wallHeight + 4)
        ceiling.upRight = Vector3(70, 120, wallHeight)
        v = ceiling.upLeft.getDirectionTo(ceiling.upRight)
        v = Geometry.rotatePoint(v, Vector3(0, 1, 0), CommonConstants.axisOrigin, Math.piHalf)
        v.normalize()
        ceiling.frontNormal = v
        ceiling.material = Material.ceilingMetal1
        self.addCeiling(ceiling)

        ceiling = Ceiling()
        ceiling.downLeft = Vector3(40, 40, wallHeight + 4)
        ceiling.downRight = Vector3(50, 40, wallHeight + 4)
        ceiling.upLeft = Vector3(40, 80, wallHeight + 4)
        ceiling.upRight = Vector3(50, 80, wallHeight + 4)
        ceiling.material = Material.ceilingMetal2
        self.addCeiling(ceiling)

        ceiling = Ceiling()
        ceiling.downLeft = Vector3(40, 80, wallHeight + 4)
        ceiling.downRight = Vector3(50, 80, wallHeight + 4)
        ceiling.upLeft = Vector3(40, 90, wallHeight + 4)
        ceiling.upRight = Vector3(50, 90, wallHeight + 4)
        ceiling.material = Material.ceilingMetal2
        self.addCeiling(ceiling)

        ceiling = Ceiling()
        ceiling.downLeft = Vector3(40, 90, wallHeight + 4)
        ceiling.downRight = Vector3(50, 90, wallHeight + 4)
        ceiling.upLeft = Vector3(40, 120, wallHeight + 4)
        ceiling.upRight = Vector3(50, 120, wallHeight + 4)
        ceiling.material = Material.ceilingMetal2
        self.addCeiling(ceiling)

        ceiling = Ceiling()
        ceiling.downLeft = Vector3(50, 40, wallHeight + 4)
        ceiling.downRight = Vector3(70, 40, wallHeight + 8)
        ceiling.upLeft = Vector3(50, 50, wallHeight + 4)
        ceiling.upRight = Vector3(70, 50, wallHeight + 8)
        v = ceiling.upLeft.getDirectionTo(ceiling.upRight)
        v = Geometry.rotatePoint(v, Vector3(0, 1, 0), CommonConstants.axisOrigin, Math.piHalf)
        v.normalize()
        ceiling.frontNormal = v
        ceiling.material = Material.ceilingMetal1
        self.addCeiling(ceiling)

        light = Lamp()
        light.position = Vector3(45, 115, wallHeight + 4 - 0.1)
        light.color.mul(1)
        light.joinGroup = "pass2"
        self.addLight(light)

        light = Lamp()
        light.position = Vector3(45, 85, wallHeight + 6 - 0.1)
        light.color.mul(1)
        light.joinGroup = "pass2"
        self.addLight(light)

        light = Lamp()
        light.position = Vector3(45, 45, wallHeight + 8 - 0.1)
        light.color.mul(1)
        light.joinGroup = "pass2"
        self.addLight(light)

    def makePass3(self):
        wallHeight = 4

        wall = Wall()
        wall.startPoint = Vector3(130, 160, 0)
        wall.endPoint = Vector3(130, 170, 1)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(1, 0, 0)
        wall.height = wallHeight
        wall.material = Material.wallMetal1
        wall.info = "pass 3"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(130, 170, 1)
        wall.endPoint = Vector3(130, 180, 1)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(1, 0, 0)
        wall.height = wallHeight
        wall.material = Material.wallMetal1
        wall.info = "pass 3"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(130, 180, 1)
        wall.endPoint = Vector3(140, 180, 1)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, -1, 0)
        wall.height = wallHeight
        wall.material = Material.wallMetal1
        wall.info = "pass 3"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(140, 180, 1)
        wall.endPoint = Vector3(230, 180, 12)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, -1, 0)
        wall.height = wallHeight
        wall.material = Material.wallMetal1
        wall.info = "pass 3"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(230, 180, 12)
        wall.endPoint = Vector3(240, 180, 12)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, -1, 0)
        wall.height = wallHeight
        wall.material = Material.wallMetal1
        wall.info = "pass 3"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(240, 160, 12)
        wall.endPoint = Vector3(240, 180, 12)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(-1, 0, 0)
        wall.height = wallHeight
        wall.material = Material.wallMetal1
        wall.info = "pass 3"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(140, 160, 0)
        wall.endPoint = Vector3(140, 170, 1)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(-1, 0, 0)
        wall.height = wallHeight
        wall.material = Material.wallMetal1
        wall.info = "pass 3"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(140, 170, 1)
        wall.endPoint = Vector3(230, 170, 12)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, 1, 0)
        wall.height = wallHeight
        wall.material = Material.wallMetal1
        wall.info = "pass 3"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(230, 160, 12)
        wall.endPoint = Vector3(230, 170, 12)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(1, 0, 0)
        wall.height = wallHeight
        wall.material = Material.wallMetal1
        wall.info = "pass 3"
        self.addWall(wall)

        floor = Floor()
        floor.downLeft = Vector3(130, 160, 0)
        floor.downRight = Vector3(140, 160, 0)
        floor.upLeft = Vector3(130, 170, 1)
        floor.upRight = Vector3(140, 170, 1)
        v = floor.downRight.getDirectionTo(floor.upRight)
        floor.frontNormal = Geometry.rotatePoint(v, Vector3(1, 0, 0), CommonConstants.axisOrigin, Math.piHalf)
        floor.frontNormal.normalize()
        floor.material = Material.floorConcrete1
        floor.commit()
        self.addFloor(floor)

        floor = Floor()
        floor.downLeft = Vector3(130, 170, 1)
        floor.downRight = Vector3(140, 170, 1)
        floor.upLeft = Vector3(130, 180, 1)
        floor.upRight = Vector3(140, 180, 1)
        floor.z = 1
        floor.material = Material.floorConcrete1
        self.addFloor(floor)

        floor = Floor()
        floor.downLeft = Vector3(140, 170, 1)
        floor.downRight = Vector3(230, 170, 12)
        floor.upLeft = Vector3(140, 180, 1)
        floor.upRight = Vector3(230, 180, 12)
        v = floor.upLeft.getDirectionTo(floor.upRight)
        floor.frontNormal = Geometry.rotatePoint(v, Vector3(0, -1, 0), CommonConstants.axisOrigin, Math.piHalf)
        floor.frontNormal.normalize()
        floor.material = Material.floorConcrete1
        floor.commit()
        self.addFloor(floor)

        floor = Floor()
        floor.downLeft = Vector3(230, 160, 12)
        floor.downRight = Vector3(240, 160, 12)
        floor.upLeft = Vector3(230, 180, 12)
        floor.upRight = Vector3(240, 180, 12)
        floor.z = 12
        floor.material = Material.floorConcrete1
        self.addFloor(floor)

        ceiling = Ceiling()
        ceiling.downLeft = Vector3(130, 160, wallHeight)
        ceiling.downRight = Vector3(140, 160, wallHeight)
        ceiling.upLeft = Vector3(130, 170, wallHeight + 1)
        ceiling.upRight = Vector3(140, 170, wallHeight + 1)
        v = ceiling.downRight.getDirectionTo(ceiling.upRight)
        ceiling.frontNormal = Geometry.rotatePoint(v, Vector3(-1, 0, 0), CommonConstants.axisOrigin, Math.piHalf)
        ceiling.frontNormal.normalize()
        ceiling.material = Material.ceilingMetal1
        self.addCeiling(ceiling)

        ceiling = Ceiling()
        ceiling.downLeft = Vector3(130, 170, wallHeight + 1)
        ceiling.downRight = Vector3(140, 170, wallHeight + 1)
        ceiling.upLeft = Vector3(130, 180, wallHeight + 1)
        ceiling.upRight = Vector3(140, 180, wallHeight + 1)
        ceiling.material = Material.ceilingMetal1
        self.addCeiling(ceiling)

        ceiling = Ceiling()
        ceiling.downLeft = Vector3(140, 170, wallHeight + 1)
        ceiling.downRight = Vector3(230, 170, wallHeight + 12)
        ceiling.upLeft = Vector3(140, 180, wallHeight + 1)
        ceiling.upRight = Vector3(230, 180, wallHeight + 12)
        v = ceiling.upLeft.getDirectionTo(ceiling.upRight)
        ceiling.frontNormal = Geometry.rotatePoint(v, Vector3(0, 1, 0), CommonConstants.axisOrigin, Math.piHalf)
        ceiling.frontNormal.normalize()
        ceiling.material = Material.ceilingMetal1
        self.addCeiling(ceiling)

        ceiling = Ceiling()
        ceiling.downLeft = Vector3(230, 160, wallHeight + 12)
        ceiling.downRight = Vector3(240, 160, wallHeight + 12)
        ceiling.upLeft = Vector3(230, 180, wallHeight + 12)
        ceiling.upRight = Vector3(240, 180, wallHeight + 12)
        ceiling.material = Material.ceilingMetal1
        self.addCeiling(ceiling)

        light = Lamp()
        light.position = Vector3(135, 175, wallHeight + 1 - 0.1)
        light.color.mul(1.5)
        self.addLight(light)

        light = Lamp()
        light.position = Vector3(235, 175, wallHeight + 12 - 0.1)
        light.color.mul(1.5)
        self.addLight(light)

    def makePass4(self):
        wallHeight = 4

        wall = Wall()
        wall.startPoint = Vector3(140, 130, 0)
        wall.endPoint = Vector3(170, 130, 3)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, -1, 0)
        wall.height = wallHeight
        wall.material = Material.wallMetal1
        wall.info = "pass 4"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(140, 120, 0)
        wall.endPoint = Vector3(170, 120, 3)
        wall.orientation = Orientation.horizontal
        wall.frontNormal = Vector3(0, 1, 0)
        wall.height = wallHeight
        wall.material = Material.wallMetal1
        wall.info = "pass 4"
        self.addWall(wall)

        floor = Floor()
        floor.downLeft = Vector3(140, 120, 0)
        floor.downRight = Vector3(170, 120, 3)
        floor.upLeft = Vector3(140, 130, 0)
        floor.upRight = Vector3(170, 130, 3)
        v = floor.upLeft.getDirectionTo(floor.upRight)
        floor.frontNormal = Geometry.rotatePoint(v, Vector3(0, -1, 0), CommonConstants.axisOrigin, Math.piHalf)
        floor.frontNormal.normalize()
        floor.material = Material.floorConcrete1
        floor.commit()
        self.addFloor(floor)

        ceiling = Ceiling()
        ceiling.downLeft = Vector3(140, 120, wallHeight)
        ceiling.downRight = Vector3(170, 120, wallHeight + 3)
        ceiling.upLeft = Vector3(140, 130, wallHeight)
        ceiling.upRight = Vector3(170, 130, wallHeight + 3)
        v = ceiling.upLeft.getDirectionTo(ceiling.upRight)
        ceiling.frontNormal = Geometry.rotatePoint(v, Vector3(0, 1, 0), CommonConstants.axisOrigin, Math.piHalf)
        ceiling.frontNormal.normalize()
        ceiling.material = Material.ceilingMetal1
        self.addCeiling(ceiling)

        light = Lamp()
        light.position = Vector3(155, 125, wallHeight + 2 - 0.1)
        light.color.mul(2)
        self.addLight(light)

    def makePass5(self):
        wallHeight = 4

        wall = Wall()
        wall.startPoint = Vector3(100, 80, 0)
        wall.endPoint = Vector3(100, 90, 0)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(1, 0, 0)
        wall.height = wallHeight
        wall.material = Material.wallMetal1
        wall.info = "pass 5"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(110, 80, 0)
        wall.endPoint = Vector3(110, 90, 0)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(-1, 0, 0)
        wall.height = wallHeight
        wall.material = Material.wallMetal1
        wall.info = "pass 5"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(100, 90, 0)
        wall.endPoint = Vector3(100, 100, 0)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(1, 0, 0)
        wall.height = wallHeight
        wall.material = Material.wallMetal1
        wall.info = "pass 5"
        self.addWall(wall)

        wall = Wall()
        wall.startPoint = Vector3(110, 90, 0)
        wall.endPoint = Vector3(110, 100, 0)
        wall.orientation = Orientation.vertical
        wall.frontNormal = Vector3(-1, 0, 0)
        wall.height = wallHeight
        wall.material = Material.wallMetal1
        wall.info = "pass 5"
        self.addWall(wall)

        floor = Floor()
        floor.downLeft = Vector3(100, 80, 0)
        floor.downRight = Vector3(110, 80, 0)
        floor.upLeft = Vector3(100, 90, 0)
        floor.upRight = Vector3(110, 90, 0)
        floor.z = 0
        floor.material = Material.floorConcrete1
        self.addFloor(floor)

        floor = Floor()
        floor.downLeft = Vector3(100, 90, 0)
        floor.downRight = Vector3(110, 90, 0)
        floor.upLeft = Vector3(100, 100, 0)
        floor.upRight = Vector3(110, 100, 0)
        floor.z = 0
        floor.material = Material.floorConcrete1
        self.addFloor(floor)

        ceiling = Ceiling()
        ceiling.downLeft = Vector3(100, 80, wallHeight)
        ceiling.downRight = Vector3(110, 80, wallHeight)
        ceiling.upLeft = Vector3(100, 90, wallHeight)
        ceiling.upRight = Vector3(110, 90, wallHeight)
        ceiling.material = Material.ceilingMetal1
        self.addCeiling(ceiling)

        ceiling = Ceiling()
        ceiling.downLeft = Vector3(100, 90, wallHeight)
        ceiling.downRight = Vector3(110, 90, wallHeight)
        ceiling.upLeft = Vector3(100, 100, wallHeight)
        ceiling.upRight = Vector3(110, 100, wallHeight)
        ceiling.material = Material.ceilingMetal1
        self.addCeiling(ceiling)

        light = Lamp()
        light.position = Vector3(105, 85, wallHeight - 0.1)
        light.joinGroup = "room3"
        self.addLight(light)

    def getCollisionSplitPlanes(self):
        result = []

        result.extend(self.getVisibilitySplitPlanes())

        # room 1
        s = SplitPlane()
        s.basePoint = Vector3(110, 50, 3)
        s.frontNormal = Vector3(0, 0, 1)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(75, 45, 8)
        s.frontNormal = Vector3(0, 0, 1)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(90, 45, 0)
        s.frontNormal = Vector3(-1, 0, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(130, 45, 0)
        s.frontNormal = Vector3(1, 0, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(80, 40, 0)
        s.frontNormal = Vector3(0, -1, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(130, 40, 0)
        s.frontNormal = Vector3(0, -1, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(80, 50, 0)
        s.frontNormal = Vector3(0, 1, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(130, 50, 0)
        s.frontNormal = Vector3(0, 1, 0)
        result.append(s)

        # floor
        s = SplitPlane()
        s.basePoint = Vector3(90, 45, 8)
        s.frontNormal = Vector3(-1, 0, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(80, 45, 8)
        s.frontNormal = Vector3(-1, 0, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(80, 30, 8)
        s.frontNormal = Vector3(0, -1, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(80, 60, 8)
        s.frontNormal = Vector3(0, 1, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(85, 25, 8)
        s.frontNormal = Vector3(-1, -1, 0)
        s.frontNormal.normalize()
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(85, 65, 8)
        s.frontNormal = Vector3(-1, 1, 0)
        s.frontNormal.normalize()
        result.append(s)

        # floor
        s = SplitPlane()
        s.basePoint = Vector3(130, 45, 8)
        s.frontNormal = Vector3(1, 0, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(140, 45, 8)
        s.frontNormal = Vector3(1, 0, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(140, 30, 8)
        s.frontNormal = Vector3(0, -1, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(140, 60, 8)
        s.frontNormal = Vector3(0, 1, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(135, 25, 8)
        s.frontNormal = Vector3(1, -1, 0)
        s.frontNormal.normalize()
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(135, 65, 8)
        s.frontNormal = Vector3(1, 1, 0)
        s.frontNormal.normalize()
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(110, 20, 8)
        s.frontNormal = Vector3(0, -1, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(110, 70, 8)
        s.frontNormal = Vector3(0, 1, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(75, 40, 8)
        s.frontNormal = Vector3(0, 1, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(75, 50, 8)
        s.frontNormal = Vector3(0, -1, 0)
        result.append(s)

        # pass 5
        s = SplitPlane()
        s.basePoint = Vector3(100, 85, 0)
        s.frontNormal = Vector3(1, 0, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(110, 85, 0)
        s.frontNormal = Vector3(-1, 0, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(105, 100, 0)
        s.frontNormal = Vector3(0, 1, 0)
        result.append(s)

        # pass 1
        s = SplitPlane()
        s.basePoint = Vector3(190, 45, 0)
        s.frontNormal = Vector3(-1, 0, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(215, 70, 0)
        s.frontNormal = Vector3(0, -1, 0)
        result.append(s)

        # room 2
        s = SplitPlane()
        s.basePoint = Vector3(210, 120, 6)
        s.frontNormal = Vector3(0, 0, 1)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(235, 155, 12)
        s.frontNormal = Vector3(0, 0, 1)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(185, 125, 2)
        s.frontNormal = Vector3(-1, 0, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(255, 125, 2)
        s.frontNormal = Vector3(1, 0, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(220, 105, 2)
        s.frontNormal = Vector3(0, -1, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(220, 145, 2)
        s.frontNormal = Vector3(0, 1, 0)
        result.append(s)

        # floor
        s = SplitPlane()
        s.basePoint = Vector3(200, 125, 12)
        s.frontNormal = Vector3(1, 0, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(210, 125, 12)
        s.frontNormal = Vector3(-1, 0, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(230, 125, 12)
        s.frontNormal = Vector3(1, 0, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(240, 125, 12)
        s.frontNormal = Vector3(-1, 0, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(220, 130, 12)
        s.frontNormal = Vector3(0, -1, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(220, 120, 12)
        s.frontNormal = Vector3(0, 1, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(185, 130, 12)
        s.frontNormal = Vector3(0, -1, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(185, 120, 12)
        s.frontNormal = Vector3(0, 1, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(255, 130, 12)
        s.frontNormal = Vector3(0, -1, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(255, 120, 12)
        s.frontNormal = Vector3(0, 1, 0)
        result.append(s)

        # room 3
        s = SplitPlane()
        s.basePoint = Vector3(110, 130, 0)
        s.frontNormal = Vector3(0, -1, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(110, 125, 0)
        s.frontNormal = Vector3(-1, 0, 0)
        result.append(s)

        # pass 2
        s = SplitPlane()
        s.basePoint = Vector3(50, 115, 0)
        s.frontNormal = Vector3(-1, 0, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(50, 45, 0)
        s.frontNormal = Vector3(-1, 0, 0)
        result.append(s)

        # pass 3
        s = SplitPlane()
        s.basePoint = Vector3(180, 170, 0)
        s.frontNormal = Vector3(0, 1, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(140, 165, 0)
        s.frontNormal = Vector3(-1, 0, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(140, 175, 0)
        s.frontNormal = Vector3(-1, 0, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(230, 175, 0)
        s.frontNormal = Vector3(1, 0, 0)
        result.append(s)

        return result

    def getVisibilitySplitPlanes(self):
        result = []

        s = SplitPlane()
        s.basePoint = Vector3(150, 80, 0)
        s.frontNormal = Vector3(0, -1, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(150, 90, 0)
        s.frontNormal = Vector3(0, 1, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(150, 50, 0)
        s.frontNormal = Vector3(-1, 0, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(70, 50, 0)
        s.frontNormal = Vector3(1, 0, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(150, 160, 0)
        s.frontNormal = Vector3(0, -1, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(170, 120, 0)
        s.frontNormal = Vector3(1, 0, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(70, 120, 0)
        s.frontNormal = Vector3(1, 0, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(140, 120, 0)
        s.frontNormal = Vector3(-1, 0, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(100, 85, 0)
        s.frontNormal = Vector3(1, 0, 0)
        result.append(s)

        s = SplitPlane()
        s.basePoint = Vector3(110, 85, 0)
        s.frontNormal = Vector3(-1, 0, 0)
        result.append(s)

        return result

    def makeJoinLines(self):
        self.addJoinLine(LevelSegmentJoinLine(Vector3(100, 80, 2), Vector3(110, 80, 2), Vector3(0, -1, 0)))
        self.addJoinLine(LevelSegmentJoinLine(Vector3(210, 80, 4), Vector3(220, 80, 4), Vector3(0, -1, 0)))
        self.addJoinLine(LevelSegmentJoinLine(Vector3(40, 80, 5), Vector3(50, 80, 5), Vector3(0, -1, 0)))
        self.addJoinLine(LevelSegmentJoinLine(Vector3(150, 40, 2), Vector3(150, 50, 2), Vector3(-1, 0, 0)))
        self.addJoinLine(LevelSegmentJoinLine(Vector3(70, 40, 10), Vector3(70, 50, 10), Vector3(1, 0, 0)))
        self.addJoinLine(LevelSegmentJoinLine(Vector3(100, 90, 2), Vector3(110, 90, 2), Vector3(0, 1, 0)))
        self.addJoinLine(LevelSegmentJoinLine(Vector3(40, 90, 5), Vector3(50, 90, 5), Vector3(0, -1, 0)))
        self.addJoinLine(LevelSegmentJoinLine(Vector3(210, 90, 2), Vector3(220, 90, 2), Vector3(0, -1, 0)))
        self.addJoinLine(LevelSegmentJoinLine(Vector3(130, 160, 2), Vector3(140, 160, 2), Vector3(0, -1, 0)))
        self.addJoinLine(LevelSegmentJoinLine(Vector3(230, 160, 13), Vector3(240, 160, 13), Vector3(0, -1, 0)))
        self.addJoinLine(LevelSegmentJoinLine(Vector3(170, 120, 4), Vector3(170, 130, 4), Vector3(1, 0, 0)))
        self.addJoinLine(LevelSegmentJoinLine(Vector3(70, 110, 2), Vector3(70, 120, 2), Vector3(1, 0, 0)))
        self.addJoinLine(LevelSegmentJoinLine(Vector3(140, 120, 2), Vector3(140, 130, 2), Vector3(-1, 0, 0)))

    def makePowerupAreas(self):
        # room 1
        self.addPowerupArea(PowerupArea(Vector3(90, 12, 1), Vector3(90, 12, 1), 0))
        self.addPowerupArea(PowerupArea(Vector3(85, 65, 1), Vector3(135, 25, 1), 5))
        self.addPowerupArea(PowerupArea(Vector3(110, 20, 1), Vector3(110, 70, 1), 5))
        self.addPowerupArea(PowerupArea(Vector3(75, 45, 1), Vector3(185, 45, 1), 5))
        self.addPowerupArea(PowerupArea(Vector3(75, 30, 8), Vector3(75, 60, 8), 5))
        self.addPowerupArea(PowerupArea(Vector3(75, 60, 8), Vector3(90, 75, 8), 3.5))
        self.addPowerupArea(PowerupArea(Vector3(90, 75, 8), Vector3(130, 75, 8), 5))
        self.addPowerupArea(PowerupArea(Vector3(130, 75, 8), Vector3(145, 60, 8), 3.5))
        self.addPowerupArea(PowerupArea(Vector3(145, 60, 8), Vector3(145, 30, 8), 5))
        self.addPowerupArea(PowerupArea(Vector3(145, 30, 8), Vector3(130, 15, 8), 3.5))
        self.addPowerupArea(PowerupArea(Vector3(130, 15, 8), Vector3(90, 15, 8), 5))
        self.addPowerupArea(PowerupArea(Vector3(90, 15, 8), Vector3(75, 30, 8), 3.5))

        # room 3
        self.addPowerupArea(PowerupArea(Vector3(90, 115, 1), Vector3(90, 115, 1), 15))
        self.addPowerupArea(PowerupArea(Vector3(115, 140, 1), Vector3(115, 140, 1), 20))

        # pass 1
        self.addPowerupArea(PowerupArea(Vector3(195, 50, 2), Vector3(215, 70, 2), 5))
        self.addPowerupArea(PowerupArea(Vector3(215, 70, 2), Vector3(215, 90, 2), 5))

    def setPlayerPosition(self):
        self.playerPosition = Vector3(100, 30, 0)
        self.playerFrontNormal = Vector3(0, 1, 0)
