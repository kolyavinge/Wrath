class Floor:

    def __init__(self):
        self.walls = []
        self.grounds = []
        self.height = 5

    def validate(self):
        for w in self.walls:
            w.validate()
