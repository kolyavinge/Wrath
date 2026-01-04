from game.engine.GameState import GameState
from game.model.weapon.Debris import DebrisBulletTrace
from game.model.weapon.Launcher import LauncherBulletTrace
from game.model.weapon.Pistol import PistolBulletTrace
from game.model.weapon.Railgun import RailgunBulletTrace
from game.model.weapon.Rifle import RifleBulletTrace
from game.model.weapon.Sniper import SniperBulletTrace
from game.render.weapon.trace.LauncherBulletTraceRenderer import *
from game.render.weapon.trace.RailgunBulletTraceRenderer import *
from game.render.weapon.trace.RifleBulletTraceRenderer import *
from game.render.weapon.trace.SniperBulletTraceRenderer import *


class BulletTraceRenderer:

    def __init__(
        self,
        gameState: GameState,
        rifleBulletTraceRenderer: RifleBulletTraceRenderer,
        launcherBulletTraceRenderer: LauncherBulletTraceRenderer,
        railgunBulletTraceRenderer: RailgunBulletTraceRenderer,
        sniperBulletTraceRenderer: SniperBulletTraceRenderer,
    ):
        self.gameState = gameState
        self.renderers = {}
        self.renderers[PistolBulletTrace] = rifleBulletTraceRenderer
        self.renderers[RifleBulletTrace] = rifleBulletTraceRenderer
        self.renderers[LauncherBulletTrace] = launcherBulletTraceRenderer
        self.renderers[RailgunBulletTrace] = railgunBulletTraceRenderer
        self.renderers[SniperBulletTrace] = sniperBulletTraceRenderer
        self.renderers[DebrisBulletTrace] = rifleBulletTraceRenderer

    def render(self):
        visibleTraces = self.getVisibleTracesDictionary()
        if len(visibleTraces) == 0:
            return

        for traceType, traces in visibleTraces.items():
            self.renderers[traceType].renderTraces(traces)

    def getVisibleTracesDictionary(self):
        result = {}
        for levelSegment in self.gameState.visibleLevelSegments:
            for trace in levelSegment.bulletTraces:
                if type(trace) in result:
                    result[type(trace)].add(trace)
                else:
                    result[type(trace)] = set([trace])

        return result
