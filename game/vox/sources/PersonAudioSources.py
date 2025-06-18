class PersonAudioSources:

    def __init__(self, person, audioSourceFactory):
        self.person = person
        self.stepConcrete = audioSourceFactory.makeStepConcrete()
        self.stepMetal = audioSourceFactory.makeStepMetal()
        self.stepMetal.setGain(0.15)
        self.jumping = audioSourceFactory.makeJumping()
        self.jumping.setGain(0.4)
        self.landing = audioSourceFactory.makeLanding()
        self.landing.setGain(0.7)

    def updatePosition(self):
        position = self.person.currentCenterPoint
        self.stepConcrete.setPosition(position)
        self.stepMetal.setPosition(position)
        self.jumping.setPosition(position)
        self.landing.setPosition(position)

    def release(self):
        self.stepConcrete.release()
        self.stepMetal.release()
        self.jumping.release()
        self.landing.release()
