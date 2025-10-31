from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal
from game.engine.GameData import GameData


class BulletTraceUpdater:

    def __init__(
        self,
        gameData: GameData,
        traversal: BSPTreeTraversal,
    ):
        self.gameData = gameData
        self.traversal = traversal

    def update(self):
        for trace in self.gameData.bulletTraces:
            if trace.bullet.traceShift > 0:
                trace.currentPosition = trace.bullet.direction.copy()
                trace.currentPosition.mul(-trace.bullet.traceShift)
                trace.currentPosition.add(trace.bullet.currentPosition)
            else:
                trace.currentPosition = trace.bullet.currentPosition.copy()

            visibilityLevelSegment = self.traversal.findLevelSegmentOrNone(self.gameData.visibilityTree, trace.currentPosition)
            if visibilityLevelSegment not in trace.visibilityLevelSegments:
                visibilityLevelSegment.bulletTraces.append(trace)
                trace.visibilityLevelSegments.add(visibilityLevelSegment)

            trace.update()

            if not trace.isVisible:
                self.gameData.bulletTraces.remove(trace)
                for levelSegment in trace.visibilityLevelSegments:
                    levelSegment.bulletTraces.remove(trace)
