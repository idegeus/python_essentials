#
# hw4pr2.py
# List comprehensions!
#
# Name: Ivo de Geus
#


# this gives us functions like sin and cos...
from math import *


# two more functions (not in the math library above)
def dbl(x):
    """ doubler!  input: x, a number """
    return 2*x

def sq(x):
    """ squarer!  input: x, a number """
    return x**2


# exampled for getting used to list comprehensions...

def lc_dbl(N):
    """ this example takes in an int N
    and returns a list of integers
    from 0 to N-1, **each multiplied by 2**
    """
    return [dbl(x) for x in range(N) ]



# === Here is where your functions start for the lab: === #
# Step 1, part 1
def unitfracs(N):
    """ returns evenly distributed fracs of N.
        Input: int
        Output: evenly distributed list fracs based on input, eg: 3 -> [0, 0.33, 0.66]
    """
    return [float(x)/N for x in range(N) ]


def scaledfracs (lo, hi, N):
    """ Returns a list of N points between lo and hi
     Input: starting point, endpoint, amount of points between
     Output: List of evenly distributed points
    """
    return [(hi - lo) * x + lo for x in unitfracs(N)]


def sqfracs (lo, hi, N):
    """ Returns a list of N points between lo and hi, squared
     Input: starting point, endpoint, amount of points between
     Output: List of evenly distributed points squared
    """
    return [x**2 for x in scaledfracs(lo, hi, N)]


def f_of_fracs (f, lo, hi, N):
    """ Returns a list of N points between lo and hi, put through function f
     Input: function, starting point, endpoint, amount of points between
     Output: List of evenly distributed points, put through f
    """
    return [f(x) for x in scaledfracs(lo, hi, N)]


def integrate(f, low, hi, N):
    """ integrate returns an estimate of the definite integral
    of the function f (the first input)
    with lower limit low (the second input)
    and upper limit hi (the third input)
    where N steps are taken (the fourth input)

    integrate simply returns the sum of the areas of rectangles
    under f, drawn at the left endpoints of N uniform steps
    from low to hi
    """
    return (hi - (low * 1.0) ) / N * sum( f_of_fracs(f, low, hi, N) )