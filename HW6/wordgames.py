import random
import string


VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7
word_list = []

SCRABBLE_LETTER_VALUES = { 'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2,
    'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10,
    'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10 }

WORDLIST_FILENAME = "words.txt"

# -----------------------------------
# Some functions to get you started
# Make sure you understand what they do and how they work!

def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand = {}
    number_of_vowels = n / 3
    
    for _ in range(number_of_vowels):
        letter = VOWELS[random.randrange(0, len(VOWELS))]
        hand[letter] = hand.get(letter, 0) + 1
        
    for _ in range(number_of_vowels, n):    
        letter = CONSONANTS[random.randrange(0, len(CONSONANTS))]
        hand[letter] = hand.get(letter, 0) + 1
        
    return hand

def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    wrd = ''
    for letter, frequency in hand.items():
        for _ in range(frequency):
             wrd += (letter + ' ')
    return wrd

# -----------------------------------


#
# Problem 0: Reading the words file 
#
def load_words():
    """
    Reads the file in the WORDLIST_FILENAME variable and returns a list of 
    words in that file, in lowercase. The file should contain valid english
    words, each placed on a new line. Depending on the size of the word list,
    this function may take a while to finish.

    return: list of strings
    """
    words_file = open(WORDLIST_FILENAME)
    return [line.lower().rstrip() for line in words_file]



#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    The score for a word is the sum of the points for letters
    in the word multiplied by the length of the word, plus 50
    points if all n letters are used on the first go.

    Letters are scored as in Scrabble; A is worth 1, B is
    worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string (lowercase letters)
    returns: int >= 0
    """
    score = 0
    for i in range(len(word)):
        try:
            score += SCRABBLE_LETTER_VALUES[word[i]]
        except:
            score += 0
    score *= len(word)
    if len(word) == n:
        score += 50
    return score


#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    nhand = hand.copy()
    for wordkey in range(len(word)):
        for handkey in nhand.keys():
            if(word[wordkey] == handkey):
                if nhand[handkey] > 1:
                    nhand[handkey] = nhand[handkey] - 1
                else:
                    del nhand[handkey]
                    break
    return nhand


#
# Problem #3: Test word validity
#
def get_frequency_dict(word):
    """
    Returns a dictionary where the keys are letters of the word
    and the values are integer counts, for the number of times that
    letter is repeated in the word

    word: string
    return: dictionary
    """
    dict = {}
    for i in range(len(word)):
        if word[i] in dict:
            dict[word[i]] += 1
        else:
            dict[word[i]] = 1
    return dict

def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
    
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """

    word_dict = get_frequency_dict(word)
    hand_dict = hand

    if word in word_list:
        for n in range(len(word)):
            if word_dict[n] in hand_dict:
                hand_dict[n] -= 1
            else:
                return False
        return True
    else:
        return False


#
# Problem #4: Playing a hand
#
def hand_length(hand):
    """
    Computes the total number of letters left in the hand.
    Note: This is not same as len(hand)!
    
    hand: dictionary (string -> int)    
    returns: int
    """
    som = 0
    for n in hand.keys():
        som += hand[n]
    return som

def play_hand(hand, word_list):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word.
    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing a single
      period (the string '.') instead of a word.

    hand: dictionary (string -> int)
    words: list of lowercase strings
    """
    hand_score = 0
    while hand_length(hand) > 0:
        print "CurrentHand: " + str(display_hand(hand))
        new = raw_input("Enter word, or a '.' to indicate that you are finished: ")
        if new == '.':
            break
        elif new not in word_list:
            print "Your input is not a valid english word. Please try again."
        #TODO: Enter check for frequency decrepencies here
        else:
            hand_score += get_word_score(new, hand_length(hand))
            hand = update_hand(hand, new)
            print "Total score: " + str(hand_score) + " points."
        print
    print "Ending this hand with a total score of " + str(hand_score) + " points."
    return hand_score

#
# Problem #5: Playing a game
# Make sure you understand how this code works!
# 
def play_game(word_list):
    """
    Allow the user to play an arbitrary number of hands.

    * Asks the user to input 'n' or 'r' or 'e'.
    * If the user inputs 'n', let the user play a new (random) hand.
      When done playing the hand, ask the 'n' or 'e' question again.
    * If the user inputs 'r', let the user play the last hand again.
    * If the user inputs 'e', exit the game.
    * If the user inputs anything else, ask them again.
    """

    random_hand = deal_hand(HAND_SIZE)
    while True:
        choice = raw_input("Please choose between n, r or e:")
        if choice == 'n':
            print "Starting new random hand"
            random_hand = deal_hand(HAND_SIZE)
            play_hand(random_hand, word_list)
        elif choice == 'r':
            print "Replaying last hand!"
            play_hand(random_hand, word_list)
        elif choice == 'e':
            print "Exiting wordgames, thank you for playing!"
            break
        else:
            print "This is not a valid choice, please try again."


#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)

