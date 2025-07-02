from game.anx.PersonConstants import PersonConstants
from game.engine.GameData import GameData
from game.lib.Math import Math
from game.lib.Numeric import Numeric


class PlayerSelectedWeaponPositionUpdater:

    def __init__(self, gameData: GameData):
        self.gameData = gameData
        self.radianStep = Math.piHalf / PersonConstants.selectWeaponDelayHalf

    def update(self):
        if self.gameData.player.selectWeaponDelay.isExpired():
            return
        player = self.gameData.player
        # -1 чтобы на последнем шаге delay равнялся нулю и следовательно значение radians в raiseWeapon() тоже равнялось нулю
        delay = player.selectWeaponDelay.value - 1
        personItems = self.gameData.playerItems
        if Numeric.between(delay, PersonConstants.selectWeaponDelayHalf + 1, PersonConstants.selectWeaponDelay):
            self.putWeaponDown(delay, personItems)
        elif delay == PersonConstants.selectWeaponDelayHalf:
            self.setSelectedWeaponAsCurrent(personItems)
        else:
            self.raiseWeapon(delay, personItems)

    def putWeaponDown(self, delay, personItems):
        # правая часть выражения стремится к нулю, radians стремится к pi/2
        # оружие вращается по часовой стрелке, от взгляда игрока до низа
        radians = Math.piHalf - (delay - PersonConstants.selectWeaponDelayHalf) * self.radianStep
        personItems.rightHandWeapon.selectionPitchRadians = -radians
        if personItems.leftHandWeapon is not None:
            personItems.leftHandWeapon.selectionPitchRadians = -radians

    def setSelectedWeaponAsCurrent(self, personItems):
        personItems.rightHandWeapon = personItems.selectedRightHandWeapon
        personItems.leftHandWeapon = personItems.selectedLeftHandWeapon
        personItems.currentWeapon = personItems.selectedCurrentWeapon
        personItems.selectedRightHandWeapon = None
        personItems.selectedLeftHandWeapon = None
        personItems.selectedCurrentWeapon = None

    def raiseWeapon(self, delay, personItems):
        # правая часть выражения стремится к нулю, radians стремится к нулю
        # оружие вращается против часовой стрелки, от низа до взгляда игрока
        radians = 0 - delay * self.radianStep
        personItems.rightHandWeapon.selectionPitchRadians = radians
        if personItems.leftHandWeapon is not None:
            personItems.leftHandWeapon.selectionPitchRadians = radians
