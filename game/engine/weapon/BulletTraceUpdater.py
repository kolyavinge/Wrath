from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal


class BulletTraceUpdater:

    def __init__(
        self,
        traversal: BSPTreeTraversal,
    ):
        self.traversal = traversal

    def update(self, gameState):
        for trace in gameState.bulletTraces:
            if trace.bullet.traceShift > 0:
                trace.currentPosition = trace.bullet.direction.copy()
                trace.currentPosition.mul(-trace.bullet.traceShift)
                trace.currentPosition.add(trace.bullet.currentPosition)
            else:
                trace.currentPosition = trace.bullet.currentPosition.copy()

            visibilityLevelSegment = self.traversal.findLevelSegmentOrNone(gameState.visibilityTree, trace.currentPosition)
            if visibilityLevelSegment not in trace.visibilityLevelSegments:
                visibilityLevelSegment.bulletTraces.append(trace)
                trace.visibilityLevelSegments.add(visibilityLevelSegment)

            trace.update()

            if not trace.isVisible:
                gameState.bulletTraces.remove(trace)
                for levelSegment in trace.visibilityLevelSegments:
                    levelSegment.bulletTraces.remove(trace)
