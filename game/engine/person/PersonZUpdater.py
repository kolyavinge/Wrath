from game.anx.Events import Events
from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal
from game.engine.GameData import GameData
from game.lib.EventManager import EventManager
from game.lib.Math import Math
from game.lib.Numeric import Numeric
from game.model.person.PersonZState import PersonZState


class PersonZUpdater:

    def __init__(
        self,
        gameData: GameData,
        traversal: BSPTreeTraversal,
        eventManager: EventManager,
    ):
        self.gameData = gameData
        self.traversal = traversal
        self.eventManager = eventManager

    def updateIfMoved(self):
        for person in self.gameData.allPerson:
            if person.hasMoved:
                self.updatePerson(person)

    def update(self):
        for person in self.gameData.allPerson:
            self.updatePerson(person)

    def updatePerson(self, person):
        levelSegment = self.traversal.findLevelSegmentOrNone(self.gameData.collisionTree, person.nextCenterPoint)
        assert levelSegment is not None
        if len(levelSegment.floors) == 1:
            self.processFloor(person, levelSegment)
        elif len(levelSegment.floors) == 0:
            self.processHole(person)
        else:
            raise Exception("Wrong floors count in segment. Segment can contain zero or one floor.")

    def processFloor(self, person, levelSegment):
        floor = levelSegment.floors[0]
        person.currentFloor = floor
        floorZ = floor.getZ(person.nextCenterPoint.x, person.nextCenterPoint.y)
        personOnFloor = Numeric.between(person.getZ() - floorZ, 0, 0.5)
        if personOnFloor and person.zState == PersonZState.onFloor and person.jumpingValue == 0:
            person.setZ(floorZ)
        elif personOnFloor and person.zState == PersonZState.onFloor and person.jumpingValue > 0:
            person.zState = PersonZState.jumping
        elif person.zState == PersonZState.jumping and person.jumpingValue > 0:
            person.setZ(person.getZ() + person.jumpingValue)
        elif person.zState == PersonZState.jumping and person.jumpingValue == 0:
            person.zState = PersonZState.falling
        elif personOnFloor and person.zState == PersonZState.falling:
            person.setZ(floorZ)
            person.fallingTime = 0
            person.zState = PersonZState.landing
            person.landingTime = 10 * 0.1
            self.eventManager.raiseEvent(Events.personLanded, person)
        elif personOnFloor and person.zState == PersonZState.landing:
            person.landingTime -= 0.1
            if person.landingTime <= 0:
                person.zState = PersonZState.onFloor
                person.landingTime = 0
        elif not personOnFloor:
            person.zState = PersonZState.falling
            self.processPersonFall(person, floorZ)
        else:
            raise Exception("Wrong person state.")

    def processHole(self, person):
        person.zState = PersonZState.falling
        self.processPersonFall(person)

    def processPersonFall(self, person, floorZ=None):
        person.fallingTime += 0.1
        personZ = person.getZ() - person.fallingFunc.getValue(person.fallingTime)
        if floorZ is not None:
            person.setZ(Math.max(personZ, floorZ))
        else:
            person.setZ(personZ)
