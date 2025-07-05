from game.anx.Events import Events
from game.anx.PersonConstants import PersonConstants
from game.engine.GameData import GameData
from game.lib.EventManager import EventManager
from game.lib.Math import Math
from game.lib.Numeric import Numeric
from game.model.weapon.NullWeapon import NullWeapon


class PlayerSelectedWeaponPositionUpdater:

    def __init__(
        self,
        gameData: GameData,
        eventManager: EventManager,
    ):
        self.gameData = gameData
        self.eventManager = eventManager
        self.radianStep = Math.piHalf / PersonConstants.selectWeaponDelayHalf

    def update(self):
        if self.gameData.player.selectWeaponDelay.isExpired():
            return
        player = self.gameData.player
        # -1 чтобы на последнем шаге delay равнялся нулю и следовательно значение radians в raiseWeapon() тоже равнялось нулю
        delay = player.selectWeaponDelay.value - 1
        personItems = self.gameData.playerItems
        if player.selectWeaponDelay.value == PersonConstants.selectWeaponDelay and type(personItems.currentWeapon) != NullWeapon:
            self.eventManager.raiseEvent(Events.weaponPutDown, (player, personItems.currentWeapon))
        elif Numeric.between(delay, PersonConstants.selectWeaponDelayHalf + 1, PersonConstants.selectWeaponDelay):
            self.putWeaponDown(delay, personItems)
        elif delay == PersonConstants.selectWeaponDelayHalf:
            self.setSelectedWeaponAsCurrent(personItems)
            if type(personItems.currentWeapon) != NullWeapon:
                self.eventManager.raiseEvent(Events.weaponRaised, (player, personItems.currentWeapon))
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
