import pygame
import os

pygame.init()

screen_width = 1000
screen_height = 600

# PYGAME SCREEN
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Memory game - forest and animals")
game_icon = pygame.image.load('meza_dzivnieki/beka.png')
pygame.display.set_icon(game_icon)
background_image = pygame.image.load('background.png')
# background_image = pygame.transform.scale(background_image, (screen_width, screen_height)
background_image = pygame.transform.scale(
    background_image, (screen_width, screen_height))
background_image_rectangle = background_image.get_rect()

# Creating list of pictures for the game
pictures_for_game = []
for item in os.listdir('meza_dzivnieki/'):
    pictures_for_game.append(item.split('.')[0])

print(pictures_for_game)


running = True
while running:
    screen.blit(background_image, background_image_rectangle)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit(), sys.exit()

    pygame.display.update()


pygame.display.flip()

pygame.quit()
exit()
