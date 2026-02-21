from game.model.ai.AIData import AIData
from game.model.person.Person import Person


class Bot(Person):

    def __init__(self):
        super().__init__()
        self.aiData = AIData()
