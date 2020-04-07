try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
    
from vector import Vector
import globals

CANVAS_DIMS = globals.CANVAS_DIMS

class Enemy:
    def __init__(self): #columns,rows
        
        self.pos = Vector(CANVAS_DIMS[0]/2, CANVAS_DIMS[1]/2)
        self.vel = Vector(2,2)
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
