# coding=utf-8
# Name(s): Ivo de Geus
# Date: 12-9-2016
# four fours are above...
## here == an interactive program:
import os
import time             # includes a library named time
import random           # a random library
import sys              # the system library (printing to screen, etc.)
import Tkinter as tk

#defining global variables
yc = ''
mc = ''
possibilities = ['rock', 'paper', 'scissors']
saw = ("\n"
       "─────▄██▀▀▀▀▀▀▀▀▀▀▀▀▀██▄─────\n"
       "────███───────────────███────\n"
       "───███─────────────────███───\n"
       "──███───▄▀▀▄─────▄▀▀▄───███──\n"
       "─████─▄▀────▀▄─▄▀────▀▄─████─\n"
       "─████──▄████─────████▄──█████\n"
       "█████─██▓▓▓██───██▓▓▓██─█████\n"
       "█████─██▓█▓██───██▓█▓██─█████\n"
       "█████─██▓▓▓█▀─▄─▀█▓▓▓██─█████\n"
       "████▀──▀▀▀▀▀─▄█▄─▀▀▀▀▀──▀████\n"
       "███─▄▀▀▀▄────███────▄▀▀▀▄─███\n"
       "███──▄▀▄─█──█████──█─▄▀▄──███\n"
       "███─█──█─█──█████──█─█──█─███\n"
       "███─█─▀──█─▄█████▄─█──▀─█─███\n"
       "███▄─▀▀▀▀──█─▀█▀─█──▀▀▀▀─▄███\n"
       "████─────────────────────████\n"
       "─███───▀█████████████▀───████\n"
       "─███───────█─────█───────████\n"
       "─████─────█───────█─────█████\n"
       "───███▄──█────█────█──▄█████─\n"
       "─────▀█████▄▄███▄▄█████▀─────\n"
       "──────────█▄─────▄█──────────\n"
       "\n")


#intro script
def intro():
    name = raw_input('Hi...what is your name?\n')
    print ''
    print 'Welcome,', name
    print 'I\'m happy you have finally arrived.'
    print 'Let\'s play a game.'
    print saw
    time.sleep(0.5)
    print '.',
    time.sleep(0.5)
    print '.',
    time.sleep(0.5)
    print '.',
    time.sleep(0.5)
    print '.'
    time.sleep(0.5)
    print ''

#repeatable questionnaire for playing game
def oneTry():
    while True:
        yc = raw_input("Choose Rock, Paper or Scissors\n").lower()
        mc = random.choice(possibilities)
        if yc in possibilities and mc in possibilities:
            print 'You chose', yc
            print 'I chose', mc
            return yc,mc
        else:
            print 'Please play fair, choose from the possibilities.'
            print ''

#finds out who won. 0=tie, 1=player, 2=computer
def whoWon(mc, yc):
    if mc == yc:
        return 0
    elif (yc == 'rock' and mc == 'scissors') or (yc == 'paper' and mc == 'rock') or (yc == 'scissors' and mc == 'paper'):
        return 1
    else:
        return 2


def mainProcess():
    while True:
        yc, mc = oneTry()
        if whoWon(mc, yc) == 0: #tie
            print 'It\'s a Tie! Let\'s try again'
        elif whoWon(mc, yc) == 1:
            print 'You won! I want a rematch!'
        elif whoWon(mc, yc) == 2:
            print 'Ha, I won! You might want a rematch.'
        else:
            print 'This should never happen. Throw a WTF error.'
        print ''

intro()
mainProcess()
