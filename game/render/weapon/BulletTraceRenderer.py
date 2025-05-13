from OpenGL.GL import *

from game.engine.GameData import GameData
from game.model.weapon.Pistol import PistolBulletTrace
from game.model.weapon.Railgun import RailgunBulletTrace
from game.model.weapon.Rifle import RifleBulletTrace
from game.model.weapon.Sniper import SniperBulletTrace
from game.render.weapon.trace.RailgunBulletTraceRenderer import *
from game.render.weapon.trace.RifleBulletTraceRenderer import *
from game.render.weapon.trace.SniperBulletTraceRenderer import SniperBulletTraceRenderer


class BulletTraceRenderer:

    def __init__(
        self,
        gameData: GameData,
        rifleBulletTraceRenderer: RifleBulletTraceRenderer,
        railgunBulletTraceRenderer: RailgunBulletTraceRenderer,
        sniperBulletTraceRenderer: SniperBulletTraceRenderer,
    ):
        self.gameData = gameData
        self.renderers = {}
        self.renderers[PistolBulletTrace] = rifleBulletTraceRenderer
        self.renderers[RifleBulletTrace] = rifleBulletTraceRenderer
        self.renderers[RailgunBulletTrace] = railgunBulletTraceRenderer
        self.renderers[SniperBulletTrace] = sniperBulletTraceRenderer

    def render(self):
        traces = self.getVisibleTraces()
        if len(traces) == 0:
            return

        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnable(GL_BLEND)
        glEnable(GL_ALPHA_TEST)
        glEnable(GL_DEPTH_TEST)

        for trace in traces:
            if type(trace) in self.renderers:
                renderer = self.renderers[type(trace)]
                renderer.renderTrace(trace)

        glDisable(GL_DEPTH_TEST)
        glDisable(GL_ALPHA_TEST)
        glDisable(GL_BLEND)

    def getVisibleTraces(self):
        result = set()
        for levelSegment in self.gameData.visibleLevelSegments:
            for trace in levelSegment.bulletTraces:
                result.add(trace)

        return result


def makeBulletTraceRenderer(resolver):
    return BulletTraceRenderer(
        resolver.resolve(GameData),
        resolver.resolve(RifleBulletTraceRenderer),
        resolver.resolve(RailgunBulletTraceRenderer),
        resolver.resolve(SniperBulletTraceRenderer),
    )
