class PersonAudioSources:

    def __init__(self, person, audioBufferCollection, audioSourceLoader):
        self.person = person
        self.step = audioSourceLoader.load(audioBufferCollection.step)

    def updatePosition(self):
        position = self.person.currentCenterPoint
        self.step.setPosition(position)

    def release(self):
        self.step.release()
