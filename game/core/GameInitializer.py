from game.anx.PersonIdLogic import PersonIdLogic
from game.audio.AudioPlayer import AudioPlayer
from game.core.GameStartMode import GameStartMode
from game.engine.ai.EnemyAIUpdater import EnemyAIUpdater
from game.engine.bsp.BSPTreeBuilder import BSPTreeBuilder
from game.engine.GameState import ClientGameState, ServerGameState
from game.engine.GameUpdater import GameUpdater
from game.engine.level.BackgroundVisibilityUpdater import BackgroundVisibilityUpdater
from game.engine.level.LevelLoader import LevelLoader
from game.engine.level.LevelSegmentJoinLineAnalyzer import LevelSegmentJoinLineAnalyzer
from game.engine.level.LevelSegmentLightAnalyzer import LevelSegmentLightAnalyzer
from game.engine.level.LevelValidator import LevelValidator
from game.engine.person.AIDataInitializer import AIDataInitializer
from game.engine.person.CameraUpdater import CameraUpdater
from game.engine.person.FragStatisticUpdater import FragStatisticUpdater
from game.engine.person.LevelSegmentVisibilityUpdater import *
from game.engine.person.PersonInitializer import PersonInitializer
from game.engine.person.PersonWeaponPositionUpdater import PersonWeaponPositionUpdater
from game.engine.weapon.WeaponFlashUpdater import WeaponFlashUpdater
from game.gl.TextRenderer import TextRenderer
from game.network.ClientConnectionLogic import ClientConnectionLogic
from game.network.ClientMultiplayerSynchronizer import ClientMultiplayerSynchronizer
from game.network.GameService import GameService
from game.network.ServerConnectionLogic import ServerConnectionLogic
from game.network.ServerMultiplayerSynchronizer import ServerMultiplayerSynchronizer
from game.render.common.MaterialTextureCollection import MaterialTextureCollection
from game.render.common.ShaderCollection import ShaderCollection
from game.render.common.ShaderProgramCollection import ShaderProgramCollection
from game.render.common.TextureCollection import TextureCollection
from game.vox.common.AudioBufferCollection import AudioBufferCollection


