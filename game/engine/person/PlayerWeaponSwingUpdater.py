from game.anx.CommonConstants import CommonConstants
from game.calc.Geometry import Geometry
from game.engine.GameData import GameData
from game.lib.Math import Math
from game.lib.mirrorRange import mirrorRange
from game.model.person.PersonStates import PersonZState


class PlayerWeaponSwingUpdater:

    def __init__(self, gameData: GameData):
        self.gameData = gameData
        stepsCount = 15
        stepValue = Math.pi / stepsCount
        self.steps = [v for v in mirrorRange(stepValue, stepsCount)]
        self.lastStep = 0

    def update(self):
        self.updateMovingSwing()
        self.updateLandingSwing()

    def updateMovingSwing(self):
        player = self.gameData.player
        if player.zState != PersonZState.onFloor:
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

        self.gameData.playerItems.rightHandWeapon.position.add(swing)
        if self.gameData.playerItems.leftHandWeapon is not None:
            self.gameData.playerItems.leftHandWeapon.position.add(swing)

    def updateLandingSwing(self):
        player = self.gameData.player
        if player.zState == PersonZState.landing:
            swingValue = 0.05 * player.landingTime * Math.sin(player.landingTime)
            self.gameData.playerItems.rightHandWeapon.position.z -= swingValue
            if self.gameData.playerItems.leftHandWeapon is not None:
                self.gameData.playerItems.leftHandWeapon.position.z -= swingValue
