try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import math, time, random

import globals
from menu import Menu
from keyboard import Keyboard
from enemy import Enemy
from player import Player
from vector import Vector
from walls import WideWall
from walls import TallWall
from levels import Levels
from level1 import Level1
from spritesheet import SpriteSheet

CANVAS_DIMS = globals.CANVAS_DIMS
PLAYER_WALK_SPEED = 2
menu = Menu()

level1 = Level1()

def draw(self, canvas):
    if globals.game_start and not globals.game_end:
        Levels.update()
        Levels.draw(canvas)
        for enemy in globals.Enemies:
            enemy.draw(canvas)
            enemy.update()
        for wall in globals.Walls:
            wall.draw(canvas)
    menu.draw(canvas)
    #menu.update()
    
def mouse_handler(pos):
    global level1
    global menu
    if globals.show_help or globals.show_scores or globals.game_end or globals.game_won:
        globals.show_help = globals.game_end = globals.game_won = globals.show_scores = False
        globals.show_menu = True
    elif not globals.game_start and globals.show_menu:
        if menu.BUTTON_START_MAIN_POS[0] - menu.BUTTON_HALFSIZE[0] <= pos[0] <= menu.BUTTON_START_MAIN_POS[0] + menu.BUTTON_HALFSIZE[0] and menu.BUTTON_START_MAIN_POS[1] - menu.BUTTON_HALFSIZE[1] <= pos[1] <= menu.BUTTON_START_MAIN_POS[1] + menu.BUTTON_HALFSIZE[1]:
            level1.LoadLevel()
            globals.game_start = True

        elif menu.BUTTON_HELP_MAIN_POS[0] - menu.BUTTON_HALFSIZE[0] <= pos[0] <= menu.BUTTON_HELP_MAIN_POS[0] + menu.BUTTON_HALFSIZE[0] and menu.BUTTON_HELP_MAIN_POS[1] - menu.BUTTON_HALFSIZE[1] <= pos[1] <= menu.BUTTON_HELP_MAIN_POS[1] + menu.BUTTON_HALFSIZE[1]:
            globals.show_help = True
            globals.show_menu = False
        elif menu.BUTTON_SCORES_POS[0] - menu.BUTTON_HALFSIZE[0] <= pos[0] <= menu.BUTTON_SCORES_POS[0] + menu.BUTTON_HALFSIZE[0] and menu.BUTTON_SCORES_POS[1] - menu.BUTTON_HALFSIZE[1] <= pos[1] <= menu.BUTTON_SCORES_POS[1] + menu.BUTTON_HALFSIZE[1]:
            globals.show_scores = True
            globals.show_menu = False
    elif globals.game_start and globals.game_paused:
        if menu.BUTTON_RESUME_POS[0] - menu.BUTTON_HALFSIZE[0] <= pos[0] <= menu.BUTTON_RESUME_POS[0] + menu.BUTTON_HALFSIZE[0]:
            if menu.BUTTON_RESUME_POS[1] - menu.BUTTON_HALFSIZE[1] <= pos[1] <= menu.BUTTON_RESUME_POS[1] + menu.BUTTON_HALFSIZE[1]:
                globals.game_paused = False
            elif menu.BUTTON_HELP_PAUSE_POS[1] - menu.BUTTON_HALFSIZE[1] <= pos[1] <= menu.BUTTON_HELP_PAUSE_POS[1] + menu.BUTTON_HALFSIZE[1]:
                globals.show_help = True
                globals.show_menu = False
            elif menu.BUTTON_MAINMENU_PAUSE_POS[1] - menu.BUTTON_HALFSIZE[1] <= pos[1] <= menu.BUTTON_MAINMENU_PAUSE_POS[1] + menu.BUTTON_HALFSIZE[1]:
                globals.game_end = True
                globals.game_paused = False
                globals.game_start = False
    elif globals.game_end:
        if menu.BUTTON_MAINMENU_END_POS[1] - menu.BUTTON_HALFSIZE[1] <= pos[1] <= menu.BUTTON_MAINMENU_END_POS[1] + menu.BUTTON_HALFSIZE[1]:
            globals.game_start = False
    elif globals.game_won:
        if menu.BUTTON_MAINMENU_WIN_POS[1] - menu.BUTTON_HALFSIZE[1] <= pos[1] <= menu.BUTTON_MAINMENU_WIN_POS[1] + menu.BUTTON_HALFSIZE[1]:
            print("this isn't implemented yet") 

frame = simplegui.create_frame("COVID-19 Simulator 2020", CANVAS_DIMS[0], CANVAS_DIMS[1])
frame.set_canvas_background('White')
frame.set_draw_handler(draw)
frame.set_keydown_handler(Levels.kbd.keyDown)
frame.set_keyup_handler(Levels.kbd.keyUp)
frame.set_mouseclick_handler(mouse_handler)
frame.start()
