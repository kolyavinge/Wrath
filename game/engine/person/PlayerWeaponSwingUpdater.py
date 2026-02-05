from game.anx.CommonConstants import CommonConstants
from game.calc.Geometry import Geometry
from game.lib.Math import Math
from game.lib.mirrorRange import mirrorRange
from game.model.person.PersonStates import PersonZState


class PlayerWeaponSwingUpdater:

    def __init__(self):
        stepsCount = 10
        stepValue = Math.pi / stepsCount
        self.steps = [v for v in mirrorRange(stepValue, stepsCount)]
        self.lastStep = 0

    def update(self, gameState):
        self.updateMovingSwing(gameState)
        self.updateLandingSwing(gameState)

    def updateMovingSwing(self, gameState):
        player = gameState.player
        if player.zState != PersonZState.onFloor:
            self.lastStep = 0
        elif player.velocityValue == 0:
            self.lastStep = 0
        else:
            self.lastStep += 1.0 * gameState.playerItems.currentWeapon.slowdownCoeff
            if self.lastStep >= len(self.steps):
                self.lastStep = 0

        radians = self.steps[int(self.lastStep)]
        swing = Geometry.rotatePoint(player.rightNormal, player.frontNormal, CommonConstants.axisOrigin, radians)
        swing.setLength(0.015 * player.velocityValue)

        gameState.playerItems.rightHandWeapon.position.add(swing)
        if gameState.playerItems.leftHandWeapon is not None:
            gameState.playerItems.leftHandWeapon.position.add(swing)

    def updateLandingSwing(self, gameState):
        player = gameState.player
        if player.zState == PersonZState.landing:
            swingValue = 0.05 * player.landingTime * Math.sin(player.landingTime)
            gameState.playerItems.rightHandWeapon.position.z -= swingValue
            if gameState.playerItems.leftHandWeapon is not None:
                gameState.playerItems.leftHandWeapon.position.z -= swingValue
