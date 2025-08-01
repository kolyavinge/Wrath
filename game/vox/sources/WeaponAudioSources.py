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
        self.reloads[Sniper].setGain(0.6)

        self.putdown = {}
        self.putdown[Pistol] = audioSourceFactory.makeWeaponPutdown()
        self.putdown[Rifle] = self.putdown[Pistol]
        self.putdown[Plasma] = self.putdown[Pistol]
        self.putdown[Launcher] = self.putdown[Pistol]
        self.putdown[Railgun] = self.putdown[Pistol]
        self.putdown[Sniper] = self.putdown[Pistol]

        self.raises = {}
        self.raises[Pistol] = audioSourceFactory.makePistolRaise()
        self.raises[Rifle] = audioSourceFactory.makeRifleRaise()
        self.raises[Plasma] = audioSourceFactory.makePlasmaRaise()
        self.raises[Launcher] = audioSourceFactory.makeLauncherRaise()
        self.raises[Railgun] = audioSourceFactory.makeRailgunRaise()
        self.raises[Railgun].setGain(0.8)
        self.raises[Sniper] = audioSourceFactory.makeSniperRaise()
        self.raises[Sniper].setGain(0.8)

    def updatePosition(self):
        position = self.person.currentCenterPoint
        for shot in self.shots.values():
            shot.setPosition(position)
        for reload in self.reloads.values():
            reload.setPosition(position)
        for putdown in self.putdown.values():
            putdown.setPosition(position)
        for raise_ in self.raises.values():
            raise_.setPosition(position)

    def release(self):
        for shot in self.shots.values():
            shot.release()
        for reload in self.reloads.values():
            reload.release()
        for putdown in self.putdown.values():
            putdown.release()
        for raise_ in self.raises.values():
            raise_.release()
