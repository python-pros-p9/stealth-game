try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import math, time, random

import globals
import menu
import keyboard
import enemy
from player import Player
from vector import Vector
from interactions import Interaction
import walls
import levels
from spritesheet import SpriteSheet

#CONSTANTS - use all caps, separated by underscores
CANVAS_DIMS = globals.CANVAS_DIMS
PLAYER_WALK_SPEED = 2
PLAYER_START_POS = [CANVAS_DIMS[0]/4, CANVAS_DIMS[1]/4]
menu = menu.Menu()

#VARIABLES - use lowercase words, separated by underscores
level = 0
#Controls
# WASD (up, left, down, right) to dictate movement direction
    
def mouse_handler(pos):
    #global menu
    if globals.show_help or globals.show_scores or globals.game_end or globals.game_won:
        globals.show_help = globals.game_end = globals.game_won = globals.show_scores = False
        globals.show_menu = True
    elif not globals.game_start and globals.show_menu:
        if menu.BUTTON_START_MAIN_POS[0] - menu.BUTTON_HALFSIZE[0] <= pos[0] <= menu.BUTTON_START_MAIN_POS[0] + menu.BUTTON_HALFSIZE[0] and menu.BUTTON_START_MAIN_POS[1] - menu.BUTTON_HALFSIZE[1] <= pos[1] <= menu.BUTTON_START_MAIN_POS[1] + menu.BUTTON_HALFSIZE[1]:
            #level1.LoadLevel()
            globals.game_start = True
            print("start button pressed")
        elif menu.BUTTON_HELP_MAIN_POS[0] - menu.BUTTON_HALFSIZE[0] <= pos[0] <= menu.BUTTON_HELP_MAIN_POS[0] + menu.BUTTON_HALFSIZE[0] and menu.BUTTON_HELP_MAIN_POS[1] - menu.BUTTON_HALFSIZE[1] <= pos[1] <= menu.BUTTON_HELP_MAIN_POS[1] + menu.BUTTON_HALFSIZE[1]:
            print("help button pressed")
            globals.show_help = True
            globals.show_menu = False
        elif menu.BUTTON_SCORES_POS[0] - menu.BUTTON_HALFSIZE[0] <= pos[0] <= menu.BUTTON_SCORES_POS[0] + menu.BUTTON_HALFSIZE[0] and menu.BUTTON_SCORES_POS[1] - menu.BUTTON_HALFSIZE[1] <= pos[1] <= menu.BUTTON_SCORES_POS[1] + menu.BUTTON_HALFSIZE[1]:
            print("scores button pressed")
            globals.show_scores = True
            globals.show_menu = False
    elif globals.game_start and globals.game_paused:
        if menu.BUTTON_RESUME_POS[0] - menu.BUTTON_HALFSIZE[0] <= pos[0] <= menu.BUTTON_RESUME_POS[0] + menu.BUTTON_HALFSIZE[0]:
            if menu.BUTTON_RESUME_POS[1] - menu.BUTTON_HALFSIZE[1] <= pos[1] <= menu.BUTTON_RESUME_POS[1] + menu.BUTTON_HALFSIZE[1]:
                globals.game_paused = False
                print("resume button pressed")
            elif menu.BUTTON_HELP_PAUSE_POS[1] - menu.BUTTON_HALFSIZE[1] <= pos[1] <= menu.BUTTON_HELP_PAUSE_POS[1] + menu.BUTTON_HALFSIZE[1]:
                print("help button pressed")
                globals.show_help = True
                globals.show_menu = False
            elif menu.BUTTON_MAINMENU_PAUSE_POS[1] - menu.BUTTON_HALFSIZE[1] <= pos[1] <= menu.BUTTON_MAINMENU_PAUSE_POS[1] + menu.BUTTON_HALFSIZE[1]:
                print("main menu button pressed")
                globals.game_end = True
                globals.game_paused = False
                globals.game_start = False
    elif globals.game_end:
        if menu.BUTTON_MAINMENU_END_POS[1] - menu.BUTTON_HALFSIZE[1] <= pos[1] <= menu.BUTTON_MAINMENU_END_POS[1] + menu.BUTTON_HALFSIZE[1]:
            globals.game_start = False
            print("menu button pressed")
    elif globals.game_won:
        if menu.BUTTON_MAINMENU_WIN_POS[1] - menu.BUTTON_HALFSIZE[1] <= pos[1] <= menu.BUTTON_MAINMENU_WIN_POS[1] + menu.BUTTON_HALFSIZE[1]:
            #menu = Menu()
            print("menu button pressed")   
            
wall1 = walls.TallWall(0)
wall3 = walls.TallWall(CANVAS_DIMS[0])
wall4 = walls.WideWall(0)
wall6 = walls.WideWall(CANVAS_DIMS[1])

list_walls = [wall1, wall3, wall4, wall6]

player = Player()
enemy1 = enemy.Enemy(((CANVAS_DIMS[0]/6)*5,(CANVAS_DIMS[1]/8)*2),1,(20,20))
list_entities = [enemy1]

kbd = keyboard.Keyboard()

interaction = Interaction(list_walls, list_entities, player)

frame = simplegui.create_frame("COVID-19 Simulator 2020", CANVAS_DIMS[0], CANVAS_DIMS[1])
frame.set_canvas_background('White')
frame.set_draw_handler(interaction.draw)
frame.set_keydown_handler(kbd.keyDown)
frame.set_keyup_handler(kbd.keyUp)
frame.set_mouseclick_handler(mouse_handler)
frame.start()
