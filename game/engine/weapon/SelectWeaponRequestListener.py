from game.engine.weapon.WeaponSelector import WeaponSelector
from game.lib.EventManager import EventManager, Events
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
        person, personItems, weaponNumber = args
        requestedWeaponType = WeaponCollection.getWeaponTypeByNumber(weaponNumber)
        self.weaponSelector.selectWeaponByType(person, personItems, requestedWeaponType)

    def onSelectNextWeaponRequested(self, args):
        person, personItems = args
        self.weaponSelector.selectNextWeapon(person, personItems)

    def onSelectPrevWeaponRequested(self, args):
        person, personItems = args
        self.weaponSelector.selectPrevWeapon(person, personItems)
