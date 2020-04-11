# currently obselete as class Interaction is in main
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import globals
import levels
from vector import Vector
from player import Player
from menu import Menu

class Interaction:
    def __init__(self, keyboard, list_walls, list_entities, player,enemy):
        self.player = player
        self.enemy = enemy
        self.list_walls = list_walls
        self.list_entities = list_entities
        
    def update(self): # changes player's velocity and spriteset based on keyboard events
        kbd = levels.kbd
        player = levels.player
        if kbd.right & kbd.left:
            self.player.vel.x = 0
        elif kbd.right: 
            self.player.vel.x = min(self.player.vel.x+0.01,player.speed)
            self.player.sprite_current = self.player.sprite_right
        elif kbd.left:            
            self.player.vel.x = max(self.player.vel.x-0.01,-player.speed)
            self.player.sprite_current = self.player.sprite_left
        if kbd.up & kbd.down:
            self.player.vel.x = 0
        if kbd.up:            
            self.player.vel.y = max(self.player.vel.y-0.01,-player.speed)
            self.player.sprite_current = self.player.sprite_up
        elif kbd.down:            
            self.player.vel.y = min(self.player.vel.y+0.01,player.speed)
            self.player.sprite_current = self.player.sprite_down
        
        if kbd.right & kbd.left:
            self.player.vel.x = 0
        elif kbd.right: 
            self.player.vel.x = player.speed
            self.player.sprite_current = self.player.sprite_right
        elif kbd.left:            
            self.player.vel.x = -player.speed
            self.player.sprite_current = self.player.sprite_left
        if kbd.up & kbd.down:
            self.player.vel.x = 0
        if kbd.up:            
            self.player.vel.y = -player.speed
            self.player.sprite_current = self.player.sprite_up
        elif kbd.down:            
            self.player.vel.y = player.speed
            self.player.sprite_current = self.player.sprite_down

        for wall in globals.Walls:
            s = wall.hit(player)
            if s!= 0:
                self.player.bounce(wall.normal)
                
        for wall in globals.Walls:
            for enemy in globals.Enemies:
                s = wall.hit(enemy)
                if s!= 0:
                    self.enemy.bounce(wall.normal)
      
        self.player.update()
        self.enemy.update()
