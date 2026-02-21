from game.lib.Random import Random


class BurstFireLogic:

    def fire(self, bot, botItems):
        aiData = bot.aiData
        if aiData.fireDelayRemain.isExpired() and aiData.fireBurstRemain.isExpired():
            weapon = botItems.currentWeapon
            aiData.fireBurstRemain.set(Random.getInt(weapon.minBurstCount, weapon.maxBurstCount))
            return True

        aiData.fireDelayRemain.decrease()
        if not aiData.fireDelayRemain.isExpired():
            return False

        if botItems.currentWeapon.isFiring:
            aiData.fireBurstRemain.decrease()
            if aiData.fireBurstRemain.isExpired():
                aiData.fireDelayRemain.set(Random.getInt(10, 50))

        return True
