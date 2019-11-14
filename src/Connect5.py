"""
Connect 5 game!

This file is what is run to pay connect 5. It will use data structures and
information from other files to run in the __main__ function.

@Author: Kyle Ferreira
@Date: 2019/10/24
"""
import sys
import pygame
from Board import Board
from Player import Player, Human, EasyAI, MediumAI
from Game import Game

pygame.init()
WIDTH = int(pygame.display.Info().current_w / 1.2)
HEIGHT = int(pygame.display.Info().current_h / 1.2)
DIMENSION = 19
RECTANGLES = {}
game_state = 0  # indicates menu state


def set_up_game()->Game:
    """
    This function sets up the logic and data structures for the game by
    initializing relevant classes
    """
    game_board = Board(DIMENSION)
    player1 = Human("Player 1", game_board)
    player2 = MediumAI("Player 2", game_board)
    return Game(player1, player2, game_board)


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


def draw_game(game_board: Board, player1: Player, player2: Player)->None:
    """
    This function draws the game board on the screen using pygame. This function
    can be called repeatedly to update visuals of the pieces on the board as
    needed.
    It is currently unimplemented
    :return: None
    """
    # fill menu background colour
    screen.fill((255, 160, 0))

    # create a rectangle on the screen
    pygame.draw.rect(screen, (0, 0, 0),
                     ((WIDTH // 4) - 1, ((HEIGHT - (WIDTH // 2)) // 2) - 1,
                      (WIDTH // 2) + 1, (WIDTH // 2) + 1))

    # draw and store board boundaries
    for x in range(game_board.dimension):
        for y in range(game_board.dimension):
            RECTANGLES[(x, y)] = pygame.draw.rect(screen, (135, 206, 235), (int((WIDTH / 4) + x * (WIDTH / (2 * DIMENSION))), int(((HEIGHT - (WIDTH / 2)) / 2) + y * (WIDTH / (2 * DIMENSION))), int((WIDTH / (2 * DIMENSION)) - 1), int((WIDTH / (2 * DIMENSION)) - 1)))

    # tie colour to players
    player1_colour = (255, 255, 255)
    player2_colour = (0, 0, 0)
    # draw tiles to board

    for a in range(game_board.dimension):
        for b in range(game_board.dimension):
            if game_board.get_piece(a, b) == player1.name:
                pygame.draw.circle(screen, player1_colour, RECTANGLES[(a, b)].center, RECTANGLES[(a, b)].width // 2)
            elif game_board.get_piece(a, b) == player2.name:
                pygame.draw.circle(screen, player2_colour, RECTANGLES[(a, b)].center, RECTANGLES[(a, b)].width // 2)

    # update screen
    pygame.display.update()


def start_game()->None:
    """
    This function calls for the game board to be drawn on the screen. It then
    waits for user input via listening for mouse clicks
    :return:
    """
    new_game = set_up_game()
    draw_game(new_game.board, new_game.player1, new_game.player2)
    while game_state == 1:
        # check for mouse clicks
        for event in pygame.event.get():
            # user exits via builtin close button
            if event.type == pygame.QUIT:
                sys.exit()
            if not new_game.is_game_over():
                # Human's Turn
                if pygame.mouse.get_pressed()[0] and \
                        isinstance(new_game.whose_turn(), Human):
                    mouse_position = pygame.mouse.get_pos()
                    for i in RECTANGLES:
                        if RECTANGLES[i].collidepoint(mouse_position):
                            if not new_game.is_game_over():
                                new_game.make_move(i[0], i[1])
                                draw_game(new_game.board, new_game.player1,
                                          new_game.player2)
                                if new_game.is_winner():
                                    print("WINNER")
                # AI's Turn
                elif new_game.whose_turn() == new_game.player2 and \
                        not isinstance(new_game.player2, Human):
                    if not new_game.is_game_over():
                        x, y = new_game.player2.get_move()
                        new_game.make_move(x, y)
                        draw_game(new_game.board, new_game.player1,
                                  new_game.player2)
                    if new_game.is_winner():
                        print("WINNER")


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
