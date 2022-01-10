# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 06:54:28 2022

@author: jdemt

https://www.pygame.org/news

"""

import pygame
import time

colors = [
    (0, 0, 0),
    (0, 240, 240),
    (100, 179, 179),
    (80, 34, 22),
    (80, 134, 22),
    (180, 34, 22),
    (180, 34, 122)    
    ]

# ***************************
# klasse

class Figure:
    x = 0
    y = 0
    
    def __init__(self, x_coord, y_coord):
        self.x = x_coord
        self.y = y_coord
    

class Tetris:
    height = 0
    width = 0
    field = []
    score = 0
    state = "start"
    
    def __init__(self, _height, _width): 
        self.height = _height
        self.width = _width
        self.field = []
        self.sclore = 0
        self.state = "start"
        
        for i in range(_height):
            new_line = []
            for j in range (_width):
                new_line.append(0)
            self.field.append(new_line)
        self.field[0][0] = 1
        self.field[1][1] = 2
     


# ***************************
# rest

pygame.init()
screen = pygame.display.set_mode((280, 670))
pygame.display.set_caption("Tetris")

done = False
fps = 25
clock = pygame.time.Clock()
counter = 0
zoom = 20

game = Tetris(20, 10)
pressing_down = False
pressing_left = False
pressing_right = False

BLACK= (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                game.rotate()
            if event.key == pygame.K_DOWN:
                pressing_down = True            
            if event.key == pygame.K_LEFT:
                pressing_left = True
            if event.key == pygame.K_RIGHT:
                pressing_right = True          
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
              pressing_down = False            
            if event.key == pygame.K_LEFT:
               pressing_left = False
            if event.key == pygame.K_RIGHT:
                pressing_right = False      

        if pressing_left:
            game.left()
        if pressing_down:
            game.down()
        if pressing_right:
            game.right()
        
    screen.fill(color=WHITE)       
    
    for i in range(game.height):
        for j in range (game.width):
            if (game.field[i][j]) == 0:
                color = GRAY
                just_border = 1
            else:
                color = colors[game.field[i][j]]
                just_border = 0
            pygame.draw.rect(screen, color, [30+j*zoom, 30+i*zoom, zoom, zoom], just_border)
        
        
    pygame.display.flip()
    
    
    clock.tick(fps)
  
time.sleep(5)
pygame.quit()
