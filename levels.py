try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from player import Player
from interactions import Interaction
from keyboard import Keyboard
from playerInteraction import PlayerInteraction
from walls import Wall
from interactionSet import *
from projectileCollision import ProjectileCollision
import globals
from scores import *