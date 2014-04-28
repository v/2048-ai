#!/usr/bin/python
# -*- coding: utf-8 -*-

''' Help the user achieve a high score in a real game of threes by using a move searcher. '''

from __future__ import print_function
import ctypes
import time
import os

for suffix in ['so', 'dll', 'dylib']:
    dllfn = 'bin/2048.' + suffix
    if not os.path.isfile(dllfn):
        continue
    gamelib = ctypes.CDLL(dllfn)
    break
else:
    print("Couldn't find 2048 library bin/2048.{so,dll,dylib}! Make sure to build it first.")
    exit()

def main():
    gamelib.init_tables()

    result = gamelib.play_game_randomly()
    print(result)

if __name__ == '__main__':
    main()
