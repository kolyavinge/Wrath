from game.anx.PersonConstants import PersonConstants
from game.engine.GameData import GameData


class PersonDamageLogic:

    def __init__(self, gameData: GameData):
        self.gameData = gameData

    def damageByBullet(self, person, bullet):
        self.gameData.collisionData.personBullet[person] = bullet
        self.damage(person, bullet.damagePercent)

    def damageByHeadshot(self, person, bullet):
        self.gameData.collisionData.personBullet[person] = bullet
        person.damage(PersonConstants.maxPersonHealth)

    def damageByRay(self, person, ray):
        self.gameData.collisionData.personRay[person] = ray
        self.damage(person, ray.damagePercent)

    def damageByExplosion(self, person, explosion):
        self.gameData.collisionData.personExplosion[person] = explosion
        personItems = self.gameData.allPersonItems[person]
        if personItems.vest > 0:
            personItems.damageVest(explosion.damagePercent * PersonConstants.maxVest)
            person.damage((explosion.damagePercent * PersonConstants.maxPersonHealth) / 2.0)
        else:
            person.damage(explosion.damagePercent * PersonConstants.maxPersonHealth)

    def damageByFalling(self, person):
        damagePercent = person.fallingDamageFunc.getValue(person.fallingTime)
        if damagePercent > 0:
            self.gameData.collisionData.personFalling.add(person)
            person.damage(damagePercent * PersonConstants.maxPersonHealth)

    def damage(self, person, damagePercent):
        personItems = self.gameData.allPersonItems[person]
        if personItems.vest > 0:
            personItems.damageVest(damagePercent * PersonConstants.maxVest)
            person.damage((damagePercent * PersonConstants.maxPersonHealth) / 2.0)
        else:
            person.damage(damagePercent * PersonConstants.maxPersonHealth)
