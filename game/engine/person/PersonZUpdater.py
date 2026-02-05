from game.engine.person.PersonDamageLogic import PersonDamageLogic
from game.lib.Math import Math
from game.lib.Numeric import Numeric
from game.model.level.NullFloor import NullFloor
from game.model.person.PersonStates import PersonZState


class PersonZUpdater:

    def __init__(
        self,
        personDamageLogic: PersonDamageLogic,
    ):
        self.personDamageLogic = personDamageLogic

    def updateIfMovedForPlayer(self, gameState):
        if gameState.player.hasMoved:
            self.updatePerson(gameState.player, gameState.collisionData, gameState.updateStatistic)

    def updateIfMovedForEnemies(self, gameState):
        for enemy in gameState.enemies:
            if enemy.hasMoved:
                self.updatePerson(enemy, gameState.collisionData, gameState.updateStatistic)

    def updatePerson(self, person, collisionData, updateStatistic):
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
            self.personDamageLogic.damageByFalling(person, collisionData)
            person.landingTime = 0.8 * person.fallingTime
            person.fallingTime = 0
            person.zState = PersonZState.landing
            if person.landingTime > 0.6:
                updateStatistic.landedPerson.append(person)
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
