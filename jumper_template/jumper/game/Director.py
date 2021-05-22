from game.console import Console
from game.jumper import Jumper
from game.word import Word


class Director:
    """Director class engine of the program"""

    def __init__(self):
        """States the variables we will use"""

        self.lives = 4
        self.console = Console()
        self.jumper = Jumper()
        self.word = Word()

    def start_game(self):
        """Starts the game"""

        self.console.write("Hello welcome to Jumper")
        # Get a word
        self.word.get_word()

        while self.lives >= 0:
            # Display word
            result = self.word.print_word()
            if result:
                self.console.write(
                    "Congratulations you guessed the word correctly")
                break

            # Display the Jumper
            self.console.write(self.jumper.get_parachute(self.lives))

            # Check if you lose
            if not self.lives:
                self.console.write("You killed him")
                break

            # Ask for a Guess
            guess = self.console.read("Guess a letter [a-z]: ")

            # Filters input
            result = self.word.check_guess(guess)
            if not result:
                continue

            # Saves guess and updates life
            result = self.word.save_guess(guess)
            if not result:
                self.lives -= 1
