from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal
from game.engine.GameState import GameState


class BulletTraceUpdater:

    def __init__(
        self,
        gameState: GameState,
        traversal: BSPTreeTraversal,
    ):
        self.gameState = gameState
        self.traversal = traversal

    def update(self):
        for trace in self.gameState.bulletTraces:
            if trace.bullet.traceShift > 0:
                trace.currentPosition = trace.bullet.direction.copy()
                trace.currentPosition.mul(-trace.bullet.traceShift)
                trace.currentPosition.add(trace.bullet.currentPosition)
            else:
                trace.currentPosition = trace.bullet.currentPosition.copy()

            visibilityLevelSegment = self.traversal.findLevelSegmentOrNone(self.gameState.visibilityTree, trace.currentPosition)
            if visibilityLevelSegment not in trace.visibilityLevelSegments:
                visibilityLevelSegment.bulletTraces.append(trace)
                trace.visibilityLevelSegments.add(visibilityLevelSegment)

            trace.update()

            if not trace.isVisible:
                self.gameState.bulletTraces.remove(trace)
                for levelSegment in trace.visibilityLevelSegments:
                    levelSegment.bulletTraces.remove(trace)
