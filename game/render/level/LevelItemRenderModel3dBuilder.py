from game.gl.RenderModel3d import RenderMesh, RenderModel3d
from game.gl.VBOBuilderFactory import VBOBuilderFactory
from game.lib.List import List
from game.model.level.Construction import Construction
from game.model.level.Stair import Stair
from game.model.level.Wall import Wall
from game.model.light.Lamp import Lamp
from game.render.common.MaterialTextureCollection import MaterialTextureCollection
from game.render.level.ConstructionVBOBuilder import ConstructionVBOBuilder
from game.render.level.LampVBOBuilder import LampVBOBuilder
from game.render.level.StairVBOBuilder import StairVBOBuilder
from game.render.level.WallVBOBuilder import WallVBOBuilder


class LevelItemRenderModel3dBuilder:

    def __init__(self, vboBuilderFactory, wallVBOBuilder, constructionVBOBuilder, stairVBOBuilder, lampVBOBuilder, materialTextureCollection):
        self.vboBuilderFactory = vboBuilderFactory
        self.wallVBOBuilder = wallVBOBuilder
        self.constructionVBOBuilder = constructionVBOBuilder
        self.stairVBOBuilder = stairVBOBuilder
        self.lampVBOBuilder = lampVBOBuilder
        self.materialTextureCollection = materialTextureCollection

    def buildRenderModel3d(self, levelSegment):
        meshes = []
        groupsByMaterial = self.getLevelItemsGroupedByMaterial(levelSegment)
        for material, levelItems in groupsByMaterial:
            texture = self.materialTextureCollection.getTextureForMaterial(material)
            vbo = self.buildVBO(levelItems)
            meshes.append(RenderMesh(vbo, texture, material))

        return RenderModel3d(meshes)

    def buildVBO(self, levelItems):
        vboBuilder = self.vboBuilderFactory.makeVBOBuilder()
        for item in levelItems:
            if isinstance(item, Wall):
                self.wallVBOBuilder.build(item, vboBuilder)
            elif isinstance(item, Stair):
                self.stairVBOBuilder.build(item, vboBuilder)
            elif isinstance(item, Construction):
                self.constructionVBOBuilder.build(item, vboBuilder)
            elif isinstance(item, Lamp):
                self.lampVBOBuilder.build(item, vboBuilder)
            else:
                raise Exception("Wrong level item.")

        return vboBuilder.build()

    def getLevelItemsGroupedByMaterial(self, levelSegment):
        allLevelItems = levelSegment.getAllItems()
        result = List.groupby(allLevelItems, lambda item: item.material)

        return result


def makeLevelItemRenderModel3dBuilder(resolver):
    return LevelItemRenderModel3dBuilder(
        resolver.resolve(VBOBuilderFactory),
        resolver.resolve(WallVBOBuilder),
        resolver.resolve(ConstructionVBOBuilder),
        resolver.resolve(StairVBOBuilder),
        resolver.resolve(LampVBOBuilder),
        resolver.resolve(MaterialTextureCollection),
    )
