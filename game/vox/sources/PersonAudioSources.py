class PersonAudioSources:

    def __init__(self, person, audioSourceFactory):
        self.person = person
        self.stepConcrete = audioSourceFactory.makeStepConcrete()
        self.stepMetal = audioSourceFactory.makeStepMetal()
        self.stepMetal.setGain(0.3)

    def updatePosition(self):
        position = self.person.currentCenterPoint
        self.stepConcrete.setPosition(position)
        self.stepMetal.setPosition(position)

    def release(self):
        self.stepConcrete.release()
        self.stepMetal.release()
