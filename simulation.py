# Chandler Supple, 4/28/2018
# A simulation of Newton's Cradle in a vacuum environment, devoid of weight and friction.

import sys
import math
import pygame
import random
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((1000,500))
pygame.display.set_caption("Netwon's Cradle Simulation (Vacuum, Weighless, Controlled)")

clock = pygame.time.Clock()

i = 0
j_ = 0
clicked = 0
stop = 0

white = (255,255,255)
black = (0,0,0)
light_grey = (245,245,245)
grey = (230,230,230)
grey_other = (120,120,120)
brown = (152, 128, 99)
dark_brown = (122, 100, 71)
light_brown = (172, 148, 119)
light_blue = (180,180,255)
random_color = ((random.randint(50,230)), (random.randint(50,230)), (random.randint(50,230)))

font = pygame.font.SysFont("corbel", 35)
title = font.render("Newton's Cradle", 3, (dark_brown))

def base():
    pygame.draw.rect(screen, brown, (0, 400, 1000, 100), 0)
    pygame.draw.rect(screen, dark_brown, (0, 380, 1000, 65), 0)
    pygame.draw.rect(screen, light_brown, ((0), 450, 1000, 50), 0)

def frame():
    pygame.draw.rect(screen, grey_other, (100, 100, 700, 13), 0)
    pygame.draw.rect(screen, grey_other, (100, 100, 13, 310), 0)
    pygame.draw.rect(screen, grey_other, (800, 100, 13, 310), 0)
    pygame.draw.rect(screen, grey_other, (75, 410, 60, 13), 0)
    pygame.draw.rect(screen, grey_other, (775, 410, 60, 13), 0)
    for i in range (0,6):
        pygame.draw.circle(screen, white, ((i*40)+340+(i),120), 12, 2)    

x_ = 340
y_ = 320 
    
def first_marble(x_, y_):
    if (x_>340):
        x_ = 340
    if (y_>320):
        y_ = 320
    pygame.draw.line(screen, light_grey, (340,130), (x_,y_), 2)
    pygame.draw.circle(screen, random_color, (x_, y_), 20, 0)        
        
def marbles():
    for i in range (1,5):  
        pygame.draw.rect(screen, light_grey, ((i*40)+339+(i),130, 2, 180), 0)
        pygame.draw.circle(screen, random_color, ((i*40)+340+(i),320), 20, 0)
        
def end_marble(x, y):
    if (x<544):
        x = 544
    if (y>322):
        y = 320
    pygame.draw.line(screen, light_grey, (544,130), (x,y), 2)
    pygame.draw.circle(screen, random_color, (x, y), 20, 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_SPACE]: clicked = 1
    
    if (clicked == 0):        
        x, y__ = pygame.mouse.get_pos()
        y = int(round(math.sqrt(300000-(((x-436)**2)/2))-216.5,0))
        x_ = 340
        y_ = 320
        x_ch = x
        y_ch = y
    
    if (clicked == 1):
        diff = x_ch - 544
        if (i <= diff):
            x = x_ch - (i)
            y = int(round(math.sqrt(300000-(((x-436)**2)/2))-216.5,0))
            i = i + 25
            if pressed[pygame.K_s]: clicked = 0
        if (i >= diff):
            x = 544
            y = 320
            i = 0
            clicked = 2
            
    if (clicked == 2):
        diff = x_ch - 544
        if (i <= diff):
            x_ = 340 - (i)
            y_ = int(round(math.sqrt(300000-(((x_-436)**2)/2))-216.5,0))
            i = i + 25
            if pressed[pygame.K_s]: clicked = 0
        if (i >= diff):
            i = 0
            clicked = 3
            
    if (clicked == 3):
        diff = x_ch - 544
        if (i <= diff):
            x_ = (340-diff) + (i)
            y_ = int(round(math.sqrt(300000-(((x_-436)**2)/2))-216.5,0))
            i = i + 25
            if pressed[pygame.K_s]: clicked = 0
        if (i >= diff):
            x_ = 340
            y_ = 320
            i = 0
            clicked = 4
            
    if (clicked == 4):
        diff = x_ch - 544
        if (i <= diff):
            x = 544 + (i)
            y = int(round(math.sqrt(300000-(((x-436)**2)/2))-216.5,0))
            i = i + 25
            if pressed[pygame.K_s]: clicked = 0
        if (i >= diff):
            i = 0
            clicked = 1

#    print('x: %s' %(x))
#    print('y: %s' %(y))
        
    screen.fill(grey)
    base()
    frame()
    first_marble(x_, y_)
    marbles()
    end_marble(x, y)
    
    screen.blit(title, (100,50))
        
    pygame.display.flip()
    clock.tick(60)
