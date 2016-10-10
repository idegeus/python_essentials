#
# hw1pr2.py (Lab1, part 2)
#
# Name: Ivo de Geus
# Date: 19-9-2016
#


def dbl(x):
    """  output: dbl returns twice its input
         input x: a number (int or float)
         Spam is great, and dbl("spam") is better!
    """
    return 2*x

def tpl(x):
    """ output: tpl returns thrice its input
         input x: a number (int or float)
    """
    return 3*x

def sq(x):
    """" output: sq returns the input squared
        input x: a number (int or float)
    """
    return x**2

def interp(low,hi,fraction):
    """" Gets the number on the fraction between low and high
    """
    return ( ( hi - low ) * fraction ) + low

def checkends(s):
    """" Checks string for the same starting as ending character.
        Outputs True if the first and last chars are same
    """
    return True if s[0] == s[-1] else False

def flipside(s):
    """" Splits string in half and reverses it.
        Input string, example foobar
        Output string, example barfoo
    """
    length = int(round(len(s)/2, 0))
    end = length*-1
    if((len(s)%2) == 0):
        end = end + 1
    return s[end-1:] + s[:length]


def convertFromSeconds(s):
    """" Input: INT seconds
        Output: list of increasingly specific time units:
        [days, hours, minutes, seconds] each subtracted
    """
    days = s / (24 * 60 * 60)  # # of days
    s = s % (24 * 60 * 60)  # the leftover
    hours = s / (60 * 60)
    s = s % (60 * 60)  # the leftover
    minutes = s / 60
    s = s % 60  # the leftover
    seconds = s
    return [days, hours, minutes, seconds]

def front3(s):
    """" Input: string
        Output: first three characters repeated. if less
         than three, the string repeated 3 times.
    """
    front = s[0:3]
    return front*3