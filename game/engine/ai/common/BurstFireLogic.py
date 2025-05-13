from game.lib.Random import Random


class BurstFireLogic:

    def __init__(self):
        self.rand = Random()

    def fire(self, enemy, enemyItems):
        aiData = enemy.aiData
        if aiData.fireDelayRemain == 0 and aiData.fireBurstRemain == 0:
            weapon = enemyItems.currentWeapon
            aiData.fireBurstRemain = self.rand.getInt(weapon.minBurstCount, weapon.maxBurstCount)
            return True

        if aiData.fireDelayRemain > 0:
            aiData.fireDelayRemain -= 1
            return False

        if enemyItems.currentWeapon.isFiring:
            aiData.fireBurstRemain -= 1
            if aiData.fireBurstRemain == 0:
                aiData.fireDelayRemain = self.rand.getInt(10, 50)

        return True
