try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
    
import globals

CANVAS_DIMS = globals.CANVAS_DIMS

class Menu:
    def __init__(self):
        self.game_start = False
        self.game_end = False
        self.paused = False
        self.won = False
        self.show_menu = True
        self.show_help = False
        self.show_scores = False
        self.TITLETEXT = simplegui.load_image(
            "https://raw.githubusercontent.com/python-pros-p9/stealth-game/master/menutext.png")
        self.TITLETEXT_CENTRE = (self.TITLETEXT.get_width() / 2, self.TITLETEXT.get_height() / 2)
        self.TITLETEXT_DIMS = (self.TITLETEXT.get_width(), self.TITLETEXT.get_height())
        self.TITLETEXT_SIZE = (CANVAS_DIMS[0], CANVAS_DIMS[1])
        self.TITLETEXT_POS = (CANVAS_DIMS[0] / 2, CANVAS_DIMS[1] / 2)  # where to draw image
        
        self.BUTTON = simplegui.load_image(
            "https://raw.githubusercontent.com/python-pros-p9/stealth-game/master/start_button.png")
        self.BUTTON_CENTRE = (self.BUTTON.get_width() / 2, self.BUTTON.get_height() / 2)
        self.BUTTON_DIMS = (self.BUTTON.get_width(), self.BUTTON.get_height())
        self.BUTTON_SIZE = (240, 80)
        self.BUTTON_HALFSIZE =  (self.BUTTON_SIZE[0]/2,self.BUTTON_SIZE[1]/2)
        self.BUTTON_MAIN_POS = (CANVAS_DIMS[0] / 3, 400)
        
        self.BUTTON_HELP = simplegui.load_image(
            "https://raw.githubusercontent.com/python-pros-p9/stealth-game/master/help_button.png")
        self.BUTTON_HELP_MAIN_POS = (CANVAS_DIMS[0] * (2/3), 400)
        self.BUTTON_HELP_PAUSE_POS = (CANVAS_DIMS[0]/2,(CANVAS_DIMS[1]/5)*3)  
        
        self.BUTTON_SCORES = simplegui.load_image(
            "https://raw.githubusercontent.com/python-pros-p9/stealth-game/master/score_button.png")
        self.BUTTON_SCORES_POS = (CANVAS_DIMS[0] / 2, 500)
        
        self.BUTTON_MAINMENU = simplegui.load_image(
            "https://raw.githubusercontent.com/python-pros-p9/stealth-game/master/menu_button.png")
        self.BUTTON_MAINMENU_END_POS = (CANVAS_DIMS[0] / 2, 450)
        self.BUTTON_MAINMENU_WIN_POS = (CANVAS_DIMS[0] / 2, 500)
        self.BUTTON_MAINMENU_PAUSE_POS = (CANVAS_DIMS[0]/2,(CANVAS_DIMS[1]/5)*4)  
        
        self.BUTTON_RESUME = simplegui.load_image(
            "https://raw.githubusercontent.com/python-pros-p9/stealth-game/master/resume_button.png")
        self.BUTTON_RESUME_POS = (CANVAS_DIMS[0]/2,(CANVAS_DIMS[1]/5)*2)       
        
        self.END = simplegui.load_image(
            "https://raw.githubusercontent.com/python-pros-p9/stealth-game/master/gameover.png")
        
        self.WIN = simplegui.load_image(
            "https://raw.githubusercontent.com/python-pros-p9/stealth-game/master/winscreen.png")
        
    def draw(self, canvas):
        

        if not self.game_start and self.show_menu:
            canvas.draw_image(self.TITLETEXT, self.TITLETEXT_CENTRE, self.TITLETEXT_DIMS, self.TITLETEXT_POS, self.TITLETEXT_SIZE)
            canvas.draw_image(self.BUTTON, self.BUTTON_CENTRE, self.BUTTON_DIMS, self.BUTTON_MAIN_POS, self.BUTTON_SIZE)
            canvas.draw_image(self.BUTTON_HELP, self.BUTTON_CENTRE, self.BUTTON_DIMS, self.BUTTON_HELP_MAIN_POS, self.BUTTON_SIZE)
            canvas.draw_image(self.BUTTON_SCORES, self.BUTTON_CENTRE, self.BUTTON_DIMS, self.BUTTON_SCORES_POS, self.BUTTON_SIZE)
            
        if self.game_end:
            canvas.draw_image(self.END, self.TITLETEXT_CENTRE, self.TITLETEXT_DIMS, self.TITLETEXT_POS, self.TITLETEXT_SIZE)
            canvas.draw_text("Score: ", (CANVAS_DIMS[0]/2, 350), 50, 'Purple', 'sans-serif')
            #canvas.draw_text("Score: " + str(Scores.score), (CANVAS_DIMS[0]/2, 350), 50, 'rgb(102,2,60)', 'sans-serif')
            canvas.draw_image(self.BUTTON_MAINMENU, self.BUTTON_CENTRE, self.BUTTON_DIMS, self.BUTTON_MAINMENU_END_POS, self.BUTTON_SIZE)
            
        if self.won:
            canvas.draw_image(self.WIN, self.TITLETEXT_CENTRE, self.TITLETEXT_DIMS, self.TITLETEXT_POS, self.TITLETEXT_SIZE)
            canvas.draw_text("Score: ", (CANVAS_DIMS[0]/2+100, 420), 50, 'rgb(102,2,60)', 'sans-serif')
            #canvas.draw_text("Score: " + str(Scores.score), (CANVAS_DIMS[0]/2+100, 420), 50, rgb(102,2,60))
            canvas.draw_image(self.BUTTON_MAINMENU, self.BUTTON_CENTRE, self.BUTTON_DIMS, self.BUTTON_MAINMENU_WIN_POS, self.BUTTON_SIZE)
            
        if self.paused:
            canvas.draw_text("Game Paused", [CANVAS_DIMS[0]/2-(383/2),(CANVAS_DIMS[1]/5)], 60, "Purple", 'sans-serif')
            canvas.draw_image(self.BUTTON_RESUME, self.BUTTON_CENTRE, self.BUTTON_DIMS, self.BUTTON_RESUME_POS, self.BUTTON_SIZE)
            canvas.draw_image(self.BUTTON_HELP, self.BUTTON_CENTRE, self.BUTTON_DIMS, self.BUTTON_HELP_PAUSE_POS, self.BUTTON_SIZE)
            canvas.draw_image(self.BUTTON_MAINMENU, self.BUTTON_CENTRE, self.BUTTON_DIMS, self.BUTTON_MAINMENU_PAUSE_POS, self.BUTTON_SIZE)
            
        if self.show_help:
            canvas.draw_line((0, CANVAS_DIMS[1]/2), (CANVAS_DIMS[0], CANVAS_DIMS[1]/2), CANVAS_DIMS[1], 'Lime')
            canvas.draw_text("Help menu", [CANVAS_DIMS[0]/20,(CANVAS_DIMS[1]/8)], 60, "Purple")
            canvas.draw_text("1. Use WASD keys to move", [CANVAS_DIMS[0]/20,(CANVAS_DIMS[1]/8)*2], 50, "Purple", 'sans-serif')
            canvas.draw_text("2. Avoid the guards' (blue circles) field of view", [CANVAS_DIMS[0]/20,(CANVAS_DIMS[1]/8)*3], 50, "Purple", 'sans-serif')
            canvas.draw_text("3. Press 'P' to Pause.", [CANVAS_DIMS[0]/20,(CANVAS_DIMS[1]/8)*4], 50, "Purple", 'sans-serif')
            canvas.draw_text("4. ", [CANVAS_DIMS[0]/20,(CANVAS_DIMS[1]/8)*5], 50, "Purple", 'sans-serif')
            canvas.draw_text("5. ", [CANVAS_DIMS[0]/20,(CANVAS_DIMS[1]/8)*6], 50, "Purple", 'sans-serif')
            canvas.draw_text("Click anywhere to return to menu", [CANVAS_DIMS[0]/20,(CANVAS_DIMS[1]/8)*7], 50, "Purple", 'sans-serif')
            
        if self.show_scores:
            canvas.draw_text("Scores", [CANVAS_DIMS[0]/20,(CANVAS_DIMS[1]/8)], 60, "Purple")
            canvas.draw_text("This feature not yet implemented.", [CANVAS_DIMS[0]/20,(CANVAS_DIMS[1]/8)*2], 50, "Purple", 'sans-serif')
            canvas.draw_text("", [CANVAS_DIMS[0]/20,(CANVAS_DIMS[1]/8)*3], 50, "Purple", 'sans-serif')
            canvas.draw_text("", [CANVAS_DIMS[0]/20,(CANVAS_DIMS[1]/8)*4], 50, "Purple", 'sans-serif')
            canvas.draw_text("", [CANVAS_DIMS[0]/20,(CANVAS_DIMS[1]/8)*5], 50, "Purple", 'sans-serif')
            canvas.draw_text("", [CANVAS_DIMS[0]/20,(CANVAS_DIMS[1]/8)*6], 50, "Purple", 'sans-serif')
            canvas.draw_text("Click anywhere to return to menu", [CANVAS_DIMS[0]/20,(CANVAS_DIMS[1]/8)*7], 50, "Purple", 'sans-serif')
            
    #def update(self):
    #    if player.health <= 0:
     #       self.game_end = True
      #      self.game_start = True
            
