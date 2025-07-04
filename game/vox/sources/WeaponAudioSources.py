from game.model.weapon.Launcher import Launcher
from game.model.weapon.Pistol import Pistol
from game.model.weapon.Plasma import Plasma
from game.model.weapon.Railgun import Railgun
from game.model.weapon.Rifle import Rifle
from game.model.weapon.Sniper import Sniper


class WeaponAudioSources:

    def __init__(self, person, audioSourceFactory):
        self.person = person

        self.shots = {}
        self.shots[Pistol] = audioSourceFactory.makePistolShot()
        self.shots[Pistol].setGain(0.8)
        self.shots[Rifle] = audioSourceFactory.makeRifleShot()
        self.shots[Plasma] = audioSourceFactory.makePlasmaShot()
        self.shots[Launcher] = audioSourceFactory.makeLauncherShot()
        self.shots[Railgun] = audioSourceFactory.makeRailgunShot()
        self.shots[Sniper] = audioSourceFactory.makeSniperShot()
        self.shots[Sniper].setGain(0.8)

        self.reloads = {}
        self.reloads[Sniper] = audioSourceFactory.makeSniperReload()
        self.reloads[Sniper].setGain(0.5)

    def updatePosition(self):
        position = self.person.currentCenterPoint
        for shot in self.shots.values():
            shot.setPosition(position)
        for reload in self.reloads.values():
            reload.setPosition(position)

    def release(self):
        for shot in self.shots.values():
            shot.release()
        for reload in self.reloads.values():
            reload.release()
