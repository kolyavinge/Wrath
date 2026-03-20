from game.render.gl.SpriteRenderer import SpriteRenderer
from game.render.gl.vbo.VBORenderer import VBORenderer
from game.render.gl.vbo.VBOUpdaterFactory import VBOUpdaterFactory


class SpriteRendererFactory:

    def __init__(
        self,
        vboUpdaterFactory: VBOUpdaterFactory,
        vboRenderer: VBORenderer,
    ):
        self.vboUpdaterFactory = vboUpdaterFactory
        self.vboRenderer = vboRenderer

    def make(self):
        return SpriteRenderer(self.vboUpdaterFactory, self.vboRenderer)
