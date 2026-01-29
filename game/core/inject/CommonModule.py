from game.anx.BulletIdLogic import *
from game.anx.ExplosionIdLogic import *
from game.anx.PersonIdLogic import *
from game.anx.PowerupIdLogic import *
from game.lib.EventManager import *
from game.lib.FileSystem import *


class CommonModule:

    def init(self, binder):
        binder.bindSingleton(BulletIdLogic)
        binder.bindSingleton(ExplosionIdLogic)
        binder.bindSingleton(PersonIdLogic)
        binder.bindSingleton(PowerupIdLogic)
        binder.bindSingleton(EventManager)
        binder.bindSingleton(FileSystem)
