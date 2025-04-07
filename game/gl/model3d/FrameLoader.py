from game.calc.Quaternion import Quaternion
from game.calc.TransformMatrix4 import TransformMatrix4
from game.gl.model3d.Model3d import Frame
from game.lib.List import List


class FrameLoader:

    def loadFrames(self, channel, aiChannel):
        translationFrames = list(self.getTranslationFrames(aiChannel))
        rotationFrames = list(self.getRotationFrames(aiChannel))
        scaleFrames = list(self.getScaleFrames(aiChannel))
        assert List.isSorted(translationFrames, lambda x: x.time)
        assert List.isSorted(rotationFrames, lambda x: x.time)
        assert List.isSorted(scaleFrames, lambda x: x.time)
        self.linkNextFrames(translationFrames)
        self.linkNextFrames(rotationFrames)
        self.linkNextFrames(scaleFrames)
        channel.translationFrameRoot = self.makeFrameRootNode(translationFrames)
        channel.rotationFrameRoot = self.makeFrameRootNode(rotationFrames)
        channel.scaleFrameRoot = self.makeFrameRootNode(scaleFrames)

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

    def makeFrameRootNode(self, frames):

        def rec(leftIndex, rightIndex):
            if leftIndex <= rightIndex:
                middleIndex = int(leftIndex + (rightIndex - leftIndex) / 2)
                middle = frames[middleIndex]
                middle.leftChild = rec(leftIndex, middleIndex - 1)
                middle.rightChild = rec(middleIndex + 1, rightIndex)
                return middle
            else:
                return None

        rootNode = rec(0, len(frames) - 1)

        return rootNode


def makeFrameLoader(resolver):
    return FrameLoader()
