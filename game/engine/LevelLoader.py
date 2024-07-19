from game.anx.PlayerConstants import PlayerConstants
from game.levels.Level1 import Level1
from game.levels.LevelLoop import LevelLoop


class LevelLoader:

    def loadFromFile(self):
        level = LevelLoop()
        self.calculateWallCrossLines(level)
        level.validate()

        return level

    def calculateWallCrossLines(self, level):
        for wall in level.walls:
            crossDirection = wall.frontNormal.copy()
            crossDirection.setLength(PlayerConstants.xyLengthHalf)
            wall.crossLine.startPoint = wall.startPoint.copy()
            wall.crossLine.endPoint = wall.endPoint.copy()
            wall.crossLine.startPoint.add(crossDirection)
            wall.crossLine.endPoint.add(crossDirection)
            wallDirection = wall.endPoint.getDirectionTo(wall.startPoint)
            wallDirection.setLength(PlayerConstants.xyLengthHalf)
            wall.crossLine.startPoint.sub(wallDirection)
            wall.crossLine.endPoint.add(wallDirection)
            wall.crossLineDirection = wall.crossLine.endPoint.getDirectionTo(wall.crossLine.startPoint)


def makeLevelLoader(resolver):
    return LevelLoader()
