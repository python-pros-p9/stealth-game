try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
    
import globals
    
class Keyboard:
    def __init__(self):
        self.right = False
        self.left = False
        self.up = False
        self.down = False

    def keyDown(self, key): # tests for keyDowns of direction keys
        if key == simplegui.KEY_MAP['w']:
            self.up = True
        if key == simplegui.KEY_MAP['a']:
            self.left = True
        if key == simplegui.KEY_MAP['s']:
            self.down = True
        if key == simplegui.KEY_MAP['d']:
            self.right = True
        if key == simplegui.KEY_MAP['space']:
            pass
        if key == simplegui.KEY_MAP['p']:
            globals.game_paused = True

    def keyUp(self, key): # tests for keyUps of direction keys
        if key == simplegui.KEY_MAP['w']:
            self.up = False
        if key == simplegui.KEY_MAP['a']:
            self.left = False
        if key == simplegui.KEY_MAP['s']:
            self.down = False
        if key == simplegui.KEY_MAP['d']:
            self.right = False
        if key == simplegui.KEY_MAP['space']:
            pass

    def draw(self, canvas):
        canvas.draw_circle(self.pos.get_p(),
                           self.radius,
                           self.border,
                           self.colour,
                           self.colour)