class GameInitializer:

    def __init__(
        self,
        gameUpdater: GameUpdater,
        levelLoader: LevelLoader,
        bspTreeBuilder: BSPTreeBuilder,
        joinLineAnalyzer: LevelSegmentJoinLineAnalyzer,
        lightAnalyzer: LevelSegmentLightAnalyzer,
        levelValidator: LevelValidator,
        personIdLogic: PersonIdLogic,
        personInitializer: PersonInitializer,
        aiDataInitializer: AIDataInitializer,
        levelSegmentVisibilityUpdater: LevelSegmentVisibilityUpdater,
        cameraUpdater: CameraUpdater,
        backgroundVisibilityDetector: BackgroundVisibilityUpdater,
        personWeaponPositionUpdater: PersonWeaponPositionUpdater,
        weaponFlashUpdater: WeaponFlashUpdater,
        fragStatisticUpdater: FragStatisticUpdater,
        enemyAIUpdater: EnemyAIUpdater,
        textureCollection: TextureCollection,
        materialTextureCollection: MaterialTextureCollection,
        shaderCollection: ShaderCollection,
        shaderProgramCollection: ShaderProgramCollection,
        textRenderer: TextRenderer,
        audioPlayer: AudioPlayer,
        audioBufferCollection: AudioBufferCollection,
        clientConnectionLogic: ClientConnectionLogic,
        serverConnectionLogic: ServerConnectionLogic,
        clientMultiplayerSynchronizer: ClientMultiplayerSynchronizer,
        serverMultiplayerSynchronizer: ServerMultiplayerSynchronizer,
        gameService: GameService,
    ):
        self.levelLoader = levelLoader
        self.bspTreeBuilder = bspTreeBuilder
        self.joinLineAnalyzer = joinLineAnalyzer
        self.lightAnalyzer = lightAnalyzer
        self.levelValidator = levelValidator
        self.personIdLogic = personIdLogic
        self.personInitializer = personInitializer
        self.aiDataInitializer = aiDataInitializer
        self.levelSegmentVisibilityUpdater = levelSegmentVisibilityUpdater
        self.cameraUpdater = cameraUpdater
        self.backgroundVisibilityDetector = backgroundVisibilityDetector
        self.personWeaponPositionUpdater = personWeaponPositionUpdater
        self.weaponFlashUpdater = weaponFlashUpdater
        self.fragStatisticUpdater = fragStatisticUpdater
        self.enemyAIUpdater = enemyAIUpdater
        self.textureCollection = textureCollection
        self.materialTextureCollection = materialTextureCollection
        self.shaderCollection = shaderCollection
        self.shaderProgramCollection = shaderProgramCollection
        self.textRenderer = textRenderer
        self.audioPlayer = audioPlayer
        self.audioBufferCollection = audioBufferCollection
        self.gameUpdater = gameUpdater
        self.clientConnectionLogic = clientConnectionLogic
        self.serverConnectionLogic = serverConnectionLogic
        self.clientMultiplayerSynchronizer = clientMultiplayerSynchronizer
        self.serverMultiplayerSynchronizer = serverMultiplayerSynchronizer
        self.gameService = gameService

    def init(self, gameStartMode, client, server):
        if gameStartMode == GameStartMode.clientServerMode:
            self.initClient(client)
            self.initServer(server)
            self.serverConnectionLogic.init(server)
            self.serverConnectionLogic.connectByLocal(client)
            self.clientMultiplayerSynchronizer.init(client)
            self.serverMultiplayerSynchronizer.init(server)
            self.gameUpdater.initForClientServer(client.gameState, server.gameState)
        elif gameStartMode == GameStartMode.clientMode:
            self.initClient(client)
            self.clientConnectionLogic.connectByNet(client)
            self.clientMultiplayerSynchronizer.init(client)
            self.gameUpdater.initForClient(client.gameState)

    def initClient(self, client):
        client.gameState = ClientGameState()
        level = self.levelLoader.load()
        client.gameState.level = level
        self.bspTreeBuilder.build(client.gameState.collisionTree, level, list(level.getCollisionSplitPlanes()))
        self.bspTreeBuilder.build(client.gameState.visibilityTree, level, list(level.getVisibilitySplitPlanes()))
        self.joinLineAnalyzer.analyzeJoinLines(level, client.gameState.visibilityTree)
        self.lightAnalyzer.analyzeLights(level, client.gameState.visibilityTree)
        self.personIdLogic.resetEnemyId()
        self.personInitializer.init(client.gameState)
        self.personWeaponPositionUpdater.updateForPlayer(client.gameState)
        self.fragStatisticUpdater.init(client.gameState)
        self.cameraUpdater.update(client.gameState)
        self.levelSegmentVisibilityUpdater.update(client.gameState)
        self.backgroundVisibilityDetector.update(client.gameState)
        self.textureCollection.init()
        self.materialTextureCollection.init()
        self.shaderCollection.init()
        self.shaderProgramCollection.init()
        self.textRenderer.init()
        self.audioPlayer.init()
        self.audioBufferCollection.init()

    def initServer(self, server):
        server.gameState = ServerGameState()
        level = self.levelLoader.load()
        server.gameState.level = level
        self.bspTreeBuilder.build(server.gameState.collisionTree, level, list(level.getCollisionSplitPlanes()))
        self.bspTreeBuilder.build(server.gameState.visibilityTree, level, list(level.getVisibilitySplitPlanes()))
        self.joinLineAnalyzer.analyzeJoinLines(level, server.gameState.visibilityTree)
        self.levelValidator.validate(level, server.gameState.visibilityTree)
        self.lightAnalyzer.analyzeLights(level, server.gameState.visibilityTree)
        self.personIdLogic.resetEnemyId()
        self.personInitializer.init(server.gameState)
        self.aiDataInitializer.init(server.gameState)
        self.fragStatisticUpdater.init(server.gameState)
        self.enemyAIUpdater.init(server.gameState)
        self.personWeaponPositionUpdater.update(server.gameState)
        self.gameService.runAsync()
