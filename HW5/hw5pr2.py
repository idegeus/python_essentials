# ===
# hw5pr2.py - Lab 3 problem, "Sorting out Caesar!"
# Name(s): Ivo de Geus
# ===

from string import lowercase, uppercase


def encipher(S, n):
    """ Returns the string, rotated in the alphabet forward by N numbers
    """
    return '' . join( [ rot( S[i], n ) for i in range( len( S ) ) ] )

def rot(c, n):
    """ Rotates a single character forward or backward n numbers in the alphabet
    """
    if c in lowercase:
        return lowercase[ (lowercase.index(c) + n ) % 26 ]
    elif c in uppercase:
        return uppercase[ ( uppercase.index(c) + n ) % 26 ]
    else:
        return c

def decipher(raw):
    """ Should return a encipherd string based on probability in the english alphabet
    """
    S = raw.lower()
    max = 0
    #Maak een frequentietabel van het alphabet, met als index het nummer in lowercase
    scores = [0] * 26
    s_index = [0] * 26

    for n in range( len(S) ):
        if S[n] in lowercase:
            scores[lowercase.index(S[n])] += 1

    #Check iedere rotation
    for rotation in range(0,26):
        for letter in range(0, 26):
            #s_index[rotation] += ( letProb((letter + rotation) % 26) )
            if (max < s_index ):
                max = s_index[rotation]

    print s_index
    print scores
    pass

# table of probabilities for each letter...
def letProb(c):
    """ if c is an alphabetic character,
    we return its monogram probability (for english),
    otherwise we return 1.0 We ignore capitalization.
    Adapted from
    http://www.math.cornell.edu/~mec/2003-2004/cryptography/subs/frequencies.html
    """
    if c == 'e' or c == 'E': return 0.1202
    if c == 't' or c == 'T': return 0.0910
    if c == 'a' or c == 'A': return 0.0812
    if c == 'o' or c == 'O': return 0.0768
    if c == 'i' or c == 'I': return 0.0731
    if c == 'n' or c == 'N': return 0.0695
    if c == 's' or c == 'S': return 0.0628
    if c == 'r' or c == 'R': return 0.0602
    if c == 'h' or c == 'H': return 0.0592
    if c == 'd' or c == 'D': return 0.0432
    if c == 'l' or c == 'L': return 0.0398
    if c == 'u' or c == 'U': return 0.0288
    if c == 'c' or c == 'C': return 0.0271
    if c == 'm' or c == 'M': return 0.0261
    if c == 'f' or c == 'F': return 0.0230
    if c == 'y' or c == 'Y': return 0.0211
    if c == 'w' or c == 'W': return 0.0209
    if c == 'g' or c == 'G': return 0.0203
    if c == 'p' or c == 'P': return 0.0182
    if c == 'b' or c == 'B': return 0.0149
    if c == 'v' or c == 'V': return 0.0111
    if c == 'k' or c == 'K': return 0.0069
    if c == 'x' or c == 'X': return 0.0017
    if c == 'q' or c == 'Q': return 0.0011
    if c == 'j' or c == 'J': return 0.0010
    if c == 'z' or c == 'Z': return 0.0007
    return 1.0

def count(needle, stack):
    """" Searches for the amount of needles in a stack """
    count_nr = 0
    for i in range(len(stack)):
        if stack[i] == needle:
            count_nr += 1
    return count_nr

def blsort(L):
    """" Returns a binary sorted List L """
    return [0] * count(0, L) + [1] * count(1, L)

def lcount(needle, string):
    """" Counts the amount a letter occurs in a string """
    count_nr = 0
    for n in range( len (string) ):
        if string[n] == needle:
            count_nr += 1
    return count_nr

def jscore(S, T):
    """" Counts how many times a character occurs in both strings """
    count_nr = 0
    for n in range( len( lowercase ) ):
        S_count = lcount( lowercase[n], S)
        T_count = lcount(lowercase[n], T)
        if( S_count > T_count):
            count_nr += T_count
        else:
            count_nr += S_count
    return count_nr

def exact_change (target_amount, L):
    """"" Determines if we can pay for target_amount exactly by the numbers in list L """
    if target_amount < 0:
        return False
    target_amount_list = target_amount + 1
    booleanList = [False]*target_amount_list
    booleanList[0] = True
    for n in L:
        for x in range(target_amount, -1, -1):
            if booleanList[x] and (x + n) <= target_amount:
                booleanList[x+n] = True
    return booleanList[target_amount]