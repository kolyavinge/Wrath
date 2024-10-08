class PersonAudioSources:

    def __init__(self, person, audioSourceFactory):
        self.person = person
        self.stepConcrete = audioSourceFactory.makeStepConcrete()
        self.stepMetal = audioSourceFactory.makeStepMetal()
        self.stepMetal.setGain(0.3)
        self.landing = audioSourceFactory.makeLanding()
        self.landing.setGain(0.8)

    def updatePosition(self):
        position = self.person.currentCenterPoint
        self.stepConcrete.setPosition(position)
        self.stepMetal.setPosition(position)
        self.landing.setPosition(position)

    def release(self):
        self.stepConcrete.release()
        self.stepMetal.release()
        self.landing.release()
