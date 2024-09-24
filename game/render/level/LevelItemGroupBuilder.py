from game.gl.VBOBuilderFactory import VBOBuilderFactory
from game.lib.List import List
from game.model.level.Construction import Construction
from game.model.level.Stair import Stair
from game.model.level.Wall import Wall
from game.render.common.MaterialTextureCollection import MaterialTextureCollection
from game.render.level.ConstructionVBOBuilder import ConstructionVBOBuilder
from game.render.level.LevelItemGroup import LevelItemGroup
from game.render.level.StairVBOBuilder import StairVBOBuilder
from game.render.level.WallVBOBuilder import WallVBOBuilder


class LevelItemGroupBuilder:

    def __init__(self, vboBuilderFactory, wallVBOBuilder, constructionVBOBuilder, stairVBOBuilder, materialTextureCollection):
        self.vboBuilderFactory = vboBuilderFactory
        self.wallVBOBuilder = wallVBOBuilder
        self.constructionVBOBuilder = constructionVBOBuilder
        self.stairVBOBuilder = stairVBOBuilder
        self.materialTextureCollection = materialTextureCollection

    def buildForLevelSegment(self, levelSegment):
        levelItemGroups = []
        groupsByMaterial = self.getLevelItemsGroupedByMaterial(levelSegment)
        for material, levelItems in groupsByMaterial:
            levelItemGroup = LevelItemGroup()
            levelItemGroup.material = material
            levelItemGroup.texture = self.materialTextureCollection.getTextureForMaterial(material)
            levelItemGroup.vbo = self.buildVBO(levelItems)
            levelItemGroups.append(levelItemGroup)

        return levelItemGroups

    def buildVBO(self, levelItems):
        vboBuilder = self.vboBuilderFactory.makeVBOBuilder()
        for item in levelItems:
            if isinstance(item, Wall):
                self.wallVBOBuilder.build(item, vboBuilder)
            elif isinstance(item, Stair):
                self.stairVBOBuilder.build(item, vboBuilder)
            elif isinstance(item, Construction):
                self.constructionVBOBuilder.build(item, vboBuilder)

        return vboBuilder.build()

    def getLevelItemsGroupedByMaterial(self, levelSegment):
        allLevelItems = levelSegment.getAllItems()
        result = List.groupby(allLevelItems, lambda item: item.material)

        return result


def makeLevelItemGroupBuilder(resolver):
    return LevelItemGroupBuilder(
        resolver.resolve(VBOBuilderFactory),
        resolver.resolve(WallVBOBuilder),
        resolver.resolve(ConstructionVBOBuilder),
        resolver.resolve(StairVBOBuilder),
        resolver.resolve(MaterialTextureCollection),
    )
