from game.anx.CommonConstants import CommonConstants
from game.anx.Events import Events
from game.gl.RenderModel3d import RenderMesh
from game.gl.VBOUpdaterFactory import VBOUpdaterFactory
from game.lib.EventManager import EventManager
from game.model.weapon.BulletHoleInfo import BulletHoleInfo
from game.render.common.MaterialTextureCollection import MaterialTextureCollection


class BulletHoleRenderCollection:

    def __init__(self, vboUpdaterFactory, materialTextureCollection, eventManager):
        self.vboUpdater = vboUpdaterFactory.makeVBOUpdater()
        self.materialTextureCollection = materialTextureCollection
        self.meshes = {}
        eventManager.attachToEvent(Events.bulletHoleAdded, self.updateBulletHoles)

    def init(self, allVisibilityLevelSegments):
        for levelSegments in self.meshes.values():
            for mesh in levelSegments.values():
                mesh.release()

        self.meshes.clear()

        for levelSegment in allVisibilityLevelSegments:
            self.meshes[levelSegment] = {}
            for holeInfo in BulletHoleInfo.allItems:
                vbo = self.vboUpdater.buildUnfilled(4 * CommonConstants.maxBulletHoles, 2 * CommonConstants.maxBulletHoles)
                texture = self.materialTextureCollection.getTextureForMaterial(holeInfo.material)
                mesh = RenderMesh(vbo, texture, holeInfo.material)
                self.meshes[levelSegment][holeInfo.material] = mesh

    def getRenderMeshes(self, levelSegment):
        return self.meshes[levelSegment].values()

    def updateBulletHoles(self, bulletHole):
        mesh = self.meshes[bulletHole.levelSegment][bulletHole.material]

        if mesh.vbo.isFilled():
            mesh.vbo.refill()

        self.vboUpdater.beginUpdate(mesh.vbo)

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
    return BulletHoleRenderCollection(
        resolver.resolve(VBOUpdaterFactory), resolver.resolve(MaterialTextureCollection), resolver.resolve(EventManager)
    )
