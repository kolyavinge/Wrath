class PlayertemsAudioSources:

    def __init__(self, player, audioSourceFactory):
        self.player = player
        self.torchSwitch = audioSourceFactory.getTorchSwitch()

    def updatePosition(self):
        position = self.player.currentCenterPoint
        self.torchSwitch.setPosition(position)

    def release(self):
        self.torchSwitch.release()
