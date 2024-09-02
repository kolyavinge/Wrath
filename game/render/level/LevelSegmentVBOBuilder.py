from game.gl.VBOBuilderFactory import VBOBuilderFactory
from game.model.level.Stair import Stair
from game.render.level.CeilingVBOBuilder import CeilingVBOBuilder
from game.render.level.FloorVBOBuilder import FloorVBOBuilder
from game.render.level.StairVBOBuilder import StairVBOBuilder
from game.render.level.WallVBOBuilder import WallVBOBuilder


class LevelSegmentVBOBuilder:

    def __init__(self, vboBuilderFactory, wallVBOBuilder, floorVBOBuilder, stairVBOBuilder, ceilingVBOBuilder):
        self.vboBuilderFactory = vboBuilderFactory
        self.wallVBOBuilder = wallVBOBuilder
        self.floorVBOBuilder = floorVBOBuilder
        self.stairVBOBuilder = stairVBOBuilder
        self.ceilingVBOBuilder = ceilingVBOBuilder

    def build(self, levelSegment):
        vboBuilder = self.vboBuilderFactory.makeVBOBuilder()

        for wall in levelSegment.walls:
            self.wallVBOBuilder.build(wall, vboBuilder)

        for floor in levelSegment.floors:
            if not isinstance(floor, Stair):
                self.floorVBOBuilder.build(floor, vboBuilder)

        for stair in levelSegment.floors:
            if isinstance(floor, Stair):
                self.stairVBOBuilder.build(stair, vboBuilder)

        for ceiling in levelSegment.ceilings:
            self.ceilingVBOBuilder.build(ceiling, vboBuilder)

        vbo = vboBuilder.build()

        return vbo


def makeLevelSegmentVBOBuilder(resolver):
    return LevelSegmentVBOBuilder(
        resolver.resolve(VBOBuilderFactory),
        resolver.resolve(WallVBOBuilder),
        resolver.resolve(FloorVBOBuilder),
        resolver.resolve(StairVBOBuilder),
        resolver.resolve(CeilingVBOBuilder),
    )
