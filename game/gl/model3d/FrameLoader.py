from game.calc.Quaternion import Quaternion
from game.calc.TransformMatrix4 import TransformMatrix4
from game.gl.model3d.Model3d import Frame
from game.lib.List import List


class FrameLoader:

    def loadFrames(self, channel, aiChannel):
        channel.translationFrames = list(self.getTranslationFrames(aiChannel))
        channel.rotationFrames = list(self.getRotationFrames(aiChannel))
        channel.scaleFrames = list(self.getScaleFrames(aiChannel))
        assert List.isSorted(channel.translationFrames, lambda x: x.time)
        assert List.isSorted(channel.rotationFrames, lambda x: x.time)
        assert List.isSorted(channel.scaleFrames, lambda x: x.time)
        self.linkNextFrames(channel.translationFrames)
        self.linkNextFrames(channel.rotationFrames)
        self.linkNextFrames(channel.scaleFrames)

    def getTranslationFrames(self, aiChannel):
        assert len(aiChannel.positionkeys) > 1
        for aiFrame in aiChannel.positionkeys:
            assert aiFrame.time >= 0
            transformMatrix = TransformMatrix4()
            transformMatrix.translate(aiFrame.mValue.x, aiFrame.mValue.y, aiFrame.mValue.z)
            yield Frame(aiFrame.time, transformMatrix)

    def getRotationFrames(self, aiChannel):
        assert len(aiChannel.rotationkeys) > 1
        for aiFrame in aiChannel.rotationkeys:
            assert aiFrame.time >= 0
            quat = Quaternion()
            quat.setComponents(aiFrame.mValue.w, aiFrame.mValue.x, aiFrame.mValue.y, aiFrame.mValue.z)
            transformMatrix = quat.getTransformMatrix4()
            yield Frame(aiFrame.time, transformMatrix)

    def getScaleFrames(self, aiChannel):
        assert len(aiChannel.scalingkeys) > 1
        for aiFrame in aiChannel.scalingkeys:
            assert aiFrame.time >= 0
            transformMatrix = TransformMatrix4()
            transformMatrix.scale(aiFrame.mValue.x, aiFrame.mValue.y, aiFrame.mValue.z)
            yield Frame(aiFrame.time, transformMatrix)

    def linkNextFrames(self, frames):
        frameIterator = iter(frames)
        prevFrame = next(frameIterator)
        for currentFrame in frameIterator:
            prevFrame.nextFrame = currentFrame
            prevFrame = currentFrame


def makeFrameLoader(resolver):
    return FrameLoader()
