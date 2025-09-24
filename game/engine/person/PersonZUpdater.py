from game.anx.Events import Events
from game.engine.GameData import GameData
from game.engine.person.PersonDamageLogic import PersonDamageLogic
from game.lib.EventManager import EventManager
from game.lib.Math import Math
from game.lib.Numeric import Numeric
from game.model.level.NullFloor import NullFloor
from game.model.person.PersonStates import PersonZState


class PersonZUpdater:

    def __init__(
        self,
        gameData: GameData,
        personDamageLogic: PersonDamageLogic,
        eventManager: EventManager,
    ):
        self.gameData = gameData
        self.personDamageLogic = personDamageLogic
        self.eventManager = eventManager

    def updateIfMoved(self):
        for person in self.gameData.allPerson:
            if person.hasMoved:
                self.updatePerson(person)

    def update(self):
        for person in self.gameData.allPerson:
            self.updatePerson(person)

    def updatePerson(self, person):
        if person.nextFloor != NullFloor.instance:
            floorZ = person.nextFloor.getZ(person.nextCenterPoint.x, person.nextCenterPoint.y)
            personOnFloor = Numeric.between(person.getZ() - floorZ, -0.4, 0.4)
        else:
            floorZ = None
            personOnFloor = False

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
            self.personDamageLogic.damageByFalling(person)
            person.landingTime = 0.8 * person.fallingTime
            person.fallingTime = 0
            person.zState = PersonZState.landing
            if person.landingTime > 0.9:
                self.eventManager.raiseEvent(Events.personLanded, person)
        elif personOnFloor and person.zState == PersonZState.landing:
            person.landingTime -= 0.1
            if person.landingTime <= 0:
                person.zState = PersonZState.onFloor
                person.landingTime = 0
        elif not personOnFloor:
            person.zState = PersonZState.falling
            person.fallingTime += 0.1
            personZ = person.getZ() - person.fallingFunc.getValue(person.fallingTime)
            if floorZ is not None:
                person.setZ(Math.max(personZ, floorZ))
            else:
                person.setZ(personZ)
        else:
            raise Exception("Wrong person state.")
