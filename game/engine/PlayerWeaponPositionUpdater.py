from game.anx.PersonConstants import PersonConstants
from game.engine.GameData import GameData


class PlayerWeaponPositionUpdater:

    def __init__(self, gameData):
        self.gameData = gameData

    def update(self):
        playerItems = self.gameData.playerItems
        self.updateWeapon(playerItems.rightHandWeapon, rightHand=True)
        if playerItems.leftHandWeapon is not None:
            self.updateWeapon(playerItems.leftHandWeapon, rightHand=False)

    def updateWeapon(self, weapon, rightHand):
        player = self.gameData.player
        weaponPosition = self.getWeaponPosition(player, weapon, rightHand)
        barrelPosition = self.getBarrelPosition(player, weapon, weaponPosition, rightHand)
        aimPoint = self.getAimPoint(player, barrelPosition)

        weapon.position = weaponPosition
        weapon.barrelPosition = barrelPosition
        weapon.direction = weapon.position.getDirectionTo(aimPoint)
        weapon.direction.normalize()
        weapon.direction.add(weapon.jitter)
        weapon.direction.normalize()
        weapon.yawRadians = player.yawRadians
        weapon.pitchRadians = player.pitchRadians

        if not weapon.jitter.isZero():
            weapon.jitter.mul(weapon.jitterFade)

        if not weapon.feedback.isZero():
            weapon.feedback.mul(weapon.feedbackFade)

    def getWeaponPosition(self, player, weapon, rightHand):
        rightShift = player.rightNormal.copy()
        rightShift.mul(weapon.playerShift.x)
        if not rightHand:
            rightShift.mul(-1)
        frontShift = player.lookDirection.copy()
        frontShift.mul(weapon.playerShift.y)
        topShift = player.lookDirectionNormal.copy()
        topShift.mul(weapon.playerShift.z)
        weaponPosition = player.eyePosition.copy()
        weaponPosition.add(rightShift)
        weaponPosition.add(frontShift)
        weaponPosition.add(topShift)
        weaponPosition.add(weapon.feedback)

        return weaponPosition

    def getBarrelPosition(self, player, weapon, weaponPosition, rightHand):
        rightShift = player.rightNormal.copy()
        rightShift.mul(weapon.barrelPoint.x)
        if not rightHand:
            rightShift.mul(-1)
        frontShift = player.lookDirection.copy()
        frontShift.mul(weapon.barrelPoint.y)
        topShift = player.lookDirectionNormal.copy()
        topShift.mul(weapon.barrelPoint.z)
        barrelPosition = weaponPosition.copy()
        barrelPosition.add(rightShift)
        barrelPosition.add(frontShift)
        barrelPosition.add(topShift)

        return barrelPosition

    def getAimPoint(self, player, barrelPosition):
        aimPoint = player.lookDirection.copy()
        aimPoint.setLength(PersonConstants.aimLength)
        aimPoint.add(barrelPosition)

        return aimPoint


def makePlayerWeaponPositionUpdater(resolver):
    return PlayerWeaponPositionUpdater(resolver.resolve(GameData))
