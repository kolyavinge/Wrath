from game.render.debug.DebugRenderer import *


class RenderModule:

    def init(self, binder):
        binder.bindSingleton(DebugRenderer, makeDebugRenderer)
