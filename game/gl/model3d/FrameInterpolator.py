from game.calc.Quaternion import Quaternion
from game.calc.Vector3 import Vector3


class FrameInterpolator:

    def getTranslationVector(self, currentFrame, currentTime):
        nextFrame = currentFrame.nextFrame
        scaleFactor = self.getScaleFactor(currentFrame.time, nextFrame.time, currentTime)
        result = Vector3.getLinearInterpolatedVector(currentFrame.value, nextFrame.value, scaleFactor)

        return result

    def getRotationQuaternion(self, currentFrame, currentTime):
        nextFrame = currentFrame.nextFrame
        scaleFactor = self.getScaleFactor(currentFrame.time, nextFrame.time, currentTime)
        result = Quaternion.getSlerpNear(currentFrame.value, nextFrame.value, scaleFactor)
        result.normalize()

        return result

    def getScaleVector(self, currentFrame, currentTime):
        nextFrame = currentFrame.nextFrame
        scaleFactor = self.getScaleFactor(currentFrame.time, nextFrame.time, currentTime)
        result = Vector3.getLinearInterpolatedVector(currentFrame.value, nextFrame.value, scaleFactor)

        return result

    def getScaleFactor(self, prevTime, nextTime, currentTime):
        scaleFactor = 0.0
        midWayLength = currentTime - prevTime
        framesDiff = nextTime - prevTime
        scaleFactor = midWayLength / framesDiff

        return scaleFactor
