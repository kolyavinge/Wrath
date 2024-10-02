from game.lib.EventManager import *


class LibModule:

    def init(self, binder):
        binder.bindSingleton(EventManager, makeEventManager)
