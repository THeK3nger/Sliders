"""
player.py
Modules for player tiles.

Devide Aversa
2011
"""

import pygame

class Player(pygame.sprite.Sprite) :
    """
    Player Sprite
    """
    
    def __init__(self,cell_x,cell_y) :
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('image/player.png')
        self.image.convert()
        self.rect = self.image.get_rect()
        #self.rect = self.rect.inflate(1,1)
        self.cell_x = cell_x
        self.cell_y = cell_y
        self.tlen = 27
        self.fix_rect()
        self.final_cell_x = cell_x
        self.final_cell_y = cell_y
        #CONSTANT
        self.STOP = 0
        self.MOVE = 1
        self.direction = (0,0)
        
        self.state = self.STOP
        
    def fix_rect(self) :
        """
        Convert X,Y in grid-space in X,Y in screen-space.
        """
        x = self.tlen * (self.cell_x - 0.5) - 0.5
        y = self.tlen * (self.cell_y - 0.5) - 0.5
        self.rect.center = (x,y)
        
    def update(self) :
        if self.state == self.MOVE :
            dx,dy = self.direction
            dx *= 7
            dy *= 7
            self.rect.centerx += dx
            self.rect.centery += dy 
            
            