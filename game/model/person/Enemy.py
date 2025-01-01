from game.model.person.Person import Person


class AIData:
    pass


class Enemy(Person):

    def __init__(self):
        super().__init__()
        self.aiData = AIData()
