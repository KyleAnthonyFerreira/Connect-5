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
p1_colour = (255, 255, 255)
p2_colour = (0, 0, 0)
board_colour = (121, 122, 125)
board_lines_colour = (255, 255, 255)
rect_size = int(WIDTH // DIMENSION * 0.5)
r_d = {}
border = 5

a = pygame.image.load("colour line.png")

def set_up_game()->Game:
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


def draw_menu()->dict:
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
                                3 * screen.get_height() // 6)
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
                                     4 * screen.get_height() // 6)
    screen.blit(game_mode_text, game_mode_surface_text)
    click_able["mode"] = game_mode_surface_text

    #settings text
    settings_game = game_font.render("Settings", True, (121, 247, 241), None)
    settings_game_surface = settings_game.get_rect()
    settings_game_surface.center = (screen.get_width() // 2,
                                5 * screen.get_height() // 6)
    screen.blit(settings_game, settings_game_surface)
    click_able["settings"] = settings_game_surface

    # update screen
    pygame.display.update()

    # return all click-able text
    return click_able


def start_menu()->None:
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

    game_font = pygame.font.SysFont("Agency FB",
                                    int(screen.get_width() / 30),
                                    False, False)

    back = game_font.render("Back to main menu", True, (121, 247, 241), None)
    back_surface = back.get_rect()
    back_surface.center = (screen.get_width() // 6,
                           screen.get_height() // 6)
    screen.blit(back, back_surface)
    click_able["back"] = back_surface

    p1 = game_font.render("Pick player1's colour!", True, (121, 247, 241), None)
    p1_surface = p1.get_rect()
    p1_surface.center = (screen.get_width() // 6,
                           4 * screen.get_height() // 6)
    screen.blit(p1, p1_surface)

    p2 = game_font.render("Pick player2's colour!", True, (121, 247, 241), None)
    p2_surface = p2.get_rect()
    p2_surface.center = (screen.get_width() // 6,
                           5 * screen.get_height() // 6)
    screen.blit(p2, p2_surface)

    board = game_font.render("Pick the board's colour!", True, (121, 247, 241), None)
    board_surface = board.get_rect()
    board_surface.center = (4.1 * screen.get_width() // 6,
                           4 * screen.get_height() // 6)
    screen.blit(board, board_surface)

    default = game_font.render("Default Settings", True, (121, 247, 241), None)
    default_surface = default.get_rect()
    default_surface.center = (3.85 * screen.get_width() // 6,
                           5 * screen.get_height() // 6)
    screen.blit(default, default_surface)
    click_able["default"] = default_surface

    a_surface = a.get_rect()
    a_surface.center = (screen.get_width() // 4,
                           4.5 * screen.get_height() // 6)
    screen.blit(a, a_surface)
    click_able["a"] = a_surface

    b_surface = a.get_rect()
    b_surface.center = (screen.get_width() // 4,
                           5.5 * screen.get_height() // 6)
    screen.blit(a, b_surface)
    click_able["b"] = b_surface

    c_surface = a.get_rect()
    c_surface.center = (3 * screen.get_width() // 4,
                           4.5 * screen.get_height() // 6)
    screen.blit(a, c_surface)
    click_able["c"] = c_surface

    pygame.draw.rect(screen, board_lines_colour, (int((2.5 * WIDTH) / 4) - 1, int(HEIGHT / 3.5) - 1, 5 * int(WIDTH / (32)) + 1, 5 * int(WIDTH / (32)) + 1))

    for x in range(5):
        for y in range(5):
            settings_grid[(x, y)] = \
                pygame.draw.rect(screen, board_colour, (int((2.5 * WIDTH) / 4) + x * int(WIDTH / (32)), int(HEIGHT / 3.5) + y * int(WIDTH / (32)), int(WIDTH / (32)) - 1, int(WIDTH / (32)) - 1))

    pygame.gfxdraw.aacircle(screen, screen.get_width() // 3,
                                    4 * screen.get_height() // 6, 15, p1_colour)
    pygame.gfxdraw.filled_circle(screen, screen.get_width() // 3,
                                    4 * screen.get_height() // 6, 15, p1_colour)

    pygame.gfxdraw.aacircle(screen, screen.get_width() // 3,
                                    5 * screen.get_height() // 6, 15, p2_colour)
    pygame.gfxdraw.filled_circle(screen, screen.get_width() // 3,
                                    5 * screen.get_height() // 6, 15, p2_colour)

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
    global board_lines_colour
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
                    p1_colour = a.get_at((mouse[0] - int((WIDTH // 4) - 278), mouse[1] - int(4.5 * (HEIGHT // 6) - 8)))
                    draw_settings()
                elif click_able["b"].collidepoint(mouse):
                    p2_colour = a.get_at((mouse[0] - int((WIDTH // 4) - 278), mouse[1] - int(5.5 * (HEIGHT // 6) - 8)))
                    draw_settings()
                elif click_able["c"].collidepoint(mouse):
                    board_colour = a.get_at((mouse[0] - int((3 * WIDTH // 4) - 278), mouse[1] - int(4.5 * (HEIGHT // 6) - 8)))
                    draw_settings()
                elif click_able["back"].collidepoint(mouse):
                    game_state = 0
                elif click_able["default"].collidepoint(mouse):
                    p1_colour = (255, 255, 255)
                    p2_colour = (0, 0, 0)
                    board_colour = (121, 122, 125)
                    draw_settings()


def draw_game(game_board: Board, player1: Player, player2: Player)->dict:
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

    inst_font = pygame.font.SysFont("Agency FB",
                                    int(screen.get_width() / 45),
                                    False, False)

    # Variables needed for default board
    x = (WIDTH // 2) - ((rect_size//2+(border//2)) * DIMENSION)
    y = (HEIGHT // 2) - ((rect_size//2+(border//2)) * DIMENSION)
    counter = 0
    global r_d

    # Creates a default visual board
    for row in range(game_board.dimension):
        for column in range(game_board.dimension):
            rect = pygame.draw.rect(screen, board_colour, (x, y, rect_size, rect_size))
            r_d[(row, column)] = rect
            counter += 1
            x += rect_size + border
        y += rect_size + border
        x = (WIDTH // 2) - ((rect_size//2+(border//2)) * DIMENSION)

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
                                2.5 * screen.get_height() // 6)
    screen.blit(game_over, game_over_surface)

    instructions = inst_font.render('"M" = Menu | "R" = Reset', True,
                                 (121, 247, 241), None)
    instructions_surface = instructions.get_rect()
    instructions_surface.center = (0.68 * screen.get_width() // 6,
                                3.5 * screen.get_height() // 6)
    screen.blit(instructions, instructions_surface)

    # update screen
    pygame.display.update()

    return click_able


def update(row, col, game, player):
    rect = r_d[(row, col)]
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


def start_game()->None:
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
    click_able = draw_game(new_game.board, new_game.player1, new_game.player2)
    while game_state == 1:
        # check for mouse clicks
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    start_game()
                if event.key == pygame.K_m:
                    game_state = 0
            if not new_game.is_game_over():
                if pygame.mouse.get_pressed()[0] and \
                        isinstance(new_game.whose_turn(), Human):
                    mouse_position = pygame.mouse.get_pos()
                    for i in r_d:
                        if r_d[i].collidepoint(mouse_position):
                            if not new_game.is_game_over() and \
                                    new_game.board.is_empty(i[0], i[1]):
                                new_game.make_move(i[0], i[1])
                                update(i[0], i[1], new_game, new_game.whose_turn())
                    if click_able["Save Game"].collidepoint(mouse_position):
                        with open('objs.pickle', 'wb') as f:
                            pickle.dump([new_game.board, new_game.player1, new_game.player2], f)
                            f.close()
                    elif click_able["Load Game"].collidepoint(mouse_position):
                        with open('objs.pickle', 'rb') as f:
                            new_game.board, new_game.player1, new_game.player2 = pickle.load(f)
                        draw_game(new_game.board, new_game.player1, new_game.player2)
                # AI's Turn
                elif new_game.whose_turn() == new_game.player2 and \
                        not isinstance(new_game.player2, Human):
                    if not new_game.is_game_over():
                        x, y = new_game.player2.get_move()
                        new_game.make_move(x, y)
                        update(x, y, new_game, new_game.whose_turn())
            if new_game.is_game_over():
                game_font = pygame.font.SysFont("Agency FB",
                                                int(screen.get_width() / 30),
                                                False, False)
                game_over = game_font.render(new_game.who_goes_next().name, True,
                                             (57, 255, 20), None)
                game_over_surface = game_over.get_rect()
                game_over_surface.center = (screen.get_width() // 6,
                                            2.5 * screen.get_height() // 6)
                screen.blit(game_over, game_over_surface)

                pygame.display.update()


if __name__ == "__main__":
    # import python_ta
    # python_ta.check_all()
    screen = pygame.display.set_mode([WIDTH, HEIGHT], pygame.FULLSCREEN)
    pygame.display.set_caption("Connect 5")
    while 1:
        # menu state
        if game_state == 0:
            start_menu()
        # game state
        elif game_state == 1:
            start_game()
        # settings state
        elif game_state == 2:
            start_settings()
