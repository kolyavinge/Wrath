from game.model.weapon.Rifle import Rifle


class WeaponAudioSources:

    def __init__(self, person, audioSourceFactory):
        self.person = person
        self.weapons = {}
        self.weapons[Rifle] = audioSourceFactory.makeRifleShot()
        self.weapons[Rifle].setGain(0.8)

    def updatePosition(self):
        position = self.person.currentCenterPoint
        for weapon in self.weapons.values():
            weapon.setPosition(position)

    def release(self):
        for weapon in self.weapons.values():
            weapon.release()
