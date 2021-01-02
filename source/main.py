import random
from collections import defaultdict
import re

HANGMAN = [
    '________',
    '|       |',
    '|       O',
    '|       |',
    '|      /|\ ',
    '|       |',
    '|      / \ '
]


class GameBoard:

    def __init__(self):
        self.menu()

    def menu(self):
        print("\nWelcome to the word guessing game\n")
        print("1. Start game\n2. About game\n3. Exit")
        selected_option = input("Enter key:")
        self.display_selected_option(selected_option)

    def about_game(self):
        print(
            "A word guessing game in which the player is told how many letters are in the word.\n"
            + "The game also allows user to select difficulty level and different categories.\n"
            + "The player must discover the word by guessing letters one at a time.\n"
            + "Each correctly guessed letter is added to the word. On each wrong guess, a body part\n"
            + "is added to a picture of a hanged man. Once the hanged man is complete, the player "
            + "loses the game.")
        menu_key = input("\nPress Enter to return to menu.")
        if menu_key == '':
            self.menu()
        else:
            print("please enter the correct key.\n")
            self.about_game()

    @staticmethod
    def exit_game():
        exit()

    def display_selected_option(self, option):

        if option == "1":
            game_engine_obj.get_user_name()
            game_engine_obj.difficulty_selection()
        elif option == "2":
            self.about_game()
        elif option == "3":
            self.exit_game()
        else:
            print("Please enter the correct key")
            self.menu()


class WordManagement:

    def __init__(self):
        self.secret_word = ""
        self.game_progress = ""
        self.category = ""

    @staticmethod
    def import_word_list(file):
        with open(file, 'r') as f:
            words = list(filter(None, f.read().split('\n')))
            return words

    def word_selection(self, word_category):
        self.category = word_category
        file_path = ""
        if word_category == "1":
            file_path = "../../Database/countries_cities.txt"
        elif word_category == "2":
            file_path = "../../Database/fruits_vegetables.txt"
        else:
            file_path = "../../Database/animals.txt"

        words = self.import_word_list(file_path)
        self.secret_word = self.get_random_word(words).lower()
        self.game_progress = list('_' * len(self.secret_word))
        game_engine_obj.play(self.secret_word, self.game_progress)

    @staticmethod
    def get_random_word(wordlist):
        word_index = random.randint(0, len(wordlist) - 1)
        return wordlist[word_index]


