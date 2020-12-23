# Author: Justinas
## Attempt to recreate Diablo ##

import pygame
import sys
import os

display_height = 500
display_width = 500

grid_size = 50
grid_height = display_height / grid_size
grid_width = display_width / grid_size

pygame.init()
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('DIABLO')
clock = pygame.time.Clock()

Img1 = pygame.image.load(os.path.join("images","Diablo sticker.png"))

silver = (192, 192, 192)                          #RGB based so (more light bigger number,     ,     )
gray = (128, 128, 128)
dimGray = (105, 105, 105)
white = (255, 255, 255)
red = (255, 0, 0)
mediumBlue = (0, 0, 205)
dodgerBlue = (30, 144, 255)
crimson = (220, 20, 60)
indianRed = (205, 92, 92)
limeGreen = (50, 205, 50)
lime = (0, 255, 0)
black = (0, 0, 0)
beige = (245, 245, 220)

char_width = 84
char_height = 80

class Character:
    def __init__(self):
        self.name = "Bob"
        self.position = display_width * 0.1, display_height * 0.1

    def move(self):
        pass

class Npc:
    def __init__(self):
        self.name = ""
        self.position = display_width * 0.8, display_height * 0.7


def draw_grid(surface):
    for y in range(0, int(grid_height)):
        for x in range(0, int(grid_width)):
            if(x + y) % 2 == 0:
                r = pygame.Rect((x * grid_size, y * grid_size), (grid_size, grid_size))     
                pygame.draw.rect(surface, gray, r)
            else:
                rr = pygame.Rect((x * grid_size, y * grid_size), (grid_size, grid_size))
                pygame.draw.rect(surface, dimGray, rr)

def charImage(x,y):
        gameDisplay.blit(Img1, (x  ,y ))

def run_game():
    dead = False
    x = display_width * 0.8
    y = display_height * 0.8
    x_change = 0

    while not dead:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                dead = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        if x < display_width - char_width + 5 and x - 5 > 0:
            x += x_change
        else:
            x -= x_change
     
        gameDisplay.fill(gray)
        charImage(x, y)    

        pygame.display.update()
        clock.tick(10)


run_game()
pygame.quit()
quit()









