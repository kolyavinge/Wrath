from game.anx.PersonIdLogic import *
from game.lib.EventManager import *
from game.lib.FileSystem import *


class CommonModule:

    def init(self, binder):
        binder.bindSingleton(PersonIdLogic)
        binder.bindSingleton(EventManager)
        binder.bindSingleton(FileSystem)
