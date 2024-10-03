from line_profiler import LineProfiler
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import game.engine.bsp.BSPTreeTraversal as BSPTreeTraversal
import game.engine.GameUpdater as GameUpdater
import game.engine.LevelSegmentItemFinder as LevelSegmentItemFinder
import game.engine.LevelSegmentVisibilityUpdater as LevelSegmentVisibilityUpdater
import game.engine.PlayerLevelSegmentsUpdater as PlayerLevelSegmentsUpdater
from game.gl.ShaderProgram import ShaderProgram
from game.render.common.MainSceneLightComponentsShaderProgram import *
from game.render.level.LevelRenderer import LevelRenderer
from game.render.main.MainSceneRenderer import MainSceneRenderer


class BenchmarkRunner:

    def run(self, app):
        lp = LineProfiler()
        # lp.add_module(GameUpdater)
        # lp.add_module(LevelSegmentItemFinder)
        # lp.add_module(BSPTreeTraversal)
        # lp.add_module(MainSceneRenderer)
        # lp.add_module(LevelRenderer)
        # lp.add_module(MainSceneLightComponentsShaderProgram)
        lp.add_module(ShaderProgram)
        # lp.add_module(LevelSegmentItemFinder)
        # lp.add_module(PlayerLevelSegmentsUpdater)
        lp(app.run)()
        lp.print_stats()
