#!/usr/bin/env python

def READ(str):
    return str

def EVAL(input):
    return input

def PRINT(input):
    return input

def rep(input):
    return PRINT(EVAL(READ(input)))

while True:
    s = input('user> ')
    print(rep(s))
