class CameraUpdater:

    def update(self, gameState):
        player = gameState.player
        camera = gameState.camera
        camera.position = player.eyePosition
        camera.lookDirection = player.lookDirection
        camera.calculateViewMatrix()
        camera.setVerticalViewRadians(player.aimState.verticalViewRadians)
        camera.calculateProjectionMatrix()
        camera.calculateProjectionViewMatrix()
