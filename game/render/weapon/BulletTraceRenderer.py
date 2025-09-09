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
        traces = self.getVisibleTracesDictionary()
        if len(traces) == 0:
            return

        for traceType, traces in traces.items():
            if traceType in self.renderers:
                renderer = self.renderers[traceType]
                renderer.renderTraces(traces)

    def getVisibleTracesDictionary(self):
        result = {}
        for levelSegment in self.gameData.visibleLevelSegments:
            for trace in levelSegment.bulletTraces:
                if type(trace) in result:
                    result[type(trace)].add(trace)
                else:
                    result[type(trace)] = set([trace])

        return result
