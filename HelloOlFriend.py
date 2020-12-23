# Author: Justinas
## Attempt to recreate Diablo ##

import pygame
import sys
import os

display_height = 480
display_width = 640
grid_size = 50
grid_height = display_height / grid_size
grid_width = display_width / grid_size

pygame.init()
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('DIABLO')
clock = pygame.time.Clock()

Img1 = pygame.image.load(os.path.join("images","Humanimage.png"))
gameIcon = pygame.image.load(os.path.join("images","Diablo sticker2.png"))
pygame.display.set_icon(gameIcon)

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

char_width = 80
char_height = 80
##
class Character:
    def __init__(self):
        self.name = "Bob"
        self.position = display_width * 0.1, display_height * 0.1

    def move(self):
        pass
##
class Npc:
    def __init__(self):
        self.name = ""
        self.position = display_width * 0.8, display_height * 0.7

##
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

#def processEvents():


def run_game():
    dead = False
    x = display_width * 0.8
    y = display_height * 0.8
    x_change = 0
    y_change = 0

    while not dead:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                dead = True

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_UP:
                    y_change = -5
                elif event.key == pygame.K_DOWN:
                    y_change = 5

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                elif event.key == pygame.K_UP or pygame.K_DOWN:
                    y_change = 0

        if x - 5 > 0 and x < display_width - char_width + 5:
            x += x_change
        elif x - 5 <= 0:
            x += 1
        elif x >= display_width - char_width + 5:
            x -= 1

        if y - 5 > 0 and y < display_height - char_height + 5:
            y += y_change
        elif y - 5 <= 0:
            y += 1
        elif y >= display_height - char_height + 5:
            y -= 1

        
        gameDisplay.fill(gray)
        charImage(x, y)    

        pygame.display.update()
        clock.tick(10)


run_game()
pygame.quit()
quit()









