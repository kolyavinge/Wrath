from game.anx.CommonConstants import CommonConstants
from game.anx.Events import Events
from game.gl.VBOUpdaterFactory import VBOUpdaterFactory
from game.lib.EventManager import EventManager


class BulletHoleRenderCollection:

    def __init__(self, vboUpdaterFactory, eventManager):
        self.vboUpdater = vboUpdaterFactory.makeVBOUpdater()
        self.vbos = {}
        eventManager.attachToEvent(Events.bulletHoleAdded, self.updateBulletHoles)

    def init(self, allVisibilityLevelSegments):
        for vbo in self.vbos.values():
            vbo.release()

        self.vbos.clear()

        for levelSegment in allVisibilityLevelSegments:
            self.vbos[levelSegment] = self.vboUpdater.buildUnfilled(4 * CommonConstants.maxBulletHoles, 2 * CommonConstants.maxBulletHoles)

    def getVBO(self, levelSegment):
        return self.vbos[levelSegment]

    def updateBulletHoles(self, bulletHole):
        vbo = self.vbos[bulletHole.levelSegment]
        if vbo.isFilled():
            vbo.refill()

        self.vboUpdater.beginUpdate(vbo)

        self.vboUpdater.addVertex(bulletHole.point1)
        self.vboUpdater.addVertex(bulletHole.point2)
        self.vboUpdater.addVertex(bulletHole.point3)
        self.vboUpdater.addVertex(bulletHole.point4)

        self.vboUpdater.addNormal(bulletHole.frontNormal)
        self.vboUpdater.addNormal(bulletHole.frontNormal)
        self.vboUpdater.addNormal(bulletHole.frontNormal)
        self.vboUpdater.addNormal(bulletHole.frontNormal)

        self.vboUpdater.addTexCoord(0, 0)
        self.vboUpdater.addTexCoord(1, 0)
        self.vboUpdater.addTexCoord(1, 1)
        self.vboUpdater.addTexCoord(0, 1)

        self.vboUpdater.addFace(0, 1, 2)
        self.vboUpdater.addFace(0, 2, 3)

        self.vboUpdater.endUpdate()


def makeBulletHoleRenderCollection(resolver):
    return BulletHoleRenderCollection(resolver.resolve(VBOUpdaterFactory), resolver.resolve(EventManager))
