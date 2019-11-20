"""
Connect 5 game!

This file is what is run to pay connect 5. It will use data structures and
information from other files to run in the __main__ function.

@Author: Kyle Ferreira
@Date: 2019/10/24
"""
import sys
import pygame
import pickle
from pygame import gfxdraw
from Board import Board
from Player import Player, Human, EasyAI, MediumAI, HardAI
from Game import Game

pygame.init()
WIDTH = int(pygame.display.Info().current_w)
HEIGHT = int(pygame.display.Info().current_h)
DIMENSION = 19
RECTANGLES = {}
settings_grid = {}
game_state = 0  # indicates menu state
game_mode = 0
p1_colour = (0, 0, 0)
p2_colour = (255, 255, 255)
board_colour = (121, 122, 125)
board_lines_colour = (255, 255, 255)
rect_size = int(WIDTH // DIMENSION * 0.5)
border = 5

red_button = pygame.image.load("button red.png")
blue_button = pygame.image.load("button blue.png")
colour_wheel = pygame.image.load("colour line.png")


def set_up_game() -> Game:
    """
    This function sets up the logic and data structures for the game by
    initializing relevant classes
    """
    global game_mode
    game_board = Board(DIMENSION)
    player1 = Human("Player 1", game_board)
    if game_mode == 0:
        return Game(player1, Human("Player 2", game_board), game_board)
    elif game_mode == 1:
        return Game(player1, EasyAI("Player 2", game_board), game_board)
    elif game_mode == 2:
        return Game(player1, MediumAI("Player 2", game_board), game_board)
    elif game_mode == 3:
        return Game(player1, HardAI("Player 2", game_board), game_board)


def draw_menu() -> dict:
    """
    This function draws the game menu. It fills the background colour, sets
    the fonts, and writes the text on the screen.
    :return: None
    """
    click_able = {}

    # fill menu background colour
    screen.fill((15, 82, 87))
    # create fonts for game use
    title_font = pygame.font.SysFont("Agency FB",
                                     int(screen.get_width() / 10),
                                     True, False)
    game_font = pygame.font.SysFont("Agency FB",
                                    int(screen.get_width() / 30),
                                    False, False)

    # menu title text
    title = title_font.render("Connect 5", True, (252, 17, 17), None)
    title_surface = title.get_rect()
    title_surface.center = (screen.get_width() // 2,
                            screen.get_height() // 6)
    screen.blit(title, title_surface)

    # menu play game text
    play_game = game_font.render("Play Game", True, (121, 247, 241), None)
    play_game_surface = play_game.get_rect()
    play_game_surface.center = (screen.get_width() // 2,
                                2 * screen.get_height() // 6)
    screen.blit(play_game, play_game_surface)
    click_able["play"] = play_game_surface

    # menu exit game text
    exit_game = game_font.render("Exit Game", True, (121, 247, 241), None)
    exit_game_surface = exit_game.get_rect()
    exit_game_surface.center = (screen.get_width() // 2,
                                5 * screen.get_height() // 6)
    screen.blit(exit_game, exit_game_surface)
    click_able["exit"] = exit_game_surface

    # game mode text
    if game_mode == 0:
        game_mode_text = game_font.render("Player vs Player", True,
                                          (121, 247, 241), None)
    elif game_mode == 1:
        game_mode_text = game_font.render("Player vs AI(Easy)", True,
                                          (121, 247, 241), None)
    elif game_mode == 2:
        game_mode_text = game_font.render("Player vs AI(Medium)", True,
                                          (121, 247, 241), None)
    else:
        game_mode_text = game_font.render("Player vs AI(Hard)", True,
                                          (121, 247, 241), None)
    game_mode_surface_text = game_mode_text.get_rect()
    game_mode_surface_text.center = (screen.get_width() // 2,
                                     3 * screen.get_height() // 6)
    screen.blit(game_mode_text, game_mode_surface_text)
    click_able["mode"] = game_mode_surface_text

    # settings text
    settings_game = game_font.render("Settings", True, (121, 247, 241), None)
    settings_game_surface = settings_game.get_rect()
    settings_game_surface.center = (screen.get_width() // 2,
                                    4 * screen.get_height() // 6)
    screen.blit(settings_game, settings_game_surface)
    click_able["settings"] = settings_game_surface

    # update screen
    pygame.display.update()

    # return all click-able text
    return click_able


def start_menu() -> None:
    """
    This function calls draw menu to draw the graphics for the menu, and then
    waits for user input via listening for mouse clicks.
    :return: None
    """
    # update screen
    click_able = draw_menu()
    # check for mouse clicks
    global game_state
    global game_mode
    while game_state == 0:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            # user exits via builtin close button
            if event.type == pygame.QUIT:
                pygame.display.quit()
                sys.exit()
            # user exits via clicking in the area described by exit game
            elif pygame.mouse.get_pressed()[0]:
                if click_able["exit"].collidepoint(mouse):
                    pygame.display.quit()
                    sys.exit()
                elif click_able["play"].collidepoint(mouse):
                    game_state = 1
                elif click_able["mode"].collidepoint(mouse):
                    if game_mode < 3:
                        game_mode += 1
                        click_able = draw_menu()
                    else:
                        game_mode = 0
                        click_able = draw_menu()
                elif click_able["settings"].collidepoint(mouse):
                    game_state = 2


def draw_settings() -> dict:
    click_able = {}

    screen.fill((15, 82, 87))

    pane = pygame.draw.rect(screen, (15, 82, 87),
                            (0, HEIGHT - (HEIGHT * 0.4), WIDTH, HEIGHT // 2))

    game_font = pygame.font.SysFont("Agency FB",
                                    int(screen.get_width() / 30),
                                    False, False)

    back = game_font.render("Back to main menu", True, (121, 247, 241), None)
    back_surface = back.get_rect()
    back_surface.center = (pane.center[0] * 0.3, pane.top * 0.2)
    screen.blit(back, back_surface)
    click_able["back"] = back_surface

    p1 = game_font.render("Pick player1's colour!", True, (121, 247, 241), None)
    p1_surface = p1.get_rect()
    p1_surface.center = (pane.center[0] // 2, pane.top)
    screen.blit(p1, p1_surface)

    p2 = game_font.render("Pick player2's colour!", True, (121, 247, 241), None)
    p2_surface = p2.get_rect()
    p2_surface.center = (pane.center[0] // 2, pane.top * 1.4)
    screen.blit(p2, p2_surface)

    board = game_font.render("Pick the board's colour!", True, (121, 247, 241),
                             None)
    board_surface = board.get_rect()
    board_surface.center = (pane.center[0] * 1.5, pane.top)
    screen.blit(board, board_surface)

    default = game_font.render("Default Settings", True, (121, 247, 241), None)
    default_surface = default.get_rect()
    default_surface.center = (pane.center[0] * 1.5, pane.top * 1.4)
    screen.blit(default, default_surface)
    click_able["default"] = default_surface

    a_surface = colour_wheel.get_rect()
    a_surface.center = (pane.center[0] // 2, pane.top + (pane.top * 0.1))
    screen.blit(colour_wheel, a_surface)
    click_able["a"] = a_surface

    b_surface = colour_wheel.get_rect()
    b_surface.center = (pane.center[0] // 2, pane.top * 1.4 + (pane.top * 0.1))
    screen.blit(colour_wheel, b_surface)
    click_able["b"] = b_surface

    c_surface = colour_wheel.get_rect()
    c_surface.center = (pane.center[0] * 1.5, pane.top + (pane.top * 0.1))
    screen.blit(colour_wheel, c_surface)
    click_able["c"] = c_surface

    # Variables needed for default board
    x = pane.center[0] - (25 * 5)
    y = pane.top - (pane.top * 0.4)

    # Creates a default visual board
    for row in range(5):
        for column in range(5):
            pygame.draw.rect(screen, (51, 51, 51),
                             (x + 10, y + 10, 50, 50))
            pygame.draw.rect(screen, board_colour, (x, y, 50, 50))
            x += 50 + 5
        y += 50 + 5
        x = pane.center[0] - (25 * 5)

    pygame.gfxdraw.aacircle(screen,
                            pane.center[0] // 2 + int(pane.center[0] * 0.25),
                            pane.top, 15, p1_colour)
    pygame.gfxdraw.filled_circle(screen,
                                 pane.center[0] // 2 + int(
                                     pane.center[0] * 0.25),
                                 pane.top, 15, p1_colour)

    pygame.gfxdraw.aacircle(screen,
                            pane.center[0] // 2 + int(pane.center[0] * 0.25),
                            int(pane.top * 1.4), 15, p2_colour)
    pygame.gfxdraw.filled_circle(screen,
                                 pane.center[0] // 2 + int(
                                     pane.center[0] * 0.25),
                                 int(pane.top * 1.4), 15, p2_colour)

    pygame.display.update()

    return click_able


def start_settings() -> None:
    # update screen
    click_able = draw_settings()
    # check for mouse clicks
    global game_state
    global game_mode
    global p1_colour
    global p2_colour
    global board_colour
    global a

    while game_state == 2:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            # user exits via builtin close button
            if event.type == pygame.QUIT:
                pygame.display.quit()
                sys.exit()
            # user exits via clicking in the area described by exit game
            elif pygame.mouse.get_pressed()[0]:
                if click_able["a"].collidepoint(mouse):
                    p1_colour = colour_wheel.get_at((mouse[0] - click_able[
                        "a"].x, mouse[1] - click_able["a"].y))
                    draw_settings()
                elif click_able["b"].collidepoint(mouse):
                    p2_colour = colour_wheel.get_at((mouse[0] - click_able[
                        "b"].x, mouse[1] - click_able["b"].y))
                    draw_settings()
                elif click_able["c"].collidepoint(mouse):
                    board_colour = colour_wheel.get_at((mouse[0] - click_able[
                        "c"].x, mouse[1] - click_able["c"].y))
                    draw_settings()
                elif click_able["back"].collidepoint(mouse):
                    game_state = 0
                elif click_able["default"].collidepoint(mouse):
                    p1_colour = (0, 0, 0)
                    p2_colour = (255, 255, 255)
                    board_colour = (121, 122, 125)
                    draw_settings()


def draw_game(game_board: Board) -> dict:
    """
    This function draws the game board on the screen using pygame. This function
    can be called repeatedly to update visuals of the pieces on the board as
    needed.
    It is currently unimplemented
    :return: None
    """
    click_able = {}
    # fill menu background colour
    screen.fill((15, 82, 87))

    game_font = pygame.font.SysFont("Agency FB",
                                    int(screen.get_width() / 30),
                                    False, False)

    button_font = pygame.font.SysFont("Agency FB",
                                      int(screen.get_width() / 50),
                                      False, False)

    # Variables needed for default board
    x = (WIDTH // 2) - ((rect_size // 2 + (border // 2)) * DIMENSION)
    y = (HEIGHT // 2) - ((rect_size // 2 + (border // 2)) * DIMENSION)
    global RECTANGLES

    # Creates a default visual board
    for row in range(game_board.dimension):
        for column in range(game_board.dimension):
            pygame.draw.rect(screen, (51, 51, 51),
                             (x + 10, y + 10, rect_size, rect_size))
            rect = pygame.draw.rect(screen, board_colour,
                                    (x, y, rect_size, rect_size))
            RECTANGLES[(row, column)] = rect
            x += rect_size + border
        y += rect_size + border
        x = (WIDTH // 2) - ((rect_size // 2 + (border // 2)) * DIMENSION)

    save_game = game_font.render("Save Game", True, (121, 247, 241), None)
    save_game_surface = save_game.get_rect()
    save_game_surface.center = (5.25 * screen.get_width() // 6,
                                2.5 * screen.get_height() // 6)

    screen.blit(save_game, save_game_surface)
    click_able["Save Game"] = save_game_surface

    load_game = game_font.render("Load Game", True, (121, 247, 241), None)
    load_game_surface = load_game.get_rect()
    load_game_surface.center = (5.25 * screen.get_width() // 6,
                                3.5 * screen.get_height() // 6)

    screen.blit(load_game, load_game_surface)
    click_able["Load Game"] = load_game_surface

    game_over = game_font.render("Winner: ", True,
                                 (121, 247, 241), None)
    game_over_surface = game_over.get_rect()
    game_over_surface.center = (0.4 * screen.get_width() // 6,
                                3 * screen.get_height() // 6)
    screen.blit(game_over, game_over_surface)

    # buttons
    pane = pygame.draw.rect(screen, (15, 82, 87),
                            (WIDTH - (WIDTH * 0.98),
                             HEIGHT - (HEIGHT * 0.1), 370, 100), 1)

    restart = button_font.render("Restart", True,
                                 (121, 247, 241), None)
    restart_surface = restart.get_rect()
    restart_surface.center = (pane.left + 100, pane.center[1] - 75)
    screen.blit(restart, restart_surface)

    menu = button_font.render("Menu", True,
                              (121, 247, 241), None)
    menu_surface = menu.get_rect()
    menu_surface.center = (pane.right - 100, pane.center[1] - 75)
    screen.blit(menu, menu_surface)

    restart_surface = red_button.get_rect()
    restart_surface.center = (pane.left + 100, pane.center[1])
    screen.blit(red_button, restart_surface)
    click_able["restart"] = restart_surface

    menu_surface = blue_button.get_rect()
    menu_surface.center = (pane.right - 100, pane.center[1])
    screen.blit(blue_button, menu_surface)
    click_able["menu"] = menu_surface

    # update screen
    pygame.display.update()

    return click_able


def update(row, col, game, player):
    rect = RECTANGLES[(row, col)]
    if player == game.player1:
        pygame.gfxdraw.aacircle(screen, rect.center[0], rect.center[1],
                                rect_size // 2, p1_colour)
        pygame.gfxdraw.filled_circle(screen, rect.center[0], rect.center[1],
                                     rect_size // 2, p1_colour)
    elif player == game.player2:
        pygame.gfxdraw.aacircle(screen, rect.center[0], rect.center[1],
                                rect_size // 2, p2_colour)
        pygame.gfxdraw.filled_circle(screen, rect.center[0], rect.center[1],
                                     rect_size // 2, p2_colour)

    pygame.display.update()


def is_clicked(click_able, mouse_position, new_game):
    global game_state
    if click_able["Save Game"].collidepoint(mouse_position):
        with open('objs.pickle', 'wb') as f:
            pickle.dump(new_game.board, f)
            f.close()
    elif click_able["Load Game"].collidepoint(mouse_position):
        with open('objs.pickle', 'rb') as f:
            old_board = pickle.load(f)
            # FINISH LOAD FUNCTION

    elif click_able["restart"].collidepoint(mouse_position):
        start_game()
    elif click_able["menu"].collidepoint(mouse_position):
        game_state = 0


def start_game() -> None:
    """
    This function calls for the game board to be drawn on the screen. It then
    waits for user input via listening for mouse clicks
    :return:
    """
    global game_mode
    global game_state
    new_game = set_up_game()
    new_game.player1.set_colour(p1_colour)
    new_game.player2.set_colour(p2_colour)
    click_able = draw_game(new_game.board)
    while game_state == 1:
        # check for mouse clicks
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                sys.exit()
            if not new_game.is_game_over():
                if pygame.mouse.get_pressed()[0] and \
                        isinstance(new_game.whose_turn(), Human):
                    for i in RECTANGLES:
                        if RECTANGLES[i].collidepoint(pygame.mouse.get_pos()):
                            if new_game.board.is_empty(i[0], i[1]):
                                new_game.make_move(i[0], i[1])
                                update(i[0], i[1], new_game,
                                       new_game.who_goes_next())
                    is_clicked(click_able, pygame.mouse.get_pos(), new_game)
                # AI's Turn
                elif new_game.whose_turn() == new_game.player2 and \
                        not isinstance(new_game.player2, Human):
                    x, y = new_game.player2.get_move()
                    new_game.make_move(x, y)
                    update(x, y, new_game, new_game.who_goes_next())
            else:
                game_font = pygame.font.SysFont("Agency FB",
                                                int(screen.get_width() // 30),
                                                False, False)
                if not new_game.is_winner() == "":
                    game_over = game_font.render(new_game.who_goes_next().name,
                                                 True,
                                                 (57, 255, 20), None)
                    game_over_surface = game_over.get_rect()
                    game_over_surface.center = (screen.get_width() // 6,
                                                3 * screen.get_height() // 6)
                    screen.blit(game_over, game_over_surface)

                else:
                    game_over = game_font.render("Tie",
                                                 True,
                                                 (57, 255, 20), None)
                    game_over_surface = game_over.get_rect()
                    game_over_surface.center = (screen.get_width() // 6,
                                                3 * screen.get_height() // 6)
                    screen.blit(game_over, game_over_surface)

                if pygame.mouse.get_pressed()[0]:
                    is_clicked(click_able, pygame.mouse.get_pos(), new_game)

                pygame.display.update()


if __name__ == "__main__":
    # import python_ta
    # python_ta.check_all()
    screen = pygame.display.set_mode([WIDTH, HEIGHT], pygame.FULLSCREEN)
    pygame.display.set_caption("Connect 5")
    while True:
        # menu state
        if game_state == 0:
            start_menu()
        # game state
        elif game_state == 1:
            start_game()
        # settings state
        elif game_state == 2:
            start_settings()
