from game.anx.Events import Events
from game.anx.PersonConstants import PersonConstants
from game.engine.GameData import GameData
from game.lib.EventManager import EventManager
from game.lib.Math import Math
from game.model.person.PersonStates import WeaponSelectState
from game.model.weapon.NullWeapon import NullWeapon


class PersonSelectedWeaponPositionUpdater:

    def __init__(
        self,
        gameData: GameData,
        eventManager: EventManager,
    ):
        self.gameData = gameData
        self.eventManager = eventManager

    def update(self):
        for person, personItems in self.gameData.allPersonItems.items():
            self.updateForPerson(person, personItems)

    def updateForPerson(self, person, personItems):
        if person.weaponSelectState is None:
            return

        # startSelection
        if person.weaponSelectState == WeaponSelectState.startSelection:
            if personItems.currentWeapon != NullWeapon.instance:
                self.eventManager.raiseEvent(Events.weaponPutDown, (person, personItems.currentWeapon))
                person.weaponSelectState = WeaponSelectState.putWeaponDown
            else:
                person.weaponSelectState = WeaponSelectState.startRaising
        # putWeaponDown
        elif person.weaponSelectState == WeaponSelectState.putWeaponDown:
            self.rotateCurrentWeapon(personItems, -PersonConstants.weaponSelectRadianStep)
            if personItems.currentWeapon.selectionPitchRadians <= -Math.piHalf:
                person.weaponSelectState = WeaponSelectState.startRaising
        # startRaising
        elif person.weaponSelectState == WeaponSelectState.startRaising:
            personItems.setSelectedWeaponAsCurrent()
            personItems.resetSelectedWeapon()
            if personItems.currentWeapon != NullWeapon.instance:
                self.setCurrentWeaponSelectionPitchRadians(personItems, -Math.piHalf)
                self.eventManager.raiseEvent(Events.weaponRaised, (person, personItems.currentWeapon))
                person.weaponSelectState = WeaponSelectState.raiseWeaponUp
            else:
                person.weaponSelectState = None
        # raiseWeaponUp
        elif person.weaponSelectState == WeaponSelectState.raiseWeaponUp:
            self.rotateCurrentWeapon(personItems, PersonConstants.weaponSelectRadianStep)
            if personItems.currentWeapon.selectionPitchRadians >= 0:
                person.weaponSelectState = None
                self.setCurrentWeaponSelectionPitchRadians(personItems, 0)

    def setCurrentWeaponSelectionPitchRadians(self, personItems, radians):
        personItems.rightHandWeapon.selectionPitchRadians = radians
        if personItems.leftHandWeapon is not None:
            personItems.leftHandWeapon.selectionPitchRadians = radians

    def rotateCurrentWeapon(self, personItems, radians):
        personItems.rightHandWeapon.selectionPitchRadians += radians
        if personItems.leftHandWeapon is not None:
            personItems.leftHandWeapon.selectionPitchRadians += radians
