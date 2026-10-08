class Player:
    def __init__(self, character, kart):
        self.character = character
        self.kart = kart
        self.items = []

    def get_player(self):
        return f"{self.character} driving the {self.kart}"


player_one = Player("Yoshi", "Super Blooper")

# Create player_two here, then use get_player() to print the match line
