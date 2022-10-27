from sys import exit
import sys
from asyncore import close_all
import pygame

pygame.init()

# variables, constants for the game
timer = pygame.time.Clock()
fps = 60
antique_white = (255, 239, 219)
forest_green = (0, 100, 0)
black = (0, 0, 0)
rows = 6
columns = 6
correct = []
# need to find the folder and drop it in
title_font = pygame.font.Font('freesansbold.ttf', 51)
regular_font = pygame.font.Font('freesansbold.ttf', 25)

# create screen
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Memory game - forest and its creatures!")


def make_backgrounds():
    top_menu = pygame.draw.rect(screen, black, [0, 0, 500, 70])
    title = title_font.render("The Memory Game", True, antique_white)  # define
    screen.blit(title, (260, 20))  # draw on screen
    board_space = pygame.draw.rect(screen, antique_white, [250, 100, 500, 500])
    bottom_menu = pygame.draw.rect(screen, black, [0, 580, 1000, 20])


def make_board():
    global rows
    global columns
    for i in range(columns):
        for j in range(rows):
            piece = pygame.draw.rect(
                screen, black, [i * 80 + 270, j * 80 + 108, 60, 60], 0, 4)


running = True
while running:
    timer.tick(fps)
    make_backgrounds()
    make_board()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit(), sys.exit()
    pygame.display.flip()

pygame.quit()
exit()
