from game.gl.VBOBuilderFactory import VBOBuilderFactory
from game.lib.array import groupby
from game.model.level.Ceiling import Ceiling
from game.model.level.Floor import Floor
from game.model.level.Stair import Stair
from game.model.level.Wall import Wall
from game.render.common.MaterialTextureCollection import MaterialTextureCollection
from game.render.level.CeilingVBOBuilder import CeilingVBOBuilder
from game.render.level.FloorVBOBuilder import FloorVBOBuilder
from game.render.level.LevelItemGroup import LevelItemGroup
from game.render.level.StairVBOBuilder import StairVBOBuilder
from game.render.level.WallVBOBuilder import WallVBOBuilder


class LevelItemGroupBuilder:

    def __init__(self, vboBuilderFactory, wallVBOBuilder, floorVBOBuilder, stairVBOBuilder, ceilingVBOBuilder, materialTextureCollection):
        self.vboBuilderFactory = vboBuilderFactory
        self.wallVBOBuilder = wallVBOBuilder
        self.floorVBOBuilder = floorVBOBuilder
        self.stairVBOBuilder = stairVBOBuilder
        self.ceilingVBOBuilder = ceilingVBOBuilder
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
            elif isinstance(item, Floor):
                self.floorVBOBuilder.build(item, vboBuilder)
            elif isinstance(item, Ceiling):
                self.ceilingVBOBuilder.build(item, vboBuilder)

        return vboBuilder.build()

    def getLevelItemsGroupedByMaterial(self, levelSegment):
        allLevelItems = levelSegment.getAllItems()
        result = groupby(allLevelItems, lambda item: item.material)

        return result


def makeLevelItemGroupBuilder(resolver):
    return LevelItemGroupBuilder(
        resolver.resolve(VBOBuilderFactory),
        resolver.resolve(WallVBOBuilder),
        resolver.resolve(FloorVBOBuilder),
        resolver.resolve(StairVBOBuilder),
        resolver.resolve(CeilingVBOBuilder),
        resolver.resolve(MaterialTextureCollection),
    )
