class Level:

    def __init__(self):
        self.floors = []

    def validate(self):
        for f in self.floors:
            f.validate()
