try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from vector import Vector
import globals

class TallWall:
    def __init__(self, xpos):
        self.xpos = xpos
        self.border = 10
        self.colour = 'Red'
        self.width = 10
        self.normal = Vector(1,0)
        self.edge_r = xpos + self.border
        self.edge_l = xpos - self.border
        
    def draw(self, canvas):
        canvas.draw_line([self.xpos, 0],[self.xpos, globals.CANVAS_DIMS[1]], self.border, self.colour)
        
    def hit(self, player):        
        if self.edge_r >= player.offset_l() >= self.edge_l:
            return -1
        elif self.edge_l <= player.offset_r() <= self.edge_r:
            return 1
        else: return 0
    
class WideWall:
    def __init__(self, ypos):
        self.ypos = ypos
        self.border = 10
        self.colour = 'Red'
        self.width = 10
        self.normal = Vector(0,1)
        self.edge_t = ypos + self.border
        self.edge_b = ypos - self.border
        
    def draw(self, canvas):
        canvas.draw_line([0, self.ypos],[globals.CANVAS_DIMS[0], self.ypos], self.border, self.colour)
        
    def hit(self, player):        
        if self.edge_t >= player.offset_u() >= self.edge_b:
            return 1        
        elif self.edge_b <= player.offset_d() <= self.edge_t:
            return -1
        else: return 0
