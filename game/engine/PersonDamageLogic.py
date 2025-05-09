from game.anx.PersonConstants import PersonConstants
from game.engine.GameData import GameData


class PersonDamageLogic:

    def __init__(self, gameData):
        self.gameData = gameData

    def damageByBullet(self, person, bullet):
        personItems = self.gameData.allPersonItems[person]
        if personItems.vest > 0:
            personItems.damageVest(bullet.damagePercent * PersonConstants.maxVest)
            person.damage((bullet.damagePercent * PersonConstants.maxPersonHealth) / 2.0)
        else:
            person.damage(bullet.damagePercent * PersonConstants.maxPersonHealth)


def makePersonDamageLogic(resolver):
    return PersonDamageLogic(resolver.resolve(GameData))
