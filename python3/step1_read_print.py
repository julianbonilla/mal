#!/usr/bin/env python

def READ(str):
    return str

def EVAL(input):
    return input

def PRINT(input):
    return input

def REP(input):
    return PRINT(EVAL(READ(input)))

while True:
    try:
        s = input('user> ')
        print(REP(s))
    except EOFError:
        exit()
