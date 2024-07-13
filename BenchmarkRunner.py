from line_profiler import LineProfiler
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import game.engine.bsp.BSPTreeTraversal as BSPTreeTraversal
import game.engine.GameUpdater as GameUpdater
import game.engine.LevelSegmentItemFinder as LevelSegmentItemFinder
import game.engine.LevelSegmentVisibilityUpdater as LevelSegmentVisibilityUpdater
import game.engine.PlayerLevelSegmentsUpdater as PlayerLevelSegmentsUpdater


class BenchmarkRunner:

    def run(self, app):
        lp = LineProfiler()
        # lp.add_module(GameUpdater)
        # lp.add_module(LevelSegmentItemFinder)
        # lp.add_module(BSPTreeTraversal)
        lp.add_module(LevelSegmentVisibilityUpdater)
        # lp.add_module(LevelSegmentItemFinder)
        # lp.add_module(PlayerLevelSegmentsUpdater)
        lp(app.run)()
        lp.print_stats()
