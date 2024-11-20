from game.model.weapon.Launcher import Launcher
from game.model.weapon.Pistol import Pistol
from game.model.weapon.Plasma import Plasma
from game.model.weapon.Railgun import Railgun
from game.model.weapon.Rifle import Rifle
from game.model.weapon.Sniper import Sniper


class WeaponAudioSources:

    def __init__(self, person, audioSourceFactory):
        self.person = person
        self.weapons = {}
        self.weapons[Pistol] = audioSourceFactory.makePistolShot()
        self.weapons[Pistol].setGain(0.8)
        self.weapons[Rifle] = audioSourceFactory.makeRifleShot()
        self.weapons[Plasma] = audioSourceFactory.makeRifleShot()
        self.weapons[Launcher] = audioSourceFactory.makeLauncherShot()
        self.weapons[Railgun] = audioSourceFactory.makeRifleShot()
        self.weapons[Sniper] = audioSourceFactory.makeSniperShot()
        self.weapons[Sniper].setGain(0.8)

    def updatePosition(self):
        position = self.person.currentCenterPoint
        for weapon in self.weapons.values():
            weapon.setPosition(position)

    def release(self):
        for weapon in self.weapons.values():
            weapon.release()
