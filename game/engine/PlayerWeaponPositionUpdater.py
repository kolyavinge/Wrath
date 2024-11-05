from game.anx.PlayerConstants import PlayerConstants
from game.engine.GameData import GameData


class PlayerWeaponPositionUpdater:

    def __init__(self, gameData):
        self.gameData = gameData

    def update(self):
        player = self.gameData.player
        weapon = self.gameData.playerItems.currentWeapon

        frontShift = player.lookDirection.copy()
        frontShift.mul(weapon.playerFrontShift)
        rightShift = player.rightNormal.copy()
        rightShift.mul(weapon.playerRightShift)
        topShift = player.lookDirectionNormal.copy()
        topShift.mul(-weapon.playerTopShift)
        newPosition = player.eyePosition.copy()
        newPosition.add(frontShift)
        newPosition.add(rightShift)
        newPosition.add(topShift)

        aimPoint = player.lookDirection.copy()
        aimPoint.setLength(PlayerConstants.aimLength)
        aimPoint.add(player.eyePosition)

        weapon.position = newPosition
        weapon.position.add(weapon.feedback)
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
