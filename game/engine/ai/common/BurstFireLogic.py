from game.lib.Random import Random


class BurstFireLogic:

    def fire(self, enemy, enemyItems):
        aiData = enemy.aiData
        if aiData.fireDelayRemain.isExpired() and aiData.fireBurstRemain.isExpired():
            weapon = enemyItems.currentWeapon
            aiData.fireBurstRemain.set(Random.getInt(weapon.minBurstCount, weapon.maxBurstCount))
            return True

        aiData.fireDelayRemain.decrease()
        if not aiData.fireDelayRemain.isExpired():
            return False

        if enemyItems.currentWeapon.isFiring:
            aiData.fireBurstRemain.decrease()
            if aiData.fireBurstRemain.isExpired():
                aiData.fireDelayRemain.set(Random.getInt(10, 50))

        return True
