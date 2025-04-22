from line_profiler import LineProfiler
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import game.engine.bsp.BSPTreeTraversal as BSPTreeTraversal
import game.engine.GameUpdater as GameUpdater
import game.engine.LevelSegmentItemFinder as LevelSegmentItemFinder
import game.engine.LevelSegmentVisibilityUpdater as LevelSegmentVisibilityUpdater
import game.engine.PersonLevelSegmentsUpdater as PersonLevelSegmentsUpdater
from game.calc.TransformMatrix4 import TransformMatrix4
from game.gl.model3d.AnimationPlayer import AnimationPlayer
from game.gl.ShaderProgram import ShaderProgram
from game.render.common.MainSceneLightComponentsShaderProgram import *
from game.render.level.LevelSegmentRenderer import LevelSegmentRenderer
from game.render.main.MainSceneRenderer import MainSceneRenderer
from game.render.person.EnemyRenderer import EnemyRenderer


class BenchmarkRunner:

    def run(self, app):
        lp = LineProfiler()
        # lp.add_module(GameUpdater)
        # lp.add_module(LevelSegmentItemFinder)
        # lp.add_module(BSPTreeTraversal)
        # lp.add_module(MainSceneRenderer)
        # lp.add_module(LevelSegmentRenderer)
        # lp.add_module(MainSceneLightComponentsShaderProgram)
        lp.add_module(AnimationPlayer)
        # lp.add_module(EnemyRenderer)
        # lp.add_module(TransformMatrix4)
        # lp.add_module(LevelSegmentItemFinder)
        # lp.add_module(PersonLevelSegmentsUpdater)
        lp(app.run)()
        lp.print_stats()
