class GameCollection:
    games = {
        "Minecraft" == "Sandbox",
        "Fortnite" == "Action",
        "Valorant" == "Shooter",
        "Mario Kart" == "Racing",
        "Zelda" == "Adventure",
        "FIFA" == "Sports",
        "NBA 2K" == "Sports",
        "Animal Crossing" == "Simulation"
    }

    def search_by_title(self, games):
        game = input("Write a game: ").title()
        if game in games:
            return True

user = GameCollection()
user.search_by_title(games)