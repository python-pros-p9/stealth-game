try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from vector import Vector

class Interaction:
    def __init__(self, keyboard, list_walls, list_entities, player,enemy):
        self.player = player
        self.enemy = enemy
        self.keyboard = keyboard
        self.list_walls = list_walls
        self.list_entities = list_entities
        
    def update(self): # changes player's velocity and spriteset based on keyboard events
        if keyboard.right & keyboard.left:
            self.player.vel.x = 0
        elif keyboard.right: 
            self.player.vel.x = min(self.player.vel.x+0.01,player.speed)
            self.player.sprite_current = self.player.sprite_right
        elif keyboard.left:            
            self.player.vel.x = max(self.player.vel.x-0.01,-player.speed)
            self.player.sprite_current = self.player.sprite_left
        if keyboard.up & keyboard.down:
            self.player.vel.x = 0
        if keyboard.up:            
            self.player.vel.y = max(self.player.vel.y-0.01,-player.speed)
            self.player.sprite_current = self.player.sprite_up
        elif keyboard.down:            
            self.player.vel.y = min(self.player.vel.y+0.01,player.speed)
            self.player.sprite_current = self.player.sprite_down
        
        if keyboard.right & keyboard.left:
            self.player.vel.x = 0
        elif keyboard.right: 
            self.player.vel.x = player.speed
            self.player.sprite_current = self.player.sprite_right
        elif keyboard.left:            
            self.player.vel.x = -player.speed
            self.player.sprite_current = self.player.sprite_left
        if keyboard.up & keyboard.down:
            self.player.vel.x = 0
        if keyboard.up:            
            self.player.vel.y = -player.speed
            self.player.sprite_current = self.player.sprite_up
        elif keyboard.down:            
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
