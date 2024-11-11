from game.anx.CommonConstants import CommonConstants
from game.calc.Geometry import Geometry
from game.engine.GameData import GameData
from game.lib.Math import Math
from game.lib.mirrorRange import mirrorRange
from game.model.person.PlayerState import PlayerState


class PlayerWeaponPositionSwingLogic:

    def __init__(self, gameData):
        self.gameData = gameData
        stepsCount = 15
        stepValue = Math.pi / stepsCount
        self.steps = [v for v in mirrorRange(stepValue, stepsCount)]
        self.lastStep = 0

    def updateSwing(self):
        self.updateMovingSwing()
        self.updateLandingSwing()

    def updateMovingSwing(self):
        player = self.gameData.player
        if player.state != PlayerState.standing:
            self.lastStep = 0
        elif player.velocityValue == 0:
            self.lastStep = 0
        else:
            self.lastStep += 1
            if self.lastStep == len(self.steps):
                self.lastStep = 0

        radians = self.steps[self.lastStep]
        swing = Geometry.rotatePoint(player.rightNormal, player.frontNormal, CommonConstants.axisOrigin, radians)
        swing.setLength(0.015 * player.velocityValue)

        self.gameData.playerItems.currentWeapon.position.add(swing)

    def updateLandingSwing(self):
        player = self.gameData.player
        if player.state == PlayerState.landing:
            swingValue = 0.05 * player.landingTime * Math.sin(player.landingTime)
            self.gameData.playerItems.currentWeapon.position.z -= swingValue


def makePlayerWeaponPositionSwingLogic(resolver):
    return PlayerWeaponPositionSwingLogic(resolver.resolve(GameData))
