from game.gl.VBOBuilderFactory import VBOBuilderFactory
from game.lib.array import groupby
from game.model.level.Ceiling import Ceiling
from game.model.level.Stair import Stair
from game.model.level.Wall import Wall
from game.render.common.TextureCollection import TextureCollection
from game.render.level.CeilingVBOBuilder import CeilingVBOBuilder
from game.render.level.FloorVBOBuilder import FloorVBOBuilder
from game.render.level.LevelItemGroup import LevelItemGroup
from game.render.level.StairVBOBuilder import StairVBOBuilder
from game.render.level.WallVBOBuilder import WallVBOBuilder


class LevelItemGroupBuilder:

    def __init__(self, vboBuilderFactory, wallVBOBuilder, floorVBOBuilder, stairVBOBuilder, ceilingVBOBuilder, textureCollection):
        self.vboBuilderFactory = vboBuilderFactory
        self.wallVBOBuilder = wallVBOBuilder
        self.floorVBOBuilder = floorVBOBuilder
        self.stairVBOBuilder = stairVBOBuilder
        self.ceilingVBOBuilder = ceilingVBOBuilder
        self.textureCollection = textureCollection

    def buildForLevelSegment(self, levelSegment):
        levelItemGroups = []
        allLevelItems = levelSegment.getAllItems()
        groupsByMaterial = groupby(allLevelItems, lambda item: item.material)
        for material, levelItems in groupsByMaterial:
            levelItemGroup = LevelItemGroup()
            levelItemGroup.material = material
            levelItemGroup.texture = self.textureCollection.blank
            levelItemGroups.append(levelItemGroup)
            vbo = self.buildVBO(levelItems)
            levelItemGroup.vbo = vbo

        return levelItemGroups

    def buildVBO(self, levelItems):
        vboBuilder = self.vboBuilderFactory.makeVBOBuilder()
        for item in levelItems:
            if isinstance(item, Wall):
                self.wallVBOBuilder.build(item, vboBuilder)
            elif isinstance(item, Stair):
                self.stairVBOBuilder.build(item, vboBuilder)
            elif not isinstance(item, Stair):
                self.floorVBOBuilder.build(item, vboBuilder)
            elif isinstance(item, Ceiling):
                self.ceilingVBOBuilder.build(item, vboBuilder)

        vbo = vboBuilder.build()

        return vbo


def makeLevelItemGroupBuilder(resolver):
    return LevelItemGroupBuilder(
        resolver.resolve(VBOBuilderFactory),
        resolver.resolve(WallVBOBuilder),
        resolver.resolve(FloorVBOBuilder),
        resolver.resolve(StairVBOBuilder),
        resolver.resolve(CeilingVBOBuilder),
        resolver.resolve(TextureCollection),
    )
