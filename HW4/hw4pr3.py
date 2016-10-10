#
# hw4pr3.py
#
# Name: Ivo de Geus
#

import random

def rs():
    """ rs chooses a random step and returns it
    note that a call to rs() requires parentheses
    inputs: none at all!
    """
    return random.choice([-1,1])

def rwpos(start, nsteps):
    """ Returns a list of numbers using rs as positive or negative factor.
        Input: the starting point of the walker, and the amount of random steps left or right
        Output: Int of endpoint, based of start and random nsteps
    """
    if(nsteps == 0):
        return start
    start += rs()
    return rwpos( start, nsteps-1)

def rwsteps(start, low, hi):
    """ Prints a visual view of the sleepwalker, moving left or right. Stops once one of the low/hi is hit.
        Input: start: the starting point, and left and right borders.
        Output: the number of random steps from start until one of the borders is hit
    """
    if start == low:
        print '0' + ' ' * (hi-start) + '|'
        return 1
    elif start == hi:
        print '|' + ' ' * (start-low) + '0'
        return 1
    else:
        print '|' + ' ' * (start - low) + '0' + ' ' * (hi - start - 1) + '|'

    start += rs()
    steps_taken = rwsteps(start, low, hi)

    return steps_taken + 1

def rwposPlain(start, nsteps):
    """ Retuns the endpoint from start after nsteps with positive or negative factor.
        Input: starting point, and nsteps left or right
        Outpout: single int of steps from start after nsteps
    """
    if(nsteps == 0):
        return start
    start += rs()
    return rwpos( start, nsteps-1)



def ave_signed_displacement(numtrials):
    """ Returns the average displacement from 0
        Input: numtrials of the amount of tests
        Output: the average displacement from 0 based on numtrials
    """
    steps = 100
    LC = sum( [rwposPlain(0, steps) for x in range(numtrials)] ) / numtrials
    return LC

def ave_squared_displacement(numtrials):
    """ Returns the squared average displacement from 0
        Input: numtrials of the amount of tests
        Output: the squared average displacement from 0 based on numtrials
    """
    steps = 100
    LC = sum( [rwposPlain(0, steps) ** 2 for x in range(numtrials)] ) / numtrials
    return LC


"""
In order to compute the average signed displacement for
a random walker after 100 random steps, I ran the displacement
function based on variable steps, divided by the numtrials.

We see the results of the average and averages squared are closer to
0 once we increase the number of trials. This is because the extremes tend
to cancel eachother out. The squares are still high, but are also lower
once the numtrials rise.
"""