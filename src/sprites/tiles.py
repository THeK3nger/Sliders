"""
tiles.py
Sprite Class for every tiles on the map.

Davide Aversa
2011
"""

import pygame

TILE_SIZE = 27

class Tile(pygame.sprite.Sprite) :
    """
    Standard Tile class. It's a base for all other tiles in the map.
    """
    
    def __init__ (self,cell_x,cell_y) :
        """
        Constructor.
        
        ARGS:
            * cell_x (integer) : Cell X position in map grid.
            * cell_y (integer) : Cell Y position in map grid.
        """
        pygame.sprite.Sprite.__init__(self)
        self.cell_x = cell_x
        self.cell_y = cell_y
        self.tlen = TILE_SIZE # Tiles size in pixel.
        
    def fix_rect(self) :
        """
        Convert X,Y in grid-space in X,Y in screen-space.
        """
        x = self.tlen * (self.cell_x - 0.5) - 0.5
        y = self.tlen * (self.cell_y - 0.5) - 0.5
        self.rect.center = (x,y)
        
class Wall(Tile) :
    """
    This tile represents a fixed Wall. A wall block player movement
    and nothing else. 
    """
    
    def __init__(self,cell_x,cell_y) :
        Tile.__init__(self,cell_x,cell_y)
        self.image = pygame.image.load('image/wall.png')
        self.image.convert()
        self.rect = self.image.get_rect()
        self.fix_rect()
        
    def update(self) :
        pass # Nothing to do.
        
class Spike(Tile) :
    """
    A "Spike" kill the player when he come in direction of spike
    """
    
    def __init__(self,cell_x,cell_y,side) :
        Tile.__init__(self,cell_x,cell_y)
        self.side = side
        self.image = pygame.image.load('image/spike.png')
        if side == 'U' :
            pass
            #pygame.transform.rotate(self.image,
        elif side == 'D' :
            self.image = pygame.transform.rotate(self.image,180)
        elif side == 'L' :
            self.image = pygame.transform.rotate(self.image,90)
        else :
            self.image = pygame.transform.rotate(self.image,-90)
        self.image.convert()
        self.rect = self.image.get_rect()
        self.fix_rect()
        
class Crash(Tile) :
    """
    Crash-Block: block disappear if touched.
    """
    
    def __init__(self,cell_x,cell_y) :
        Tile.__init__(self,cell_x,cell_y)
        self.image = pygame.image.load('image/crash.png')
        self.image.convert()
        self.rect = self.image.get_rect()
        self.fix_rect()

class Exit(Tile) :
    """
    Exit zone.
    """
    
    def __init__(self,cell_x,cell_y) :
        Tile.__init__(self,cell_x,cell_y)
        self.image = pygame.image.load('image/exit.png')
        self.image.convert()
        self.rect = self.image.get_rect()
        self.fix_rect()
        
    def update(self) :
        pass
