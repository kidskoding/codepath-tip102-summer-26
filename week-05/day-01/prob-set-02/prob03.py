class Player:
    def __init__(self, character, kart):
        self.character = character
        self.kart = kart
        self.items = []

    def get_player(self):
        return f"{self.character} driving the {self.kart}"


player_one = Player("Yoshi", "Super Blooper")

# Update player_one's kart to "Dolphin Dasher" here
