 
import pygame
from levels.map import *
from levels.level import *
from sprites.tiles import *
from sprites.player import *
from sprites.collision import *
from input import *

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Game 1')

#E Entities
#   Loading Background
background = pygame.Surface(screen.get_size()) #I need this? 
background.fill((100,100,100)) # --

smap = 'W'*10 
smap += 'W' + 'H' + 'O' + 'W' + 'O'*2 + 'W'*4
smap += 'd' + 'O'*5 + 'C' + 'O' + 'E' + 'W'
smap += 'd' + 'O'*3 + 'W' + 'O'*4 + 'W'
smap += 'W'*2 + 'O'*6 + 'W'*2
smap += 'W' + 'O' + 's' + 'O'*2 + 'W' + 'O'*3 + 'W'
smap += 'W'*10

level1 = Level(10,7,smap,screen)
level1.run()