class Villager:
    # Superset across the Animal Crossing set: later problems add `personality`
    # and a `neighbor` link, so the shared class carries both.
    def __init__(self, name, species, personality, catchphrase, neighbor=None):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []
        self.neighbor = neighbor
