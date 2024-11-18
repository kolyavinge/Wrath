from game.anx.CommonConstants import CommonConstants
from game.calc.TransformMatrix4Builder import TransformMatrix4Builder
from game.lib.Random import Random
from game.model.weapon.Weapon import Flash


class SimpleFlash(Flash):

    def __init__(self):
        super().__init__()
        self.alphaSteps = [0.8, 1.0, 0.8, 0.5, 0.25, 0.1]
        self.alphaStep = 0
        self.alpha = 0.5
        self.rand = Random()

    def update(self):
        self.alphaStep += 1
        if self.alphaStep < len(self.alphaSteps):
            self.alpha = self.alphaSteps[self.alphaStep]
        else:
            self.isVisible = False
            self.alpha = 0

    def calculateModelMatrix(self, position, yawRadians, pitchRadians):
        self.modelMatrix = (
            TransformMatrix4Builder()
            .translate(position.x, position.y, position.z)
            .rotate(yawRadians, CommonConstants.zAxis)
            .rotate(self.rand.getFloat(-0.5, 0.5), CommonConstants.yAxis)
            .rotate(pitchRadians, CommonConstants.xAxis)
            .resultMatrix
        )

    def getModelMatrix(self):
        return self.modelMatrix
