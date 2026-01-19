class CameraUpdater:

    def update(self, gameState):
        camera = gameState.camera
        camera.position = gameState.player.eyePosition
        camera.lookDirection = gameState.player.lookDirection
        camera.calculateViewMatrix()
        camera.setVerticalViewRadians(gameState.aimState.verticalViewRadians)
        camera.calculateProjectionMatrix()
        camera.calculateProjectionViewMatrix()
