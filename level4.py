try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from levels import Levels
from rock import Rock
from meleeEnemy import MeleeEnemy
from superMeleeEnemy import SuperMeleeEnemy
from rangedEnemy import RangedEnemy
from gates import Gate
from room import Room
import globals