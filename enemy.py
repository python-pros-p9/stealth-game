try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from vector import Vector

class Enemy:
    def __init__(self, pos, vel, dims):
        self.pos = Vector(pos[0],pos[1])
        self.vel = Vector(0,0)
        self.dims = dims
        self.colour = "Red"
        #self.sprite = SpriteSheet("https://raw.githubusercontent.com/python-pros-p9/stealth-game/master/whitebloodcell.png",(1,1),(60,60))
        self.border = 1
         #self.viewAng = 70 
        self.speed = 20
         #self.maxSpin = 10
        
    def update(self):
        if not menu.paused:
            self.pos.add(self.vel.multiply(self.speed))
            self.vel.multiply(0.7)
        
    def draw(self, canvas):
        canvas.draw_circle(self.pos.get_p(),max(self.dims[0],self.dims[1]),self.border,self.colour,self.colour)
        
    def target(self, pos):
        self.vel = Vector(pos.get_p()[0] - self.pos.get_p()[0], pos.get_p()[1] - self.pos.get_p()[1]).normalize()
        
#class WhiteCell(Enemy):
#    def __init__(self,pos):
#        super().__init__("https://raw.githubusercontent.com/python-pros-p9/stealth-game/master/whitebloodcell.png",(60,60,) pos, 1)
#        self.radius = 20
#        self.border = 1
#        #self.health = Health()
#        self.currentlyAttacking = True
#        self.attackCount = 0
    
class RedCell:
    pass