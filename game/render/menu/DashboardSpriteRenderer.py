from game.calc.TransformMatrix4 import TransformMatrix4
from game.engine.GameState import GameState
from game.gl.SpriteRendererFactory import SpriteRendererFactory
from game.model.weapon.Launcher import Launcher
from game.model.weapon.Pistol import Pistol
from game.model.weapon.Plasma import Plasma
from game.model.weapon.Railgun import Railgun
from game.model.weapon.Rifle import Rifle
from game.model.weapon.Sniper import Sniper
from game.render.common.ShaderProgramCollection import ShaderProgramCollection
from game.render.common.TextureCollection import TextureCollection


class DashboardSpriteRenderer:

    def __init__(
        self,
        gameData: GameState,
        shaderProgramCollection: ShaderProgramCollection,
        spriteRendererFactory: SpriteRendererFactory,
        textureCollection: TextureCollection,
    ):
        self.gameData = gameData
        self.shaderProgramCollection = shaderProgramCollection
        self.textureCollection = textureCollection
        self.spriteRenderer = spriteRendererFactory.make()
        self.weaponSprite = {}
        y = -25
        self.weaponSprite[Pistol] = (0, 0, 400, y)
        self.weaponSprite[Rifle] = (0, 1, 550, y)
        self.weaponSprite[Plasma] = (0, 2, 700, y)
        self.weaponSprite[Launcher] = (0, 3, 850, y)
        self.weaponSprite[Railgun] = (1, 0, 1000, y)
        self.weaponSprite[Sniper] = (1, 1, 1150, y)

    def init(self):
        self.spriteRenderer.init(4, 4, self.textureCollection.sprites)

    def setData(self, projectionMatrix, viewportWidth):
        self.projectionMatrix = projectionMatrix
        self.viewportWidth = viewportWidth

    def render(self):
        model = TransformMatrix4()
        model.scale(1.2, 1.2, 1.0)
        shader = self.shaderProgramCollection.meshExt
        shader.use()
        shader.setModelMatrix(model)
        shader.setViewMatrix(TransformMatrix4.identity)
        shader.setProjectionMatrix(self.projectionMatrix)
        self.updateSpriteData()
        shader.unuse()

    def updateSpriteData(self):
        spriteItems = list(self.getSpriteItems())
        self.spriteRenderer.render(spriteItems)

    def getSpriteItems(self):
        dashboard = self.gameData.dashboard
        for weaponType, spriteInfo in self.weaponSprite.items():
            if weaponType in dashboard.weaponTypesSet:
                row, col, x, y = spriteInfo
                alpha = 1 if weaponType == dashboard.selectedWeaponType else 0.7
                yield (row, col, x, y, alpha)
