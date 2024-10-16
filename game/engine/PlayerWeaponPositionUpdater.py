from game.engine.GameData import GameData


class PlayerWeaponPositionUpdater:

    def __init__(self, gameData):
        self.gameData = gameData

    def update(self):
        player = self.gameData.player

        frontShift = player.lookDirection.copy()
        frontShift.mul(0.1)
        rightShift = player.rightNormal.copy()
        rightShift.mul(0.05)
        topShift = player.lookDirectionNormal.copy()
        topShift.mul(-0.1)
        newPosition = player.eyePosition.copy()
        newPosition.add(frontShift)
        newPosition.add(rightShift)
        newPosition.add(topShift)

        weapon = self.gameData.playerItems.currentWeapon
        weapon.position = newPosition
        weapon.direction = player.lookDirection
        weapon.yawRadians = player.yawRadians
        weapon.pitchRadians = player.pitchRadians


def makePlayerWeaponPositionUpdater(resolver):
    return PlayerWeaponPositionUpdater(resolver.resolve(GameData))
