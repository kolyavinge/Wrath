from game.anx.CommonConstants import CommonConstants
from game.calc.TransformMatrix4Builder import TransformMatrix4Builder
from game.lib.Random import Random
from game.model.weapon.WeaponFlash import WeaponFlash


class SimpleFlash(WeaponFlash):

    def __init__(self):
        super().__init__()
        self.alphaSteps = [0.5, 0.8, 1.0, 0.8, 0.5, 0.25, 0.15, 0.1]
        self.alphaStep = 0
        self.alpha = 0.5

    def update(self):
        self.alphaStep += 1
        if self.alphaStep < len(self.alphaSteps):
            self.alpha = self.alphaSteps[self.alphaStep]
        else:
            self.isVisible = False
            self.alpha = 0

    def getModelMatrix(self):
        return (
            TransformMatrix4Builder()
            .translate(self.weapon.barrelPosition.x, self.weapon.barrelPosition.y, self.weapon.barrelPosition.z)
            .rotate(self.weapon.yawRadians, CommonConstants.zAxis)
            .rotate(Random.getFloat(-0.2, 0.2), CommonConstants.yAxis)
            .rotate(self.weapon.pitchRadians, CommonConstants.xAxis)
            .resultMatrix
        )
