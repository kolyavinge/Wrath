from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal
from game.engine.cm.ConstructionCollisionDetector import ConstructionCollisionDetector
from game.engine.level.LevelSegmentItemFinder import LevelSegmentItemFinder


class LevelSegmentLightAnalyzer:

    def __init__(
        self,
        levelSegmentItemFinder: LevelSegmentItemFinder,
        constructionCollisionDetector: ConstructionCollisionDetector,
        traversal: BSPTreeTraversal,
    ):
        self.levelSegmentItemFinder = levelSegmentItemFinder
        self.constructionCollisionDetector = constructionCollisionDetector
        self.traversal = traversal

    def analyzeLights(self, level, bspTree):
        # чтобы свет из одного сегмента действовал и на соседние
        self.bspTree = bspTree
        allLevelSegments = self.bspTree.allLevelSegments
        for levelSegment in allLevelSegments:
            levelSegment.lightsWithJoined = levelSegment.lights.copy()
            for light in level.lights:
                lightLevelSegment = self.traversal.findLevelSegment(self.bspTree, light.position)
                if lightLevelSegment != levelSegment:
                    if self.isLightJoinedToSegment(light, lightLevelSegment, levelSegment):
                        levelSegment.lightsWithJoined.append(light)

    def isLightJoinedToSegment(self, light, lightLevelSegment, joinedLevelSegment):
        for joinLine in joinedLevelSegment.joinLines:
            for joinLinePoint in joinLine.points:
                if self.isJoinLinePointVisible(light, lightLevelSegment, joinedLevelSegment, joinLinePoint):
                    return True

        return False

    def isJoinLinePointVisible(self, light, lightLevelSegment, joinedLevelSegment, joinLinePoint):
        collidedConstruction = self.levelSegmentItemFinder.findItemOrNone(
            self.bspTree,
            lightLevelSegment,
            joinedLevelSegment,
            light.position,
            joinLinePoint,
            lambda segment, start, end: self.constructionCollisionDetector.getCollidedConstructionOrNone(segment.allConstructions, start, end),
        )

        return collidedConstruction is None
