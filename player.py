try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from vector import Vector
from spritesheet import SpriteSheet
from keyboard import Keyboard
#from healthSpriteSheet import HealthSpriteSheet
#from health import Health
#from fireball import Fireball
import globals

class Player:
    def __init__(self): #columns,rows
        self.sprite_up = SpriteSheet("https://raw.githubusercontent.com/python-pros-p9/stealth-game/master/images/doc_up.png",(9,1),(60,60),10)
        self.sprite_right = SpriteSheet("https://raw.githubusercontent.com/python-pros-p9/stealth-game/master/images/doc_right.png",(9,1),(60,60),10)
        self.sprite_down = SpriteSheet("https://raw.githubusercontent.com/python-pros-p9/stealth-game/master/images/doc_down.png",(9,1),(60,60),10)
        self.sprite_left = SpriteSheet("https://raw.githubusercontent.com/python-pros-p9/stealth-game/master/images/doc_left.png",(9,1),(60,60),10)
        self.sprite_current = self.sprite_down
        self.pos = globals.player_pos
        self.vel = Vector(0,0)
        self.radius = max(self.sprite_current.frameHeight, self.sprite_current.frameWidth,2)/2
        self.colour = "Blue"
        self.speed = 2
        self.border = 1
        self.offset = self.radius+1
        
    def bounce(self, normal):
        self.vel.reflect(normal)
        
    def update(self):
        #if 0.1 >= self.vel >= -0.1 and 0.1 >= self.vel.y >= -0.1:
        #    self.sprite_current.animated = False
        #else: 
        #    self.sprite_current.animated = True 

        if not globals.game_paused:
            self.pos.add(self.vel)
            self.vel.multiply(0.80)
            self.sprite_current.update()
        
    
    def offset_l(self):
        return self.pos.x - (self.radius+1)
    
    def offset_r(self):
        return self.pos.x + (self.radius+1)
        
    def offset_u(self):
        return self.pos.y + (self.radius+1)
    
    def offset_d(self):
        return self.pos.y - (self.radius+1)
    
    def stop(self, normal,s):
        if normal.x == 0:
            if (s == -1 and self.vel.y == -2) or (s == 1 and self.vel.y == 2):
                self.vel.y = 0                
        else:
            if (s == -1 and self.vel.x == -2) or (s == 1 and self.vel.x == 2):
                self.vel.x = 0
            
    def draw(self, canvas):
        canvas.draw_circle(self.pos.get_p(),self.radius,self.border,self.colour,self.colour)
        self.sprite_current.draw(canvas, self.pos.get_p())