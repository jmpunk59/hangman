from curses.ascii import isalpha
from words import words
import random



def get_valid_word():
    """ Choose a word randomly in the words list

    Return
    ------

    word : str
        A random valid word
    """

    word = random.choice(words)
    while ("-" or " ") in word:
        word = random.choice(words)
    return word.upper()


def main():

    used_letter = []
    # get a valid word
    word = get_valid_word()
    # slice the word into letters
    word_letters = []
    word_letters.extend(word)
    while (len(word_letters) > 0):
        # Get user guess
        user_input = input(f'Choose a letter : ').upper()
        # Check the user guess
        while (len(user_input) > 1 or not user_input.isalpha()):
            user_input = input(f'Wrong input, choose a single letter : ').upper()
        # Add letter in list
        if user_input not in used_letter:
            used_letter.append(user_input)
        if user_input in word_letters:
            # Deal with multiple occurences
            while user_input in word_letters:
                word_letters.remove(user_input)

        # Display letter used
        print("Letter used : ", ' '.join(used_letter))
        # Display the word
        word_display = [letter if letter in used_letter else '_' for letter in word ]
        print("Word : ", " ".join(word_display))
    
    print("Well done, you found the word : ", word.upper())

    



if __name__ == "__main__":
    main()