class WeaponFlashUpdater:

    def update(self, gameState):
        for levelSegment in gameState.visibilityTree.allLevelSegments:
            for flash in levelSegment.weaponFlashes:
                flash.update()
                if not flash.isVisible:
                    levelSegment.weaponFlashes.remove(flash)
