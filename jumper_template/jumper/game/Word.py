import random


class Word:

    def __init__(self):
        """Declares the word and guesses variables"""

        self.word = "halp"
        self.guesses = []

    def get_word(self):
        """Will grab a random word and return it"""

        infile = open("./words.txt", "r")
        lines = infile.readlines()
        infile.close()
        word = random.choice(lines)
        self.word = word[:-1]
        return self.word

    def print_word(self):
        """Prints the word"""

        won = 0

        for char in self.word:
            if char in self.guesses:
                print(char, end=' ')
            else:
                print('_', end=' ')
                won += 1
        print()

        if not won:
            return True
        return False

    def check_guess(self, guess):
        """Check Guesses"""

        if not guess.isalpha():
            print('Enter only a LETTER')
            return False
        elif len(guess) > 1:
            print('Enter only a SINGLE letter')
            return False
        elif guess in self.guesses:
            print('You have already guessed that letter')
            return False
        return True

    def save_guess(self, guess):
        """Saves users guess"""

        life = True
        if not guess in self.word:
            life = False

        self.guesses.append(guess)
        return life
