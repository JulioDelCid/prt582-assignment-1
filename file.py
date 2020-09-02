import random #random module
from word_list import sports_list
import unittest



class TestStringMethods(unittest.TestCase):

# This test checks that characters are converted to UPPERCASE 
    def test_upper(self):
        self.assertEqual('soccer'.upper(), 'SOCCER')

# check that characters are checked for UPPERCASE
    def test_isupper(self):
        self.assertTrue('GOLF'.isupper())
        self.assertFalse('Golf'.isupper())

# check that assert only contains letters
    def test_isalpha(self):
        self.assertIsNot('123#*&'.isalpha(),'123#*&')
        self.assertTrue('abc'.isalpha())


    """
    # check that appends to list 
    class ListFullError(unittest.TestCase):
        def test_append(self,item):
            if self.count < 5:
                raise ListFullError
            self.array[self.count] = item
            self.count -= 1
    """





#Gets random word frpm sports list
def getRandomWord():
    word = random.choice(sports_list)
    return word.upper()

#Defines the game function
def game(word):
    wordGuessesSpaces = "_" * len(word)
    guessedLetters = []
    guessedWords = []
    attempts = 6
    guessed = False
    print("\n >>>> PLAY HANGMAN BATERY LIFE <<<< ")
    print(batteryLife(attempts))
    print(wordGuessesSpaces)
    print("\n")


#Starts the event driven loop
    while not guessed and attempts > 0:
        guess = input("Please enter a letter: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessedLetters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                attempts -= 1
                guessedLetters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessedLetters.append(guess)
                word_as_list = list(wordGuessesSpaces)
                indexes = [i for i, letter in enumerate(word) if letter == guess]
                for index in indexes:
                    word_as_list[index] = guess
                wordGuessesSpaces = "".join(word_as_list)
                if "_" not in wordGuessesSpaces:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessedWords:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                attempts -= 1
                guessedWords.append(guess)
            else:
                guessed = True
                wordGuessesSpaces = word
        else:
            print("Oops, only one alphabetic character per try")
        print(batteryLife(attempts))
        print(wordGuessesSpaces)
        print("\n")

    if guessed:
        print("Well done the secret word was" + word + ". Congratulations")
    else:
        print("Game Over! The mystery word was " + word + ". Maybe next time!")




#Graphics and interactions through an mutable list [] for game

def batteryLife(attempts):
    stages = [  # Game Over
"""
                Attempts left: 0 
                Life: 0%

                ██████████████████████████████████████████  
                ██                                      ██  
                ██                                      ████
                ██          Game Over                   ████
                ██          No More Life                ████
                ██                                      ████
                ██                                      ████
                ██                                      ██  
                ██████████████████████████████████████████  
                """,
                # 6 of 6 attempts
                """
                Attempts left: 1 
                Life: 17%

                ██████████████████████████████████████████  
                ██                                      ██  
                ██  ████                                ████
                ██  ████                                ████
                ██  ████                                ████
                ██  ████                                ████
                ██  ████                                ████
                ██                                      ██  
                ██████████████████████████████████████████  
                """,
                # 5 of 6 attempts
                """
                Attempts left: 2 
                Life: 33%

                ██████████████████████████████████████████  
                ██                                      ██  
                ██  ████  ████                          ████
                ██  ████  ████                          ████
                ██  ████  ████                          ████
                ██  ████  ████                          ████
                ██  ████  ████                          ████
                ██                                      ██  
                ██████████████████████████████████████████                      
                """,
                # 4 of 6 attempts
                """
                Attempts left: 3 
                Life: 50%
                
                ██████████████████████████████████████████  
                ██                                      ██  
                ██  ████  ████  ████                    ████
                ██  ████  ████  ████                    ████
                ██  ████  ████  ████                    ████
                ██  ████  ████  ████                    ████
                ██  ████  ████  ████                    ████
                ██                                      ██  
                ██████████████████████████████████████████               
                """,
                # 3 of 6 attempts
                """
                Attempts left: 4 
                Life: 67%              
                
                ██████████████████████████████████████████  
                ██                                      ██  
                ██  ████  ████  ████  ████              ████
                ██  ████  ████  ████  ████              ████
                ██  ████  ████  ████  ████              ████
                ██  ████  ████  ████  ████              ████
                ██  ████  ████  ████  ████              ████
                ██                                      ██  
                ██████████████████████████████████████████  
                """,
                # 2 of 6 attempts
                """
                Attempts left: 5 
                Life: 83%                         
                
                ██████████████████████████████████████████  
                ██                                      ██  
                ██  ████  ████  ████  ████  ████        ████
                ██  ████  ████  ████  ████  ████        ████
                ██  ████  ████  ████  ████  ████        ████
                ██  ████  ████  ████  ████  ████        ████
                ██  ████  ████  ████  ████  ████        ████
                ██                                      ██  
                ██████████████████████████████████████████  
                """,
                # 1 of 6 attempts
                """
                Attempts left: 6
                Life: 100%                         
                
                ██████████████████████████████████████████  
                ██                                      ██  
                ██  ████  ████  ████  ████  ████  ████  ████
                ██  ████  ████  ████  ████  ████  ████  ████
                ██  ████  ████  ████  ████  ████  ████  ████
                ██  ████  ████  ████  ████  ████  ████  ████
                ██  ████  ████  ████  ████  ████  ████  ████
                ██                                      ██  
                ██████████████████████████████████████████  
                """
    ]
    return stages[attempts]




def main():
    word = getRandomWord()
    game(word)
    while input("Play Again? Yes or No? ").upper() == "Y":
        word = getRandomWord()
        game(word)


if __name__ == "__main__":
    main()

