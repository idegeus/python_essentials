#
# Name: Ivo de Geus
#
# hw3pr1.py (Lab 2, part 1)
# slicing and indexing challenges
#

#defining properties
pi = [3,1,4,1,5,9]
e = [2,7,1]

# Example problem (problem 0):
# Creating the list [2,5,9] from pi and e
answer0 = [ e[0] ] + pi[-2:]
print answer0

# Problem 1
answer1 = e[1:]
print answer1

# Problem 2
answer2 = pi[::-1][::2]
print answer2

# Problem 3
answer3 = pi[1:]
print answer3

# Problem 4
answer4 = e[::-1][::2] + pi[::2]
print answer4



#We'll be continuing after our short break
""""    4$$$$$$$$$$$$$$$$$$c   .d$$$$$$$$$$$$$$$P\
        4$$$$$$$$$$$$$$$$$$$$cd$$$$$$$$$$$$$$$$$F "r
        4$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$F  F ="=
        4$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$****$$$F  P    b
        4$$$$$$$$$$$$$$$$$$$$$$$$$$$P**"   .z$$$F."    @"
        4$$$$$$$$$$$$$$$$$$$$$$$$$"    .d$$$$$$$$"   /"
        4$$$$$$$$$$$$$$$$$$$$$$""     $P""$$$$$P   ."
        4$$$$$$$$$$$$$$$$$$$P"  z$$  4$   3$$$$   zF
        4$$$$$$$$$$$$$$$$$$F  z$$$$r  $.   $$$"  @ F
        4$$$$$$$$$$$$$$$$$$$$$$$$$$F  $$.  3$"  f  F
        4$$$$$$$$$$$$$$$*$$$$$$$$$$F  $$$r     dF  F
        4$$$$$$$$$$$$$$$  P$$$$P"$$"  $$$$    d$F  F
        4$$$$$$$$$$$$$$$  F  ""  $$   $$$$r   $$F  F
        4$$$$$$$$$$$$$$$  F      $$   $$$$$eed$$F  F
        4$$$$$$$$$$$$$$$  F      $$F  $$$$$$$$$$F  F
        4$$$$$$$$$$$$$$$ .F      $$$$$$$$$$$$$$$F  F
        4$$$$$$$$$$$$$$$@"       $$$$$$$$$$$$$$$Lr"  Gilo94' """
#Welcome Back!


# starting strings for Lab 1
# we realize the not many HMCers are in CS5 this term - but,
# as a result, these are probably equally (un)fair strings to use:

h = 'harvey'
m = 'mudd'
c = 'college'

# Problem 5:
# Creating the string 'heyyou'
answer5 = h[0] + h[4:] + h[-1] + c[1] + m[1]
print answer5

# Problem 6
answer6 = c[0:4] + m[1:3] + c[6:]
print answer6

# Problem 7
answer7 = h[1:] + m[1:]
print answer7

# Problem 8
answer8 = h[0:3] + m[3:] + c[6:] + (h[0:3] * 3)
print answer8

# Problem 9
answer9 = c[3:6] + c[1] + m[0] + h[5] + c[4:6] + c[1]
print answer9


# Problem 10
answer10 = c[:5:2] + h[1:3] + c[0] + h[1] + c[2:4]
print answer10





