class LevelValidator:

    def validate(self, level):
        level.validate()
        allLevelSegments = level.visibilityTree.getAllLevelSegments()
        self.onlyOneLevelItemInVisibilitySegment(allLevelSegments)

    def onlyOneLevelItemInVisibilitySegment(self, allLevelSegments):
		# если один обьект принадлежит нескольким сегментам, то он будет отрисовываться несколько раз
		# из-за этого может неправильно обрабатываться свет
        allLevelItems = set()
        for levelSegment in allLevelSegments:
            for levelItem in levelSegment.getAllItems():
                if levelItem not in allLevelItems:
                    allLevelItems.add(levelItem)
                else:
                    raise Exception(f"Level item exists in more than one visibility segment.")


def makeLevelValidator(resolver):
    return LevelValidator()
