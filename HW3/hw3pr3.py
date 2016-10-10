#
# hw3pr3.py
#
# Name: Ivo de Geus
# Date: 19-6-2016
#

# === mylen example from class === #
def mylen(s):
    """ mylen outputs the length of s
              input: s, which can be a string or list
    """
    if s == '' or s == []:   # if empty string or empty list
        return 0
    else:
        return 1 + mylen(s[1:])



# === My Functions === #
def mult(n, m):
    """ mult returns the product of its two inputs
            inputs: n and m are both integers
            output: the result upon multiplying n and m
        """
    if(m == 1):
        return n
    elif(m > 0):
        return n + mult(n, m-1)
    else:
        return 0


def dot(L, K):
    """" dot multiplies the two arguments together based on their index, and then adds together.
        Input: N and M are both lists, which can contain only numbers, cast to floats.
        Output: loops through both lists, and multiplies each index.
    """
    try:
        value_one = float(L.pop(0))
        value_two = float(K.pop(0))
        value = value_one*value_two
    except:
        return 0

    if value == 0 or type(value) is not float or len(L) is not len(K):
        return 0

    return value + dot(L, K)


def ind(e, L):
    """ ind gets the index of input e in list l. if it doesn't exist, returns the len(L)
        Input: e is the needle, L is the haystack.
        Output: always int, if found the index in the array, else the len.
    """
    if(L[0] == e):
        return 0
    else:
        try:
            return 1 + ind(e, L[1:])
        except:
            return 1


def letterScore(letter):
    """ letterScore returns the letter score of a scrabble
        variable.
        Input: a single character
        Output: According to scrabble rules, the according score. Else, 0
    """
    if letter in ['a', 'e', 'i', 'l', 'n', 'o', 'r', 's', 't', 'u']:
        return 1
    elif letter in ['d', 'g']:
        return 2
    elif letter in ['b', 'c', 'm', 'p']:
        return 3
    elif letter in ['f', 'h', 'v', 'w', 'y']:
        return 4
    elif letter == 'k':
        return 5
    elif letter in ['j', 'x']:
        return 8
    elif letter in ['q', 'z']:
        return 10
    else:
        return 0


def scrabbleScore(S):
    """ scrabbleScore takes a string as input, and returns the scrabble value.
        Input: string of characters
        Output: scrabbleScore of the current string of characters.
    """
    i = 0
    if(S == ""):
        return 0
    else:
        i += letterScore(S[0])
        i += scrabbleScore(S[1:])
    return i


def one_dna_to_rna(c):
    """ converts a single-character c from DNA
        nucleotide to complementary RNA nucleotide """
    if c == 'A': return 'U'
    elif(c == 'C'): return 'G'
    elif(c == 'G'): return 'C'
    elif(c == 'T'): return 'A'
    else: return ''


def transcribe(S):
    """ Transcribes DNA to RNA strings.
        Input: String of characters
        Output: Valid characters are taken out, and replaced. Others are left out.
    """
    i = ''
    if(S == ""):
        return ''
    else:
        i += one_dna_to_rna(S[0])
        i += transcribe(S[1:])
    return i
