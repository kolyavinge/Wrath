class PersonAudioSources:

    def __init__(self, person, audioBufferCollection, audioSourceLoader):
        self.person = person
        self.step = audioSourceLoader.load(audioBufferCollection.step)

    def updatePosition(self):
        self.step.setPosition(self.person.currentCenterPoint)

    def release(self):
        self.step.release()
