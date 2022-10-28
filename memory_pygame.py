from sys import exit
import sys
from asyncore import close_all
import pygame
import random


pygame.init()

# variables, constants for the game
timer = pygame.time.Clock()
fps = 60
antique_white = (255, 239, 219)
forest_green = (0, 100, 0)
black = (0, 0, 0)
blue = (0, 0, 255)
rows = 6
columns = 6
correct = [[0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0]]


options_list = []
spaces = []
used = []
new_board = True
first_guess = False
second_guess = False
first_guess_number = 0
second_guess_number = 0
score = 0
matches = 0
best_score = 0
# game_over = False

# need to find the folder and drop it in
title_font = pygame.font.Font('freesansbold.ttf', 51)
regular_font = pygame.font.Font('freesansbold.ttf', 25)
tiny_font = pygame.font.Font('freesansbold.ttf', 12)

# create screen
new_board = True
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Memory game - forest and its creatures!")


def make_board():
    global options_list
    global spaces
    global used
    for item in range(rows * columns // 2):
        options_list. append(item)

    for item in range(rows * columns):
        # have to exchange these to images
        piece = options_list[random.randint(0, len(options_list) - 1)]
        spaces.append(piece)
        if piece in used:
            used.remove(piece)
            options_list.remove(piece)
        else:
            used.append(piece)


def make_backgrounds():
    global current_turns
    global previous_best_score
    top_menu = pygame.draw.rect(screen, black, [0, 0, 1000, 70])
    title = title_font.render("The Memory Game", True, antique_white)  # define
    screen.blit(title, (260, 20))  # draw on screen
    board_space = pygame.draw.rect(screen, antique_white, [250, 100, 500, 500])
    bottom_menu = pygame.draw.rect(screen, black, [0, 580, 1000, 20])
    restart_text = regular_font.render(
        'Restart', True, antique_white)
    screen.blit(restart_text, (850, 540))
    # restart_button = pygame.draw.rect(
    #     screen, antique_white, [10, 850, 540, 100])
    score_text = regular_font.render(
        f'Current turns: {score}', True, antique_white)
    screen.blit(score_text, (770, 200))
    best_text = regular_font.render(
        f'Previous best: {best_score}', True, antique_white)
    screen.blit(best_text, (770, 400))
    # return restart_button


def board_specifications():
    global rows
    global columns
    pieces_tracked = []
    board_list = []
    for i in range(columns):
        for j in range(rows):
            piece = pygame.draw.rect(
                screen, black, [i * 80 + 270, j * 80 + 108, 60, 60], 0, 4)
            pieces_tracked.append(piece)
            # gonna have to take out, as I will have images(next 3 lines)
            # piece_text = regular_font.render(
            #     f"{spaces[i * rows +j]}", True, antique_white)
            # screen.blit(piece_text, (i * 80 + 292, j * 80 + 125))

    for r in range(rows):
        for c in range(columns):
            if correct[r][c] == 1:
                pygame.draw.rect(screen, blue, [
                    c * 80 + 270, r * 80 + 105, 63, 63], 3, 4)
                piece_text = regular_font.render(
                    f"{spaces[c * rows +r]}", True, blue)
                screen.blit(piece_text, (c * 80 + 292, r * 80 + 125))

    return pieces_tracked


def check_guesses(first, second):
    global spaces
    global correct
    global matches
    global score

    if spaces[first] == spaces[second]:
        column1 = first // rows
        column2 = second // rows
        row1 = first - (column1 * rows)
        row2 = second - (column2 * rows)
        if correct[row1][column1] == 0 and correct[row2][column2] == 0:
            correct[row1][column1] = 1
            correct[row2][column2] = 1
            score += 1
            matches += 1
    else:
        score += 1


running = True
while running:
    timer.tick(fps)
    if new_board == True:
        make_board()
        print(spaces)
        new_board = False

    # restart = make_backgrounds
    make_backgrounds()
    board = board_specifications()

    if first_guess and second_guess:
        check_guesses(first_guess_number, second_guess_number)
        pygame.time.delay(1000)
        first_guess = False
        second_guess = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit(), sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(board)):
                button = board[i]
                if button.collidepoint((event.pos)) and not first_guess:
                    first_guess = True
                    first_guess_number = i
                    print(i)
                if button.collidepoint((event.pos)) and not second_guess and first_guess and i != first_guess_number:
                    second_guess = True
                    second_guess_number = i
                    print(i)
            # if restart.collidepoint(event.pos):
            #     options_list = []
            #     used = []
            #     spaces = []
            #     new_board = []
            # score = 0
            # matches = 0
            # first_guess = False
            # second_guess = False

            # correct = [[0, 0, 0, 0, 0, 0],
            #            [0, 0, 0, 0, 0, 0],
            #            [0, 0, 0, 0, 0, 0],
            #            [0, 0, 0, 0, 0, 0],
            #            [0, 0, 0, 0, 0, 0],
            #            [0, 0, 0, 0, 0, 0]]
            # game_over = False  ALLL OF THIS SHOULD GO INTO FUNCTION

# if matches == 18:
#     game_over = Truewinner = pygame.draw.rect(
#         screen, blue, [10, 300, 800, 80], 0, 5)
#     winner_text = title_font(f"You won in {score} moves!", True, black)

# screen.blit(winner_text, (10, 320))
# if best_score > score or best_score == 0:
#     best_score = score

# if first_guess:
#     piece_text = regular_font.render(
#         f'{spaces[first_guess_number]}', True, blue)
#     location = (first_guess_number // rows * 75 + 270,
#                 (first_guess_number - (first_guess_number//rows * rows)) * 65 + 120)
#     screen.blit(piece_text, (location))

    pygame.display.flip()

pygame.quit()
exit()
