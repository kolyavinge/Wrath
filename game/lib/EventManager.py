class Events:

    personStepDone = "personStepDone"
    torchSwitched = "torchSwitched"
    personJumped = "personJumped"
    personLanded = "personLanded"

    weaponFired = "weaponFired"
    weaponReloaded = "weaponReloaded"
    weaponPutDown = "weaponPutDown"
    weaponRaised = "weaponRaised"
    bulletHoleAdded = "bulletHoleAdded"

    rayActivated = "rayActivated"
    rayDeactivated = "rayDeactivated"

    powerupPickedUp = "powerupPicked"

    torchSwitchRequested = "torchSwitchRequested"
    selectWeaponRequested = "selectWeaponRequested"
    selectNextWeaponRequested = "selectNextWeaponRequested"
    selectPrevWeaponRequested = "selectPrevWeaponRequested"

    viewportSizeChanged = "viewportSizeChanged"

    aimStateSwitched = "aimStateSwitched"


class EventManager:

    def __init__(self):
        self.handlers = {}

    def raiseEvent(self, event, args=None):
        if event in self.handlers:
            for handler in self.handlers[event]:
                handler(args)

    def attachToEvent(self, event, handler):
        if event in self.handlers:
            self.handlers[event].append(handler)
        else:
            self.handlers[event] = [handler]
