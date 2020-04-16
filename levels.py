try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from player import Player
from walls import TallWall
from walls import WideWall
import globals
from enemy import Enemy
from keyboard import Keyboard
from interactions import Interaction
#for wall in Walls:
#    wall_interactions.append(Interaction(player, wall))
#playerInteraction = PlayerInteraction(player, kbd, Walls)  # interaction to keep player within the walls
#projectileCollision = ProjectileCollision(player)

class Levels:
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
    #Obstacles = []  # List of obstacles
    #FriendlyProjectiles = []  # list of projectiles
    #EnemyProjectiles = []
    #wall_interactions = []  # list of wall interactions to help keep player within the walls
    #DoorInteractions = []  # list of interactions for above doors
    #roomText = 0  # text to represent what room the player is in

    player = Player()
    kbd = Keyboard()
    interaction = Interaction(kbd, Walls, Enemies, player, Doors)

    

    def LoadLevel(self, meleeEnemiesList, rangedEnemiesList, doorList, obstacleList):
        Levels.MeleeEnemies = []
        Levels.RangedEnemies = []
        Levels.Obstacles = []
        Levels.FriendlyProjectiles = []
        Levels.EnemyProjectiles = []
        Levels.room = None
        Levels.ObjInteractions = []
        Levels.allObj = []
        Levels.Enemies = []
        Levels.Obstacles = obstacleList
        for obstacle in obstacleList:
            Levels.allObj.append(obstacle)
        Levels.MeleeEnemies = meleeEnemiesList
        for enemy in meleeEnemiesList:
            Levels.allObj.append(enemy)
            Levels.Enemies.append(enemy)
        Levels.RangedEnemies = rangedEnemiesList
        for enemy in rangedEnemiesList:
            Levels.allObj.append(enemy)
            Levels.Enemies.append(enemy)
        Levels.Doors = []
        for door in doorList:
            Levels.Doors.append(door)
        
    
    @staticmethod
    def update():
        Levels.player.update()
        Levels.interaction.update()
        for door in globals.Doors:
            door.update()
        for enemy in globals.Enemies:
            enemy.update()

    @staticmethod
    def draw(canvas):
        #Levels.room.draw(canvas)
        Levels.player.draw(canvas)
        #for obstacle in Levels.Obstacles:
        #    obstacle.draw(canvas)
        #for melee in Levels.MeleeEnemies:
        #    melee.draw(canvas)
        #for ranged in Levels.RangedEnemies:
        #    ranged.draw(canvas)
        #for projectiles in Levels.EnemyProjectiles:
        #    projectiles.draw(canvas)
        #for projectiles in Levels.FriendlyProjectiles:
        #    projectiles.draw(canvas)
        for wall in globals.Walls:
            wall.draw(canvas)
        #for door in Levels.Doors:
        #    door.draw(canvas)
        canvas.draw_text("Room: " + str(Levels.roomText), (10, 9), 15, "White")
        canvas.draw_text("Score: " + str(globals.score), (930, 9), 15, "White")
    
    @staticmethod
    def restart():
        Levels.player = Player()  # the player
        Levels.kbd = Keyboard()  # keyboard class to check movement for player
        Levels.room = None  # background for level
        #Levels.Walls = [Wall(0), Wall(1), Wall(2), Wall(3)]  # all the walls
        #Levels.playerInteraction = PlayerInteraction(Levels.player, Levels.kbd, Levels.Walls)  # interaction to keep player within the walls
        Levels.levels = []  # list of levels. levels get appended here when they load
        #Levels.MeleeEnemies = []  # list of melee enemies
        #Levels.ObjInteractions = []  # just initialising var to store interactions between melee enemies
        #Levels.RangedEnemies = []  # list of ranged enemies
        #Levels.Obstacles = []  # List of obstacles
        Levels.Projectiles = []  # list of projectiles
        Levels.wall_interactions = []  # list of wall interactions to help keep player within the walls
        #for wall in globals.Walls:
        #    Levels.wall_interactions.append(Interaction(Levels.player, wall))
        #Levels.Doors = []  # list of doors to move player between levels
        #Levels.DoorInteractions = []  # list of interactions for above doors
        Levels.roomText = 0  # text to represent what room the player is in
        globals.score = 0
        #Levels.projectileCollision = ProjectileCollision(Levels.player)