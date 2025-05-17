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
        def onSelectWeaponRequested(args):
            person, weaponNumber = args
            requestedWeaponType = WeaponCollection.getWeaponTypeByNumber(weaponNumber)
            weaponSelector.selectWeaponByType(person, requestedWeaponType)

        eventManager.attachToEvent(Events.selectWeaponRequested, onSelectWeaponRequested)