class GameEngine:
    def __init__(self):
        self.failed_attempts = 0
        self.total_attempts = 0
        self.game_started = False
        self.username = ""
        self.difficulty = ""
        self.game_progress = ""
        self.secret_word = ""
        self.word_category = ""
        self.word_management_obj = WordManagement()
        self.regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

    @staticmethod
    def play_game():
        GameBoard()

    def get_user_name(self):
        self.username = input('\nEnter your name: ')

    def difficulty_selection(self):
        print("\nHello " + self.username)
        print("\nPlease select the difficulty level\n")
        difficulty_list = ["1", "2", "3"]
        print("1. Easy\n2. Medium\n3. Hard")
        difficulty_level = input("Enter key:")
        if difficulty_level not in difficulty_list:
            print("Please enter correct key")
            self.difficulty_selection()
        else:
            self.category_selection(difficulty_level)

    def category_selection(self, difficulty_level):
        self.difficulty = difficulty_level
        print("\nPlease select the category\n")
        category_list = ["1", "2", "3"]
        print("1. Countries and Cities\n2. Fruits and Vegetables\n3. Animals")
        self.word_category = input("Enter key:")
        if self.word_category not in category_list:
            print("Please enter the correct key")
            self.category_selection(self.difficulty)
        else:
            self.word_management_obj.word_selection(self.word_category)

    def print_game_status(self):
        print('\n')
        print('\n'.join(HANGMAN[:self.failed_attempts]))
        print('\n')
        print(' '.join(self.game_progress))

    def update_progress(self, letter, indexes):
        for index in indexes:
            self.game_progress[index] = letter

    @staticmethod
    def get_user_input():
        user_input = input('\nPlease type a letter: ')
        return user_input

    def find_indexes(self, letter):
        return [i for i, char in enumerate(self.secret_word) if letter == char]

    def is_invalid_letter(self, input_):
        return input_.isdigit() or (self.regex.search(input_) is not None) or (input_.isalpha() and len(input_) > 1)

    def play_again(self):
        print('Do you want to play again? (y/n)')
        input_key = input('> ').lower()
        if input_key == 'y':
            self.failed_attempts = 0
            self.word_management_obj.word_selection(self.word_category)
        elif input_key == 'n':
            self.play_game()
        else:
            print("Please enter the correct key!")
            self.play_again()

    def get_total_attempts(self):

        print("\nHello " + self.username)

        if self.difficulty == "1":
            self.total_attempts = 7
        elif self.difficulty == "2":
            self.total_attempts = 6
        else:
            self.total_attempts = 5

        print("\nYou have " + str(self.total_attempts) + " attempts to guess the word")

    def get_failed_attempts(self):

        if self.game_started:
            self.failed_attempts += 1
        else:
            if self.difficulty == "1":
                self.failed_attempts += 1
            elif self.difficulty == "2":
                self.failed_attempts += 2
            else:
                self.failed_attempts += 3
            self.game_started = True

    def play(self, secret_word, game_progress):

        self.secret_word = secret_word
        self.game_progress = game_progress
        score_obj = ScoreManagement()
        self.get_total_attempts()

        while self.failed_attempts < len(HANGMAN):
            self.print_game_status()
            user_input = self.get_user_input()

            # Validate the user input
            if self.is_invalid_letter(user_input):
                print('Please enter a letter')
                continue
            # Check if the letter is not already guessed
            if user_input in self.game_progress:
                print('You already have guessed that letter')
                continue

            if user_input in self.secret_word:
                indexes = self.find_indexes(user_input)
                self.update_progress(user_input, indexes)
                # If there is no letter to find in the word
                if self.game_progress.count('_') == 0:
                    print('\nYay! You win!')
                    print('The word is: {0}'.format(self.secret_word))
                    ScoreManagement.updating_scores(score_obj, self.username, self.failed_attempts)
                    ScoreManagement.highest_scores(score_obj)
                    self.play_again()
            else:
                self.get_failed_attempts()
                self.total_attempts -= 1
                if self.total_attempts != 0:
                    print("\nNow you have " + str(self.total_attempts) + " attempts are left")

        ScoreManagement.updating_scores(score_obj, self.username, self.failed_attempts)

        print('\n'.join(HANGMAN[:len(HANGMAN)]))
        print('\n')
        print('The word is: {0}'.format(self.secret_word))
        print("\nSorry,You lost!")

        ScoreManagement.highest_scores(score_obj)
        self.play_again()


class ScoreManagement:

    def __init__(self):
        self.total_score = 100
        self.file_path = "../Database/scores.txt"

    def updating_scores(self, user_name, wrong_guess):

        if wrong_guess != 0:
            self.total_score = self.total_score - (10 * wrong_guess)
        text_file = open(self.file_path, "a")
        text_file.write("\n{0}".format(user_name))
        text_file.write(" {0} ".format(str(self.total_score)))
        text_file.close()

    def highest_scores(self):

        print("your score is {0}".format(self.total_score))
        results = defaultdict(int)
        sorted_dict = {}
        with open(self.file_path, "r") as file:

            for line in file:
                name, points = line.split()
                results[name] += int(points)

        sorted_keys = sorted(results, key=results.get, reverse=True)
        for w in sorted_keys:
            sorted_dict[w] = results[w]

        print("\nHighest Scores\n")
        for name in sorted_dict:
            print(name, sorted_dict[name])


game_engine_obj = GameEngine()

if __name__ == '__main__':
    game_engine_obj.play_game()
