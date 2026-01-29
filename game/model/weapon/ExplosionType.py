from game.model.weapon.ExplosionKind import ExplosionKind
from game.model.weapon.Launcher import LauncherExplosion
from game.model.weapon.Plasma import PlasmaExplosion


class ExplosionType:

    @staticmethod
    def getExplosionTypeFromKind(kind):
        kinds = {
            ExplosionKind.plasmaExplosion: PlasmaExplosion,
            ExplosionKind.launcherExplosion: LauncherExplosion,
        }

        return kinds[kind]
