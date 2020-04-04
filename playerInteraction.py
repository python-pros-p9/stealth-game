try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from vector import Vector

class Interaction:
    def __init__(self, list_walls, list_entities):
        self.player = player
        self.list_walls = list_walls
        self.list_entities = list_entities
        
    def update(self): # changes player's velocity and spriteset based on keyboard events

        #if kbd.right & kbd.left:
        #    self.player.vel.x = 0
        if kbd.right: 
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
                
        for entity in list_entities:
            entity.update()
      
        self.player.update()
        
    def draw(self, canvas):
        #canvas.draw_image(simplegui.load_image("https://cdn.shopify.com/s/files/1/0148/8783/products/Texture-example-image_1024x1024.jpg"), menu.TITLETEXT_CENTRE, menu.TITLETEXT_DIMS, menu.TITLETEXT_POS, menu.TITLETEXT_SIZE)
        if globals.game_start and not globals.game_end:
            self.update()
            for x in self.list_entities:
                x.draw(canvas)
                x.update()
            for y in self.list_walls:
                y.draw(canvas)            
        
        menu.draw(canvas)
        #menu.update()
