from game.model.level.Floor import Floor
from game.model.level.Stair import Stair


class LevelFloorCorrector:

    def correct(self, collisionTree):
        # TODO убрано
        return
        allLevelSegments = collisionTree.getAllLevelSegments()
        for levelSegment in allLevelSegments:
            if len(levelSegment.floors) == 2 and type(levelSegment.floors[0]) == Floor and isinstance(levelSegment.floors[1], Stair):
                levelSegment.floors.remove(levelSegment.floors[0])
