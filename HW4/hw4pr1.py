#
# hw4pr1.py
# name: Ivo de Geus

import turtle

wn = turtle.Screen()
p = turtle.Turtle()

def poly( n, N ):
    """ draws n sides of an N-sided regular polygon """
    if n == 0:
        return
    else:
        p.forward(50)   # 50 is hard-coded at the moment...
        p.left(360.0 / N)
        poly( n-1, N )

def spiral( initialLength, angle, multiplier ):
    """" Draws spiraling inside or outside line. """
    if initialLength < 1 or initialLength > 1000:
        wn.exitonclick()
    p.forward(initialLength)
    p.left(angle)
    spiral( initialLength * multiplier, angle, multiplier)

def chai(size):
    """ our chai function! """
    if (size<9):
        return
    else:
        p.forward(size)
        p.left(90)
        p.forward(size / 2.0)
        p.right(90)
        chai(size / 2)

        p.right(90)
        p.forward(size)
        p.left(90)
        chai( size/2 )

        p.left(90)
        p.forward(size / 2.0)
        p.right(90)
        p.backward(size)
        return

def svtree( trunklength, levels ):
    if(levels == 0):
        return

    p.width(levels)
    p.left(20)
    p.forward(trunklength)
    svtree(trunklength / 2, levels - 1)
    p.width(levels)
    p.backward(trunklength)
    p.right(20)

    p.right(20)
    p.forward(trunklength)
    svtree(trunklength / 2, levels - 1)
    p.width(levels)
    p.backward(trunklength)
    p.left(20)
    return

def snowflake(sidelength, levels):
    """ fractal snowflake function
    sidelength: pixels in the largest-scale triangle side
    levels: the number of recursive levels in each side
    """
    flakeside( sidelength, levels )
    p.left(120)
    flakeside( sidelength, levels )
    p.left(120)
    flakeside( sidelength, levels )
    p.left(120)

def flakeside(sidelength, levels):

    clength = sidelength / 3

    p.forward(clength)
    if(levels == 0):
        p.forward(clength)
    elif(levels == 1):
        p.right(45)
        flakeside(clength, 0)
        p.left(90)
        flakeside(clength, 0)
        p.right(45)
    elif(levels == 2):
        p.right(45)
        flakeside(clength / 3, 0)
        p.left(90)
        flakeside(clength / 3, 0)
        p.right(45)
    p.forward(clength)

    return


snowflake(100,3)
wn.exitonclick()
exit()