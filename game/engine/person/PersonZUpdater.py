from game.anx.Events import Events
from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal
from game.engine.GameData import GameData
from game.lib.EventManager import EventManager
from game.model.person.PersonState import PersonState


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
            raise Exception("Wrong floors count in segment.")

    def processFloor(self, person, levelSegment):
        floor = levelSegment.floors[0]
        person.currentFloor = floor
        z = floor.getZ(person.nextCenterPoint.x, person.nextCenterPoint.y)
        playerOnFloor = person.getZ() - z < 1 or person.getZ() < z
        if playerOnFloor:
            if person.state == PersonState.standing:
                person.setZ(z)
            elif person.state == PersonState.falling:
                person.setZ(z)
                person.fallingTime = 0
                person.state = PersonState.landing
                person.landingTime = 10 * 0.1
                self.eventManager.raiseEvent(Events.personLanded, person)
            elif person.state == PersonState.landing:
                person.landingTime -= 0.1
                if person.landingTime <= 0:
                    person.state = PersonState.standing
                    person.landingTime = 0
            else:
                raise Exception("Wrong player state.")
        else:
            person.state = PersonState.falling
            self.processPersonFall(person)

    def processHole(self, person):
        person.state = PersonState.falling
        self.processPersonFall(person)

    def processPersonFall(self, person):
        person.fallingTime += 0.1
        person.setZ(person.getZ() - person.fallingFunc.getValue(person.fallingTime))
