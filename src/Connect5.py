"""
Connect 5 game!

This file is what is run to pay connect 5. It will use data structures and
information from other files to run in the __main__ function.

@Author: Kyle Ferreira
@Date: 2019/10/24
"""
import sys
import pygame
import pytest

WIDTH = 800
HEIGHT = 450

if __name__ == "__main__":
    import python_ta
    python_ta.check_all()
    pygame.init()
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    game_open = True
    while 1:
        for event in pygame.event.get():
            """event.type == pygame.KEYDOWN or"""
            if event.type == pygame.QUIT:
                sys.exit()
