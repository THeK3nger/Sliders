"""
input.py
Module for Mouse/Keyboard gesture.

Davide Aversa
2011
"""

import pygame

class KeyboardInput(object) :
    """
    Manage Keyboard Input.
    """
    
    def __init__(self, player, data) :
        """
        ARGS:
            * player (Player) : Pointer to Player's Sprite
            * data (tuple) : Data
        """
        self.player = player
        self.data = data
        
    def key_event(self,keys) :
        """
        ARGS:
            * keys : pygame keys list
        """
        p = self.player
        if p.state == p.STOP :
            if keys[pygame.K_DOWN] :
                p.direction = (0,1)
                p.state = p.MOVE
            if keys[pygame.K_RIGHT] :
                p.direction = (1,0)
                p.state = p.MOVE
            if keys[pygame.K_LEFT] :
                p.direction = (-1,0)
                p.state = p.MOVE
            if keys[pygame.K_UP] :
                p.direction = (0,-1)
                p.state = p.MOVE
