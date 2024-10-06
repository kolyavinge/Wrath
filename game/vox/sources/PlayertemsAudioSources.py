class PlayertemsAudioSources:

    def __init__(self, player, audioBufferCollection, audioSourceLoader):
        self.player = player
        self.torchSwitch = audioSourceLoader.load(audioBufferCollection.torchSwitch)

    def updatePosition(self):
        position = self.player.currentCenterPoint
        self.torchSwitch.setPosition(position)

    def release(self):
        self.torchSwitch.release()
