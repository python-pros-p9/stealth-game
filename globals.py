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


Walls = []
levels = []         # list of levels, appended as they load
Enemies = []        # list of enemies
Obstacles =  []     # list of obstacles
Doors = []          # list of doorways
PickUps = []        # list of collectable items (lives etc.)

#room = None # background for level
levels = []  # list of levels. levels get appended here when they load
#MeleeEnemies = []  # list of melee enemies
#ObjInteractions = []  # just initialising var to store interactions between melee enemies
#RangedEnemies = []  # list of ranged enemies
#Rocks = []  # List of rocks
#FriendlyProjectiles = []  # list of projectiles
#EnemyProjectiles = []
#wall_interactions = []  # list of wall interactions to help keep player within the walls
#GateInteractions = []  # list of interactions for above gates
#roomText = 0  # text to represent what room the player is in


