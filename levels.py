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
    player = Player()
    kbd = Keyboard()
    interaction = Interaction(kbd, globals.Walls, globals.Enemies, player, globals.Doors)
    def LoadLevel(self, enemyList, wallList, doorList, obstacleList):
        globals.Enemies = []
        globals.Obstacles = []
        globals.Walls = []
        for enemy in enemyList:
            globals.Enemies.append(enemy)
        for door in doorList:
            globals.Doors.append(door)
    
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
        #for rock in Levels.Rocks:
        #    rock.draw(canvas)
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
        #for gate in Levels.Gates:
        #    gate.draw(canvas)
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
        #Levels.Rocks = []  # List of rocks
        Levels.Projectiles = []  # list of projectiles
        Levels.wall_interactions = []  # list of wall interactions to help keep player within the walls
        #for wall in globals.Walls:
        #    Levels.wall_interactions.append(Interaction(Levels.player, wall))
        #Levels.Gates = []  # list of gates to move player between levels
        #Levels.GateInteractions = []  # list of interactions for above gates
        Levels.roomText = 0  # text to represent what room the player is in
        globals.score = 0
        #Levels.projectileCollision = ProjectileCollision(Levels.player)