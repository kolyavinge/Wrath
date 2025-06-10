from game.engine.debug.LevelDebugGameUpdater import LevelDebugGameUpdater
from game.engine.debug.LevelDebugPersonVelocityUpdater import *
from game.engine.GameUpdater import GameUpdater
from game.engine.person.PersonVelocityUpdater import PersonVelocityUpdater
from game.render.debug.LevelDebugGameScreenInitializer import *
from game.render.debug.LevelDebugGameScreenRenderer import LevelDebugGameScreenRenderer
from game.render.debug.LevelDebugLevelSegmentRenderer import *
from game.render.debug.LevelDebugMainSceneRenderer import LevelDebugMainSceneRenderer
from game.render.level.LevelSegmentRenderer import LevelSegmentRenderer
from game.render.main.MainSceneRenderer import MainSceneRenderer
from game.render.ui.GameScreenInitializer import GameScreenInitializer
from game.render.ui.GameScreenRenderer import GameScreenRenderer


class LevelDebugModule:

    def init(self, binder):
        binder.bindSingleton(LevelDebugGameUpdater, sameTypes=[GameUpdater], resolveByFields=True)
        binder.bindSingleton(LevelDebugPersonVelocityUpdater, sameTypes=[PersonVelocityUpdater])
        binder.bindSingleton(LevelDebugGameScreenInitializer, sameTypes=[GameScreenInitializer])
        binder.bindSingleton(LevelDebugGameScreenRenderer, sameTypes=[GameScreenRenderer])
        binder.bindSingleton(LevelDebugLevelSegmentRenderer, sameTypes=[LevelSegmentRenderer])
        binder.bindSingleton(LevelDebugMainSceneRenderer, sameTypes=[MainSceneRenderer])
