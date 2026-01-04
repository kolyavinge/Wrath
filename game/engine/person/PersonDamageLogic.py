from game.anx.PersonConstants import PersonConstants
from game.engine.GameState import GameState


class PersonDamageLogic:

    def __init__(self, gameState: GameState):
        self.gameState = gameState

    def damageByBullet(self, person, bullet):
        self.gameState.collisionData.personBullet[person] = bullet
        self.damage(person, bullet.damagePercent)

    def damageByHeadshot(self, person, bullet):
        self.gameState.collisionData.personBullet[person] = bullet
        person.damage(PersonConstants.maxPersonHealth)

    def damageByRay(self, person, ray):
        self.gameState.collisionData.personRay[person] = ray
        self.damage(person, ray.damagePercent)

    def damageByExplosion(self, person, explosion):
        self.gameState.collisionData.personExplosion[person] = explosion
        personItems = self.gameState.allPersonItems[person]
        if personItems.vest > 0:
            personItems.damageVest(explosion.damagePercent * PersonConstants.maxVest)
            person.damage((explosion.damagePercent * PersonConstants.maxPersonHealth) / 2.0)
        else:
            person.damage(explosion.damagePercent * PersonConstants.maxPersonHealth)

    def damageByFalling(self, person):
        damagePercent = person.fallingDamageFunc.getValue(person.fallingTime)
        if damagePercent > 0:
            self.gameState.collisionData.personFalling.add(person)
            person.damage(damagePercent * PersonConstants.maxPersonHealth)

    def damage(self, person, damagePercent):
        personItems = self.gameState.allPersonItems[person]
        if personItems.vest > 0:
            personItems.damageVest(damagePercent * PersonConstants.maxVest)
            person.damage((damagePercent * PersonConstants.maxPersonHealth) / 2.0)
        else:
            person.damage(damagePercent * PersonConstants.maxPersonHealth)
