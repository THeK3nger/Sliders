"""
map.py
This module contains all class and method for maps operation like loading.

Davide Aversa
2011
"""

from sprites.tiles import *
from sprites.player import *

class Map(object) :
    """
    This class represents a game map. Contains all tiles position and event.
    """
    
    def __init__(self,width,height,string_map) :
        self.height = height
        self.width = width
        self.tiles = []
        self.walls = pygame.sprite.Group()
        self.spike = pygame.sprite.Group()
        self.crash = pygame.sprite.Group()
        self.exit = pygame.sprite.GroupSingle()
        self.player = pygame.sprite.GroupSingle()
        if self._check_string(string_map) :
            c = 0
            for char in string_map :
                cx = (c % self.width) + 1
                cy = (c / self.width) + 1
                c += 1
                if char == 'W' :
                    self.walls.add(Wall(cx,cy))
                elif char == 'E' :
                    self.exit.add(Exit(cx,cy))
                elif char == 'H' :
                    self.player.add(Player(cx, cy))
                elif char == 's' :
                    self.spike.add(Spike(cx,cy,'U'))
                elif char == 'S' :
                    self.spike.add(Spike(cx,cy,'D'))
                elif char == 'D' :
                    self.spike.add(Spike(cx,cy,'L'))
                elif char == 'd' :
                    self.spike.add(Spike(cx,cy,'R'))
                elif char == 'C' :
                    self.crash.add(Crash(cx,cy))
        else :
            print "WTF! OMG!"
                    
    def update(self) :
        self.walls.update()
        self.spike.update()
        self.crash.update()
        self.player.update()
        self.exit.update()
    
    def draw(self,surface) :
        self.walls.draw(surface)
        self.spike.draw(surface)
        self.crash.draw(surface)
        self.exit.draw(surface)
        self.player.draw(surface)
        
    def clear(self,surface,back) :
        self.player.clear(surface,back)
        self.crash.clear(surface,back)
    
    def get_map_elements(self) :
        return [self.walls, self.exit, self.spike, self.crash]
    
    def _check_string(self,string_map) :
        if len(string_map) % self.height != 0 :
            return False
        if len(string_map) / self.height != self.width :
            return False
        return True
    
