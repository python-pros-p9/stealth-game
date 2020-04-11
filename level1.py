try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from vector import Vector
from levels import Levels
import walls
from enemy import Enemy
#from rock import Rock
#from meleeEnemy import MeleeEnemy
#from rangedEnemy import RangedEnemy
from doors import Door
#from room import Room
import globals

#list_walls = [wall1, wall3, wall4, wall6]

# stores values for level
class Level1(Levels):
    def __init__(self):
        globals.levels.append(self)
        #self.Enemies = [Enemy(((globals.CANVAS_DIMS[0] / 9) * 5, (globals.CANVAS_DIMS[1] / 9) * 2)), Enemy(((globals.CANVAS_DIMS[0] / 9) * 8, (globals.CANVAS_DIMS[1] / 9) * 7))]
        self.Enemies = [ Enemy((((globals.CANVAS_DIMS[0]/9)*5),((globals.CANVAS_DIMS[1]/9)*2)),Vector(2,2),(25,25))]
        #self.RangedEnemies = []
        self.Obstacles =[] # [Rock(((globals.CANVAS_DIMS[0] / 6) * 2, (globals.CANVAS_DIMS[1] / 8) * 3)), Rock(((globals.CANVAS_DIMS[0] / 9) * 7, (globals.CANVAS_DIMS[1] / 5) * 4))]
        self.Doors = [Door(0, 0, 1)]
        #self.Room = Room()

        self.Walls = [walls.TallWall((0,0),(0,globals.CANVAS_DIMS[1])),
        walls.TallWall((globals.CANVAS_DIMS[0],0),globals.CANVAS_DIMS),
        walls.WideWall((0,0),(globals.CANVAS_DIMS[0],0)),
        walls.WideWall((globals.CANVAS_DIMS[0],0),(globals,globals.CANVAS_DIMS))]

    def LoadLevel(self, Enemies, Walls, Doors, Obstacles):
        #super().LoadLevel(self.Enemies, self.Walls, self.Doors, self.Obstacles)
        Levels.roomText = 1