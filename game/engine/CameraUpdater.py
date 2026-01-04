from game.engine.GameState import GameState


class CameraUpdater:

    def __init__(self, gameState: GameState):
        self.gameState = gameState

    def update(self):
        camera = self.gameState.camera
        camera.position = self.gameState.player.eyePosition
        camera.lookDirection = self.gameState.player.lookDirection
        camera.calculateViewMatrix()
        camera.setVerticalViewRadians(self.gameState.aimState.verticalViewRadians)
        camera.calculateProjectionMatrix()
        camera.calculateProjectionViewMatrix()
