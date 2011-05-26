"""
collision.py
Collision Detection and Handler

Davide Aversa
2011
""" 

import pygame

class CollisionHandler(object) :
    """
    Collisions Handler
    """
    
    def __init__(self,player,grouplist) :
        """
        ARGS:
            * player (Player) Player Sprite
            * grouplist (list) List of sprites group.
        """
        self.player = player
        self.grouplist = grouplist
        
    def collision_check(self) :
        # EXIT COLLISION
        if self.player.rect.colliderect(self.grouplist[1].sprite.rect) :
            print "WIN"
            
        # WALL COLLISION
        walls = self.grouplist[0]
        collided = pygame.sprite.spritecollide(self.player,walls,False)
        if len(collided) != 0 :
            dx,dy = self.player.direction
            self.player.direction = (0,0)
            self.player.state = self.player.STOP            
            if dx == 1 :
                self.player.rect.right = collided[0].rect.left
            if dx == -1 :
                self.player.rect.left = collided[0].rect.right
            if dy == 1 :
                self.player.rect.bottom = collided[0].rect.top
            if dy == -1 :
                self.player.rect.top = collided[0].rect.bottom
        
        # SPIKE COLLISION
        spikes = self.grouplist[2]
        collided = pygame.sprite.spritecollide(self.player,spikes,False)
        if len(collided) != 0 :
            dx,dy = self.player.direction
            self.player.direction = (0,0)
            self.player.state = self.player.STOP
            if dx == 1 :
                self.player.rect.right = collided[0].rect.left
                if collided[0].side == 'L' :
                    print 'KILL'
            if dx == -1 :
                self.player.rect.left = collided[0].rect.right
                if collided[0].side == 'R' :
                    print 'KILL'
            if dy == 1 :
                self.player.rect.bottom = collided[0].rect.top
                if collided[0].side == 'U' :
                    print 'KILL'
            if dy == -1 :
                self.player.rect.top = collided[0].rect.bottom
                if collided[0].side == 'D' :
                    print 'KILL'
                    
        # CRASH COLLIDE
        crash = self.grouplist[3]
        collided = pygame.sprite.spritecollide(self.player,crash,True)
        if len(collided) != 0 :
            dx,dy = self.player.direction
            self.player.direction = (0,0)
            self.player.state = self.player.STOP
            collided[0].remove(crash)     
            if dx == 1 :
                self.player.rect.right = collided[0].rect.left
            if dx == -1 :
                self.player.rect.left = collided[0].rect.right
            if dy == 1 :
                self.player.rect.bottom = collided[0].rect.top
            if dy == -1 :
                self.player.rect.top = collided[0].rect.bottom