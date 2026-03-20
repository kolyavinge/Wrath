from game.lib.calc.Quaternion import Quaternion
from game.lib.calc.Vector3 import Vector3
from game.lib.collections.List import List
from game.lib.collections.Tree import Tree
from game.render.gl.model3d.Model3d import Frame


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
        channel.translationRootFrame = self.makeRootFrameNode(translationFrames)
        channel.rotationRootFrame = self.makeRootFrameNode(rotationFrames)
        channel.scaleRootFrame = self.makeRootFrameNode(scaleFrames)

    def getTranslationFrames(self, aiChannel):
        assert len(aiChannel.positionkeys) > 1
        for aiFrame in aiChannel.positionkeys:
            assert aiFrame.time >= 0
            yield Frame(aiFrame.time, Vector3(aiFrame.mValue.x, aiFrame.mValue.y, aiFrame.mValue.z))

    def getRotationFrames(self, aiChannel):
        assert len(aiChannel.rotationkeys) > 1
        for aiFrame in aiChannel.rotationkeys:
            assert aiFrame.time >= 0
            quat = Quaternion()
            quat.setComponents(aiFrame.mValue.w, aiFrame.mValue.x, aiFrame.mValue.y, aiFrame.mValue.z)
            quat.normalize()
            yield Frame(aiFrame.time, quat)

    def getScaleFrames(self, aiChannel):
        assert len(aiChannel.scalingkeys) > 1
        for aiFrame in aiChannel.scalingkeys:
            assert aiFrame.time >= 0
            yield Frame(aiFrame.time, Vector3(aiFrame.mValue.x, aiFrame.mValue.y, aiFrame.mValue.z))

    def linkNextFrames(self, frames):
        frameIterator = iter(frames)
        prevFrame = next(frameIterator)
        for currentFrame in frameIterator:
            prevFrame.nextFrame = currentFrame
            prevFrame = currentFrame

    def makeRootFrameNode(self, frames):
        return Tree.makeBinaryTreeFromSortedList(frames)
