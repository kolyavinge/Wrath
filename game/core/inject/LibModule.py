from game.lib.EventManager import *
from game.lib.FileSystem import *


class LibModule:

    def init(self, binder):
        binder.bindSingleton(EventManager)
        binder.bindSingleton(FileSystem)
