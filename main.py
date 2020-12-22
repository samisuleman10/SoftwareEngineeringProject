
class GameBoard:

    def __init__(self):
        self.menu()

    def menu(self):
        print("\nWelcome to the word guessing game\n")
        print("1. Start game\n2. About game\n3. Exit")
        selected_option = input("Enter key:")
        # print(selected_option)
        self.display_selected_option(selected_option)

    def difficulty_selection(self):
        print("\nPlease select the difficulty level\n")
        difficulty_list = ["1", "2", "3"]
        print("1. Easy\n2. Medium\n3. Hard")
        difficulty_level = input("Enter key:")
        if difficulty_level not in difficulty_list:
            print("Please enter correct key")
            self.difficulty_selection()
        else:
            self.category_selection(difficulty_level)

    def about_game(self):
        print(
            "A word guessing game in which the player is told how many letters are in the word.\n"
            + "The game also allows user to select difficulty level and different categories.\n"
            + "The player must discover the word by guessing letters one at a time.\n"
            + "Each correctly guessed letter is added to the word. On each wrong guess, a body part\n"
            + "is added to a picture of a hanged man. Once the hanged man is complete, the player "
            + "loses the game.")

    def exit_game(self):
        exit()

    def category_selection(self, difficulty_level):
        print("\nPlease select the category\n")
        category_list = ["1", "2", "3"]
        print("1. Countries and Cities\n2. Fruits and Vegetables\n3. Animals")
        word_category = input("Enter key:")
        if word_category not in category_list:
            print("Please enter the correct key")
            self.category_selection()
        else:
            print("Call another class")
            #game_engine_obj = GameEngine()
            #GameEngine.word_selection(game_engine_obj, word_category, difficulty_level)

    def display_selected_option(self, option):

        if option == "1":
            self.difficulty_selection()
        elif option == "2":
            self.about_game()
        elif option == "3":
            self.exit_game()
        else:
            print("Please enter the correct key")
            self.menu()



if __name__ == '__main__':
    GameBoard()

# Press the green button in the gutter to run the script.
