class Player:
    # Superset across the Mario Kart set: later problems add an `ahead` link
    # (the opponent in front), so the shared class carries it.
    def __init__(self, character, kart, opponent=None):
        self.character = character
        self.kart = kart
        self.items = []
        self.ahead = opponent
