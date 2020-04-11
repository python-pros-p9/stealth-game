try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
    
from vector import Vector
import globals
from spritesheet import SpriteSheet

class Enemy:
    def __init__(self, pos, vel, dims): #columns,rows
        self.sprite = SpriteSheet("https://raw.githubusercontent.com/python-pros-p9/stealth-game/master/images/coronavirus.png",(1,1),dims,10)
        self.pos = pos
        self.vel = vel
        self.dims = dims
        self.radius = 25
        self.colour = "Red"
        self.speed = 2
        self.border = 1
        self.offset = self.radius+1
        
    def bounce(self, normal):
        self.vel.reflect(normal)
        
    def update(self):
        if not globals.game_paused:
            self.pos.add(self.vel)
    
    def offset_l(self):
        return self.pos.x - (self.radius+1)
    
    def offset_r(self):
        return self.pos.x + (self.radius+1)
        
    def offset_u(self):
        return self.pos.y + (self.radius+1)
    
    def offset_d(self):
        return self.pos.y - (self.radius+1)
            
    def draw(self, canvas):
        canvas.draw_circle(self.pos.get_p(),self.radius,self.border,self.colour,self.colour)
        self.sprite.draw(canvas, self.pos.get_p())
