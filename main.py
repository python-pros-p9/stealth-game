try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import math, time, random

import globals

from vector import Vector
from interactions import Interaction
from walls import *
from levels import *
from menu import Menu
from spritesheet import SpriteSheet

#CONSTANTS - use all caps, separated by underscores
CANVAS_DIMS = globals.CANVAS_DIMS
PLAYER_WALK_SPEED = 2
PLAYER_START_POS = [CANVAS_DIMS[0]/4, CANVAS_DIMS[1]/4]
menu = Menu()

#VARIABLES - use lowercase words, separated by underscores
level = 0
#Controls
    # WASD (up, left, down, right) to dictate movement direction
    
def mouse_handler(pos):
    global menu
    if menu.show_help or menu.show_scores or menu.game_end or menu.won:
        menu.show_help = menu.game_end = menu.won = menu.show_scores = False
        menu.show_menu = True
    elif not menu.game_start and menu.show_menu:
        if menu.BUTTON_MAIN_POS[0] - menu.BUTTON_HALFSIZE[0] <= pos[0] <= menu.BUTTON_MAIN_POS[0] + menu.BUTTON_HALFSIZE[0] and menu.BUTTON_MAIN_POS[1] - menu.BUTTON_HALFSIZE[1] <= pos[1] <= menu.BUTTON_MAIN_POS[1] + menu.BUTTON_HALFSIZE[1]:
            #level1.LoadLevel()
            menu.game_start = True
            print("start button pressed")
        elif menu.BUTTON_HELP_MAIN_POS[0] - menu.BUTTON_HALFSIZE[0] <= pos[0] <= menu.BUTTON_HELP_MAIN_POS[0] + menu.BUTTON_HALFSIZE[0] and menu.BUTTON_HELP_MAIN_POS[1] - menu.BUTTON_HALFSIZE[1] <= pos[1] <= menu.BUTTON_HELP_MAIN_POS[1] + menu.BUTTON_HALFSIZE[1]:
            print("help button pressed")
            menu.show_help = True
            menu.show_menu = False
        elif menu.BUTTON_SCORES_POS[0] - menu.BUTTON_HALFSIZE[0] <= pos[0] <= menu.BUTTON_SCORES_POS[0] + menu.BUTTON_HALFSIZE[0] and menu.BUTTON_SCORES_POS[1] - menu.BUTTON_HALFSIZE[1] <= pos[1] <= menu.BUTTON_SCORES_POS[1] + menu.BUTTON_HALFSIZE[1]:
            print("scores button pressed")
            menu.show_scores = True
            menu.show_menu = False
    elif menu.game_start and menu.paused:
        if menu.BUTTON_RESUME_POS[0] - menu.BUTTON_HALFSIZE[0] <= pos[0] <= menu.BUTTON_RESUME_POS[0] + menu.BUTTON_HALFSIZE[0]:
            if menu.BUTTON_RESUME_POS[1] - menu.BUTTON_HALFSIZE[1] <= pos[1] <= menu.BUTTON_RESUME_POS[1] + menu.BUTTON_HALFSIZE[1]:
                menu.paused = False
                print("resume button pressed")
            elif menu.BUTTON_HELP_PAUSE_POS[1] - menu.BUTTON_HALFSIZE[1] <= pos[1] <= menu.BUTTON_HELP_PAUSE_POS[1] + menu.BUTTON_HALFSIZE[1]:
                print("help button pressed")
                menu.show_help = True
                menu.show_menu = False
            elif menu.BUTTON_MAINMENU_PAUSE_POS[1] - menu.BUTTON_HALFSIZE[1] <= pos[1] <= menu.BUTTON_MAINMENU_PAUSE_POS[1] + menu.BUTTON_HALFSIZE[1]:
                print("main menu button pressed")
                menu.game_end = True
                menu.paused = False
                menu.game_start = False
    elif menu.game_end:
        if menu.BUTTON_MAINMENU_END_POS[1] - menu.BUTTON_HALFSIZE[1] <= pos[1] <= menu.BUTTON_MAINMENU_END_POS[1] + menu.BUTTON_HALFSIZE[1]:
            menu.game_start = False
            print("menu button pressed")
    elif menu.won:
        if menu.BUTTON_MAINMENU_WIN_POS[1] - menu.BUTTON_HALFSIZE[1] <= pos[1] <= menu.BUTTON_MAINMENU_WIN_POS[1] + menu.BUTTON_HALFSIZE[1]:
            menu = Menu()
            print("menu button pressed")   
            
wall1 = TallWall(0)
wall3 = TallWall(CANVAS_DIMS[0])
wall4 = WideWall(0)
wall6 = WideWall(CANVAS_DIMS[1])

list_walls = [wall1, wall3, wall4, wall6]

player = Player()
enemy1 = Enemy(((CANVAS_DIMS[0]/6)*5,(CANVAS_DIMS[1]/8)*2),1,(20,20))
list_entities = [enemy1]

kbd = Keyboard()

interaction = Interaction(list_walls, list_entities, player)

frame = simplegui.create_frame("Stealth Game", CANVAS_DIMS[0], CANVAS_DIMS[1])
frame.set_canvas_background('White')
frame.set_draw_handler(interaction.draw)
frame.set_keydown_handler(kbd.keyDown)
frame.set_keyup_handler(kbd.keyUp)
frame.set_mouseclick_handler(mouse_handler)
frame.start()
