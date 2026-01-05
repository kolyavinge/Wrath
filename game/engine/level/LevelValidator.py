from game.lib.Math import Math


class LevelValidator:

    def validate(self, level, visibilityTree):
        level.validate()
        # self.printSegmentInfo(visibilityTree.allLevelSegments)

    def printSegmentInfo(self, allLevelSegments):
        # self.printItems(allLevelSegments, lambda x: x.floors, "floors")
        self.printItems(allLevelSegments, lambda x: x.walls, "walls")

    def printItems(self, allLevelSegments, getItemFunc, title):
        print(title)
        for levelSegment in allLevelSegments:
            print(
                [item.id for item in getItemFunc(levelSegment)],
                (
                    Math.minFromList([item.downLeft.z for item in getItemFunc(levelSegment)]),
                    Math.maxFromList([item.downLeft.z for item in getItemFunc(levelSegment)]),
                ),
            )
        print()
