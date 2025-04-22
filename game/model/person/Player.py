from game.model.person.Person import Person


class Player(Person):

    def __init__(self):
        super().__init__()
        self.prevPrevSwingValue = 0
        self.prevSwingValue = 0
        self.currentSwingValue = 0
