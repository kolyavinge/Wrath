class FragStatistic:

    def __init__(self, person):
        self.person = person
        self.frags = 0
        self.deaths = 0

    def __eq__(self, value):
        return self.person == value.person and self.frags == value.frags and self.deaths == value.deaths

    def __hash__(self):
        return hash((self.person, self.frags, self.deaths))
