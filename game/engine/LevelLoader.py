from game.levels.Level1 import Level1
from game.levels.LevelLoop import LevelLoop
from game.model.PlayerMeasures import PlayerMeasures


class LevelLoader:

    def loadFromFile(self):
        level = Level1()
        self.calculateWallCrossLines(level)
        level.validate()

        return level

    def calculateWallCrossLines(self, level):
        for wall in level.walls:
            crossDirection = wall.frontNormal.getCopy()
            crossDirection.setLength(PlayerMeasures.xyLengthHalf)
            wall.crossLine.startPoint = wall.startPoint.getCopy()
            wall.crossLine.endPoint = wall.endPoint.getCopy()
            wall.crossLine.startPoint.add(crossDirection)
            wall.crossLine.endPoint.add(crossDirection)
            wallDirection = wall.endPoint.getCopy()
            wallDirection.sub(wall.startPoint)
            wallDirection.setLength(PlayerMeasures.xyLengthHalf)
            wall.crossLine.startPoint.sub(wallDirection)
            wall.crossLine.endPoint.add(wallDirection)
            wall.crossLineDirection = wall.crossLine.endPoint.getCopy()
            wall.crossLineDirection.sub(wall.crossLine.startPoint)


def makeLevelLoader(resolver):
    return LevelLoader()
