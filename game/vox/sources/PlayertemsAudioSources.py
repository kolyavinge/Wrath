class PlayertemsAudioSources:

    def __init__(self, player, audioSourceFactory):
        self.player = player
        self.switchTorch = audioSourceFactory.makeSwitchTorch()
        self.switchTorch.setGain(0.6)

    def updatePosition(self):
        position = self.player.currentCenterPoint
        self.switchTorch.setPosition(position)

    def release(self):
        self.switchTorch.release()
