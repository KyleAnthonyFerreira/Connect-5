"""
Connect 5 game!

This file is what is run to pay connect 5. It will use data structures and
information from other files to run in the __main__ function.

@Author: Kyle Ferreira
@Date: 2019/10/24
"""
import sys
import pygame

WIDTH = 800
HEIGHT = 450
game_state = 0  # indicates menu state
pygame.init()


def draw_menu()->None:
    """
    This function draws the game menu. It fills the background colour, sets
    the fonts, and writes the text on the screen.
    :return: None
    """

    # fill menu background colour
    screen.fill((255, 160, 0))
    # create fonts for game use
    title_font = pygame.font.SysFont("Arial",
                                     int(screen.get_width() / 10),
                                     True, False)
    game_font = pygame.font.SysFont("Arial",
                                    int(screen.get_width() / 30),
                                    True, False)
    # menu title text
    title = title_font.render("Connect 5", True, (0, 0, 255), None)
    title_surface = title.get_rect()
    title_surface.center = (screen.get_width() // 2,
                            screen.get_height() // 6)
    screen.blit(title, title_surface)

    # menu play game text
    play_game = game_font.render("Play Game", True, (0, 0, 255), None)
    play_game_surface = play_game.get_rect()
    play_game_surface.center = (screen.get_width() // 2,
                                3 * screen.get_height() // 6)
    screen.blit(play_game, play_game_surface)

    # menu exit game text
    exit_game = game_font.render("Exit Game", True, (0, 0, 255), None)
    exit_game_surface = exit_game.get_rect()
    exit_game_surface.center = (screen.get_width() // 2,
                                4 * screen.get_height() // 6)
    screen.blit(exit_game, exit_game_surface)
    # pygame.draw.rect(screen, (255, 160, 0), (0, 0, WIDTH, HEIGHT))

    # update screen
    pygame.display.update()


def start_menu()->None:
    """
    This function calls draw menu to draw the graphics for the menu, and then
    waits for user input via listening for mouse clicks.
    :return: None
    """
    # update screen
    draw_menu()
    # check for mouse clicks
    global game_state
    while game_state == 0:
        for event in pygame.event.get():
            # user exits via builtin close button
            if event.type == pygame.QUIT:
                sys.exit()
            # user exits via clicking in the area described by exit game
            elif pygame.mouse.get_pressed()[0] \
                    and \
                    (3 * screen.get_width() // 7) < \
                    pygame.mouse.get_pos()[0] < \
                    (4 * screen.get_width() // 7) \
                    and \
                    (15 * screen.get_height() // 24) < \
                    pygame.mouse.get_pos()[1] < \
                    (17 * screen.get_height() // 24):
                sys.exit()
            # user selects to start the game
            elif pygame.mouse.get_pressed()[0] \
                    and \
                    (3 * screen.get_width() // 7) < \
                    pygame.mouse.get_pos()[0] < \
                    (4 * screen.get_width() // 7) \
                    and \
                    (11 * screen.get_height() // 24) < \
                    pygame.mouse.get_pos()[1] < \
                    (13 * screen.get_height() // 24):
                game_state = 1


def draw_game()->None:
    """
    This function draws the game board on the screen using pygame. This function
    can be called repeatedly to update visuals of the pieces on the board as
    needed.
    It is currently unimplemented
    :return: None
    """
    pass


def start_game()->None:
    """
    This function calls for the game board to be drawn on the screen. It then
    waits for user input via listening for mouse clicks
    :return:
    """
    while game_state == 1:
        # check for mouse clicks
        for event in pygame.event.get():
            # user exits via builtin close button
            if event.type == pygame.QUIT:
                sys.exit()


if __name__ == "__main__":
    # import python_ta
    # python_ta.check_all()
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    pygame.display.set_caption("Connect 5")
    while 1:
        # menu state
        if game_state == 0:
            start_menu()
        # game state
        elif game_state == 1:
            start_game()
