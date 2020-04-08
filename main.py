try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import math, time, random

import globals
import menu
import keyboard
from enemy1 import Enemy
from player import Player
from vector import Vector
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

class Interaction:
    def __init__(self, kbd, list_walls, list_entities, player,enemy):
        self.player = player
        self.enemy = enemy
        self.list_walls = list_walls
        self.list_entities = list_entities
        
    def update(self): # changes player's velocity and spriteset based on keyboard events
        if kbd.right & kbd.left:
            self.player.vel.x = 0
        elif kbd.right: 
            self.player.vel.x = min(self.player.vel.x+0.01,player.speed)
            self.player.sprite_current = self.player.sprite_right
        elif kbd.left:            
            self.player.vel.x = max(self.player.vel.x-0.01,-player.speed)
            self.player.sprite_current = self.player.sprite_left
        if kbd.up & kbd.down:
            self.player.vel.x = 0
        if kbd.up:            
            self.player.vel.y = max(self.player.vel.y-0.01,-player.speed)
            self.player.sprite_current = self.player.sprite_up
        elif kbd.down:            
            self.player.vel.y = min(self.player.vel.y+0.01,player.speed)
            self.player.sprite_current = self.player.sprite_down
        
        if kbd.right & kbd.left:
            self.player.vel.x = 0
        elif kbd.right: 
            self.player.vel.x = player.speed
            self.player.sprite_current = self.player.sprite_right
        elif kbd.left:            
            self.player.vel.x = -player.speed
            self.player.sprite_current = self.player.sprite_left
        if kbd.up & kbd.down:
            self.player.vel.x = 0
        if kbd.up:            
            self.player.vel.y = -player.speed
            self.player.sprite_current = self.player.sprite_up
        elif kbd.down:            
            self.player.vel.y = player.speed
            self.player.sprite_current = self.player.sprite_down

        for wall in self.list_walls:
            s = wall.hit(player)
            if s!= 0:
                print('"Wall collision = True"')
                self.player.bounce(wall.normal)
                
         for wall in self.list_walls:
            s = wall.hit(enemy)
            if s!= 0:
                self.enemy.bounce(wall.normal)
                
        for entity in list_entities:
            entity.update()
      
        self.player.update()
        self.enemy.update()
    def draw(self, canvas):
        if globals.game_start and not globals.game_end:
            self.update()
            player.draw(canvas)
            player.update()
            for x in self.list_entities:
                x.draw(canvas)
                x.update()
            for y in self.list_walls:
                y.draw(canvas)            
        #lives(canvas)
        menu.draw(canvas)
        #menu.update()



wall1 = walls.TallWall(0)
wall3 = walls.TallWall(CANVAS_DIMS[0])
wall4 = walls.WideWall(0)
wall6 = walls.WideWall(CANVAS_DIMS[1])

list_walls = [wall1, wall3, wall4, wall6]

player = Player()
enemy = Enemy()
list_entities = [enemy]

kbd = Keyboard()

interaction = Interaction(kbd, list_walls, list_entities, player, enemy)

frame = simplegui.create_frame("COVID-19 Simulator 2020", CANVAS_DIMS[0], CANVAS_DIMS[1])
frame.set_canvas_background('White')
frame.set_draw_handler(interaction.draw)
frame.set_keydown_handler(kbd.keyDown)
frame.set_keyup_handler(kbd.keyUp)
frame.set_mouseclick_handler(mouse_handler)
frame.start()
