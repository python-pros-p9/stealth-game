from vector import Vector

#  CONSTANTS
CANVAS_DIMS = (1000, 600) # the size of the map/window

# VARIABLES
game_start = False # is the actual game running?
game_end = False # has the game ended?
game_paused = False # is the game paused?
game_won = False # did the player win?
show_menu = True # are we on the main menu?
show_help = False # are we on the help menu?
show_scores = False # are we on the "scores" page?
score = 0
current_level = 0
player_pos = Vector(CANVAS_DIMS[0]/4, CANVAS_DIMS[1]/4)