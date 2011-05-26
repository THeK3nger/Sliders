"""
level.py
Game Level

Davide Aversa
2011
"""

import pygame
from levels.map import *
from levels.level import *
from sprites.tiles import *
from sprites.player import *
from sprites.collision import *
from input import *
from sprites.tiles import TILE_SIZE

class Level(object) :
    """
    Game Level
    """
    
    def __init__(self, width, height, string_map, screen) :
        x = width*TILE_SIZE
        y = height*TILE_SIZE
        self.levelsurf = pygame.surface.Surface((x,y))
        self.map = Map(width,height,string_map)
        self.background = pygame.Surface(screen.get_size())
        self.background.fill((100,100,100))
        self.levelsurf.blit(self.background, (0,0))
        self.screen = screen
        
    def run(self) :
        p = self.map.player.sprite
        slist = self.map.get_map_elements()
        
        going = True
        clock = pygame.time.Clock()
        
        keycontrol = KeyboardInput(p,(self.levelsurf,slist[0]))
        collision = CollisionHandler(p,slist)
        
        while going :
            clock.tick(30)
            for event in pygame.event.get() :
                if event.type == pygame.QUIT :
                    going = False
                if event.type == pygame.KEYDOWN :
                    keys = pygame.key.get_pressed()
                    keycontrol.key_event(keys)
                    
            self.map.update() # <- BEFORE COLLISION

            collision.collision_check()
                        
            self.map.clear(self.levelsurf,self.background)
            self.map.draw(self.levelsurf)
            
            self.screen.blit(self.levelsurf,(50,50))
            
            pygame.display.flip()