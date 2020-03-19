try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from vector import Vector
from spritesheet import SpriteSheet

from healthSpriteSheet import HealthSpriteSheet
from health import Health
from fireball import Fireball
import globals

CANVAS_DIMS = globals.CANVAS_DIMS

class Player:
    def __init__(self): #columns,rows
        self.sprite_up = SpriteSheet("https://raw.githubusercontent.com/python-pros-p9/stealth-game/master/doc_up.png",(9,1),(60,60),10)
        self.sprite_right = SpriteSheet("https://raw.githubusercontent.com/python-pros-p9/stealth-game/master/doc_right.png",(9,1),(60,60),10)
        self.sprite_down = SpriteSheet("https://raw.githubusercontent.com/python-pros-p9/stealth-game/master/doc_down.png",(9,1),(60,60),10)
        self.sprite_left = SpriteSheet("https://raw.githubusercontent.com/python-pros-p9/stealth-game/master/doc_left.png",(9,1),(60,60),10)
        self.sprite_current = self.sprite_down
        self.pos = Vector(CANVAS_DIMS[0]/4, CANVAS_DIMS[1]/4)
        self.vel = Vector(0,0)
        self.radius = max(self.sprite_current.frameHeight, self.sprite_current.frameWidth)/2
        self.colour = "Blue"
        self.speed = 2
        #self.sprite = SpriteSheet("https://raw.githubusercontent.com/python-pros-p9/stealth-game/master/coronavirus.png",(1,1),(60,60))
        self.border = 1
        self.offset = self.radius+1
        
    def bounce(self, normal):
        self.vel.reflect(normal)
        
    def update(self):
        if not menu.paused:
            self.pos.add(self.vel)
            self.vel.multiply(0.99)
    
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
        