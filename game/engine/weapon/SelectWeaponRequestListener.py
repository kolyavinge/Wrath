from game.anx.Events import Events
from game.engine.weapon.WeaponSelector import WeaponSelector
from game.lib.EventManager import EventManager
from game.model.weapon.WeaponCollection import WeaponCollection


class SelectWeaponRequestListener:

    def __init__(
        self,
        weaponSelector: WeaponSelector,
        eventManager: EventManager,
    ):
        self.weaponSelector = weaponSelector
        eventManager.attachToEvent(Events.selectWeaponRequested, self.onSelectWeaponRequested)
        eventManager.attachToEvent(Events.selectNextWeaponRequested, self.onSelectNextWeaponRequested)
        eventManager.attachToEvent(Events.selectPrevWeaponRequested, self.onSelectPrevWeaponRequested)

    def onSelectWeaponRequested(self, args):
        person, weaponNumber = args
        requestedWeaponType = WeaponCollection.getWeaponTypeByNumber(weaponNumber)
        self.weaponSelector.selectWeaponByType(person, requestedWeaponType)

    def onSelectNextWeaponRequested(self, person):
        self.weaponSelector.selectNextWeapon(person)

    def onSelectPrevWeaponRequested(self, person):
        self.weaponSelector.selectPrevWeapon(person)
