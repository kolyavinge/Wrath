from game.anx.BulletIdLogic import *
from game.anx.ConfigManager import *
from game.anx.PersonIdLogic import *
from game.anx.PowerupIdLogic import *
from game.lib.EventManager import *
from game.lib.FileSystem import *
from game.lib.NetPortManager import *


class CommonModule:

    def init(self, binder):
        binder.bindSingleton(BulletIdLogic)
        binder.bindSingleton(ConfigManager)
        binder.bindSingleton(PersonIdLogic)
        binder.bindSingleton(PowerupIdLogic)
        binder.bindSingleton(EventManager)
        binder.bindSingleton(FileSystem)
        binder.bindSingleton(NetPortManager)
