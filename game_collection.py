games = {
    "Minecraft" : "Sandbox",
    "Fortnite" : "Action",
    "Valorant" : "Shooter",
    "Mario Kart" : "Racing",
    "Zelda" : "Adventure",
    "FIFA" : "Sports",
    "NBA 2K" : "Sports",
    "Animal Crossing" : "Simulation"
}

# This includes repeated genres
all_genres = games.values()

# This does not include repeated genres
unique_genres = []
for genre in all_genres:
    if genre not in unique_genres:
        unique_genres.append(genre)

# This includes all available games
all_games = list(games)

class GameCollection:
    def __init__(self, games):
        self.games = games

    def add_game(self, games):
        new_game = input("Write the game's title that you want to add: ").title()
        new_genre = input("What is the game's genre? ").title()
        print(f"New game: {new_game} \n Genre: {new_genre}")
        user_answer = input("Is this information correct? ").title()
        if user_answer == "Yes":
            games[new_game] = new_genre
            print(f"{new_game} has been added with the genre \"{new_genre}\"!")
    
    def search_by_title(self, games):
        game = input("Write a game: ").title()
        if game in games:
            print(f"The genre of {game} is: {games[game]}.")
        else:
            print("The game you are currently looking for is not in the database.")
            user_answer = input("Would you like to add it? ").title()
            if user_answer == "Yes":
                GameCollection.add_game(self, games)

    def search_by_genre(self, games):
        print("Please choose a genre from the following:")
        print("\n".join(unique_genres))
        genre = input("Write a genre: ").title()
        if genre in games.values():
            print("Genre found!")
            user_answer = input("Would you like to see the games of that genre? ").title()
            if user_answer == "Yes":
                matching_values = [k for k, v in games.items() if v == genre] 
                print(f"Here are the games with the genre {genre}:")
                print("\n".join(matching_values))
            elif user_answer == "No":
                print(f"Understood! Games with the genre \"{genre}\" will not be shown!")
            else:
                print("Invalid input.")
        else:
            print("The genre you are looking for does not currently exist.")

    def display_all_games(self, games):
        print("\n".join(games.keys()))

    def display_all_genres(self, games):
        print("\n".join(games.values()))

user = GameCollection(games)

program_start = input("Would you like to run the program? ").title() 
if program_start == "Yes":
    while program_start == "Yes":
        title_or_genre = input("Do you want to search by title or genre? \n Type \"T\" if you want to search by title. Type \"G\" if you want to search by genre. \n").upper()
        
        if title_or_genre == "T":
            show_titles = input("Would you like to see all the games? ").title()
            if show_titles == "Yes":
                user.display_all_games(games)
            user.search_by_title(games)
            program_start = input("Would you like to keep the program running? ").title()
        if title_or_genre == "G":
            show_genres = input("Would you like to see all the genres? ").title()
            if show_genres == "Yes":
                user.display_all_genres(games)
            user.search_by_genre(games)
            program_start = input("Would you like to keep the program running? ").title()