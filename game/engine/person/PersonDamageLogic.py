from game.anx.PersonConstants import PersonConstants


class PersonDamageLogic:

    def damageByBullet(self, person, personItems, bullet, collisionData):
        collisionData.personBullet[person] = bullet
        self.damage(person, personItems, bullet.damagePercent)

    def damageByHeadshot(self, person, bullet, collisionData):
        collisionData.personBullet[person] = bullet
        person.damage(PersonConstants.maxPersonHealth)

    def damageByRay(self, person, personItems, ray, collisionData):
        collisionData.personRay[person] = ray
        self.damage(person, personItems, ray.damagePercent)

    def damageByExplosion(self, person, personItems, explosion, collisionData):
        collisionData.personExplosion[person] = explosion
        if personItems.vest > 0:
            personItems.damageVest(explosion.damagePercent * PersonConstants.maxVest)
            person.damage((explosion.damagePercent * PersonConstants.maxPersonHealth) / 2.0)
        else:
            person.damage(explosion.damagePercent * PersonConstants.maxPersonHealth)

    def damageByFalling(self, person, collisionData):
        damagePercent = person.fallingDamageFunc.getValue(person.fallingTime)
        if damagePercent > 0:
            collisionData.personFalling.add(person)
            person.damage(damagePercent * PersonConstants.maxPersonHealth)

    def damage(self, person, personItems, damagePercent):
        if personItems.vest > 0:
            personItems.damageVest(damagePercent * PersonConstants.maxVest)
            person.damage((damagePercent * PersonConstants.maxPersonHealth) / 2.0)
        else:
            person.damage(damagePercent * PersonConstants.maxPersonHealth)
