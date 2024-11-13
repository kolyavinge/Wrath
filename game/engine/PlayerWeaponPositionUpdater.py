from game.anx.PlayerConstants import PlayerConstants
from game.engine.GameData import GameData


class PlayerWeaponPositionUpdater:

    def __init__(self, gameData):
        self.gameData = gameData

    def update(self):
        player = self.gameData.player
        weapon = self.gameData.playerItems.currentWeapon

        rightShift = player.rightNormal.copy()
        rightShift.mul(weapon.playerShift.x)
        frontShift = player.lookDirection.copy()
        frontShift.mul(weapon.playerShift.y)
        topShift = player.lookDirectionNormal.copy()
        topShift.mul(weapon.playerShift.z)
        weaponPosition = player.eyePosition.copy()
        weaponPosition.add(rightShift)
        weaponPosition.add(frontShift)
        weaponPosition.add(topShift)
        weaponPosition.add(weapon.feedback)

        rightShift = player.rightNormal.copy()
        rightShift.mul(weapon.barrelPoint.x)
        frontShift = player.lookDirection.copy()
        frontShift.mul(weapon.barrelPoint.y)
        topShift = player.lookDirectionNormal.copy()
        topShift.mul(weapon.barrelPoint.z)
        barrelPosition = weaponPosition.copy()
        barrelPosition.add(rightShift)
        barrelPosition.add(frontShift)
        barrelPosition.add(topShift)

        aimPoint = player.lookDirection.copy()
        aimPoint.setLength(PlayerConstants.aimLength)
        aimPoint.add(barrelPosition)

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


def makePlayerWeaponPositionUpdater(resolver):
    return PlayerWeaponPositionUpdater(resolver.resolve(GameData))
