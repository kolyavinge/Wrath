from game.model.person.Person import Person


class Player(Person):

    def __init__(self):
        super().__init__()
        self.isPlayer = True
        self.swingValue = 0
