class PersonAudioSources:

    def __init__(self, person, audioSourceFactory):
        self.person = person
        self.step = audioSourceFactory.getStep()

    def updatePosition(self):
        position = self.person.currentCenterPoint
        self.step.setPosition(position)

    def release(self):
        self.step.release()
