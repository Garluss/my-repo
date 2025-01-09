import time
import pygame as pg
import math as m

non_animated = ["Projectile"]

class Scene():
    current_scene = None
    def __init__(self, name, mod_x, mod_y, collissionmap, windowobject):
        self.name = name
        self.x = mod_x
        self.y = mod_y
        self.colmap = collissionmap
        self.windowobject = windowobject
    
    def surface_load(self):
        pic = "scenes/" + self.name + ".png"
        return pg.image.load(pic)
    
    # def test_col(self, x, y):
    #     try:
    #         if self.colmap.pxarray()[int(m.floor(x/3)), int(m.floor(y/3))] == -16777216:
    #             return True
    #         else:
    #             return False
    #     except IndexError:
    #         return "Error"
    def test_col(self, x, y):
        try:
            if self.colmap.pxarray()[int(x), int(y)] == -16777216:
                return True
            else:
                return False
        except IndexError:
            return "Error"
    
    def load(self):
        Scene.current_scene = self
        pic = "scenes/" + self.name + ".png"
        img = pg.image.load(pic)
        if self.x != 200 and self.y != 100:
            img = pg.transform.scale(img,(self.x,self.y))
        rect = img.get_rect()
        rect.center = self.windowobject.get_width()/2, self.windowobject.get_height()/2
        self.windowobject.blit(img, rect)

class ColMap():
    def __init__(self, name, mod_x, mod_y, windowobject):
        self.name = name
        self.x = mod_x
        self.y = mod_y
        self.windowobject = windowobject
    def pxarray(self):
        pic = "scenes/" + self.name + ".png"
        img = pg.image.load(pic)

        #img = pg.transform.scale(img,(self.x,self.y)) #check this
        
        return pg.PixelArray(img)



class Sprite():
    instances = []
    def __init__(self, x, y, speed_x, speed_y, animroot, windowobject):
        if self.__class__.__name__ not in non_animated:
            Sprite.instances.append(self)
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.x = x
        self.y = y
        self.a = animroot
        self.windowobject = windowobject
    
    def load(self, anim:str):
        pic = "animations/" + self.a + "/" + anim + ".png"
        img = pg.image.load(pic)
        return img
    
    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def draw(self, x=28, y=28, flip_x=False, flip_y=False):
        img = self.load(self.frame)
        if flip_x != False or flip_y != False:
            img = pg.transform.flip(img,flip_x,flip_y)
        if x != 28 and y != 28:
            img = pg.transform.scale(img,(x,y))
        rect = img.get_rect()
        rect.center = self.x, self.y
        self.windowobject.blit(img, rect)

    
    def collission_dec(self):
        next_x = self.x + self.speed_x
        next_y = self.y + self.speed_y
        if Scene.current_scene.test_col(next_x, next_y) == True:
            if Scene.current_scene.test_col(next_x,self.y) == True and self.speed_x > 0:
                return "east"
            if Scene.current_scene.test_col(next_x,self.y) == True and self.speed_x < 0:
                return "west"
            if Scene.current_scene.test_col(self.x,next_y) == True and self.speed_y > 0:
                return "south"
            if Scene.current_scene.test_col(self.x,next_y) == True and self.speed_y < 0:
                return "north"
        return False

class Item():
    def __init__(self, name, x=0, y=0, bpx=0, bpy=0):
        self.name = name
        self.x = x
        self.y = y
        self.barrel_posx = bpx
        self.barrel_poxy = bpy
    
    def get_name(self):
        return self.name

class Projectile():
    p_instances = []
    def __init__(self, x, y, speed, img, animroot, windowobject, max_bounces):
        Projectile.p_instances.append(self)
        self.x = x
        self.y = y
        self.a = animroot
        self.windowobject = windowobject
        self.max_bounces = max_bounces
        self.bounces = 0
        self.frame = img
        self.speed = speed
        self.velocity_x = self.speed
        self.angle = self.get_angle()
        self.velocity_y = 0
        self.queue = False
    
    def collission_dec(self):
        next_x = self.x + self.velocity_x
        next_y = self.y + self.velocity_y
        if Scene.current_scene.test_col(next_x, next_y) == "Error":
            self.queue = True
        if Scene.current_scene.test_col(next_x, next_y) == True:
            if Scene.current_scene.test_col(next_x,self.y) == True and self.velocity_x > 0:
                self.bounces += 1
                return "east"
            if Scene.current_scene.test_col(next_x,self.y) == True and self.velocity_x < 0:
                self.bounces += 1
                return "west"
            if Scene.current_scene.test_col(self.x,next_y) == True and self.velocity_y > 0:
                self.bounces += 1
                return "south"
            if Scene.current_scene.test_col(self.x,next_y) == True and self.velocity_y < 0:
                self.bounces += 1
                return "north"

    
    def load(self, anim:str):
        pic = "animations/" + self.a + "/" + anim + ".png"
        img = pg.image.load(pic)
        return img
    
    # def set_path(self, tx, ty):
    #     dx = tx - self.x
    #     dy = ty - self.y
    #     self.velocity_x = dx/self.speed
    #     if dx != 0: 
    #         self.velocity_y = (dy/dx)*self.velocity_x
    #         print(f"{self.velocity_x}, {self.velocity_y}")
    #     else:
    #         self.velocity_y = 0

    def set_path(self, tx, ty):
        v = pg.Vector2(tx-self.x,ty-self.y)
        v = v.normalize()
        self.velocity_x = v.x * self.speed
        self.velocity_y = v.y * self.speed

    def move(self):
        # if self.is_touching_border() == 1 or self.is_touching_border() == 2:
        #     self.velocity_y = -(self.velocity_y)
        #     self.bounces += 1
        # elif self.is_touching_border() == 3 or self.is_touching_border() == 4:
        #     self.velocity_x = -(self.velocity_x)
        #     self.bounces += 1
        if self.collission_dec() == "east" or self.collission_dec() == "west":
            self.velocity_x = -(self.velocity_x)
        if self.collission_dec() == "north" or self.collission_dec() == "south":
            self.velocity_y = -(self.velocity_y)
        self.x += self.velocity_x
        self.y += self.velocity_y
    
    def draw(self, x=28, y=28, flip_x=False, flip_y=False):
        img = self.load(self.frame)
        if flip_x != False or flip_y != False:
            img = pg.transform.flip(img,flip_x,flip_y)
        if x != 28 and y != 28:
            img = pg.transform.scale(img,(x,y))
        img = pg.transform.rotate(img,90) #rotate to correct the wrong direction in .png file
        img = pg.transform.rotate(img,self.angle)
        rect = img.get_rect()
        rect.center = self.x, self.y
        self.windowobject.blit(img, rect)
    def get_angle(self):
        m_x, m_y = pg.mouse.get_pos()
        dx = -(self.x - m_x)
        dy = self.y - m_y
        if dx != 0:
            return m.degrees(m.atan(dy/dx))
        else:
            return 0
    
    def queue_destruction(self):
        if self.bounces >= self.max_bounces or self.queue == True:
            return True
        return False

class Goober(Sprite):
    def __init__(self, speed_x, speed_y, x, y, animroot, windowobject):
        super().__init__(x, y, speed_x, speed_y, animroot, windowobject)
        self.is_busy = False
        self.equipped_item = None
        self.frame = "idle-0"
        self.animation_index = 0
        self.idle = ["idle-0","idle-0","idle-1","idle-1"]
        self.walk = ["walk-0","walk-1","walk-2","walk-3","walk-4","walk-5","walk-6","walk-7"]
        self.current_animation = self.idle
    def equip(self, item):
        self.equipped_item = item
    def tick_animation(self):
        if self.is_busy == False:
            if self.animation_index > len(self.current_animation)-1:
                self.animation_index = 0
            self.frame = self.current_animation[self.animation_index]
            self.animation_index += 1
        else:
            if self.animation_index > len(self.current_animation)-1:
                self.animation_index = 0
                self.is_busy = False
            else:
                self.frame = self.current_animation[self.animation_index]
                self.animation_index += 1
    def set_state(self, state="idle"):
        match state:
            case "idle": self.current_animation = self.idle
            case "walk": self.current_animation = self.walk
            case _: return ValueError
    def is_sprite_busy(self):
        return self.is_busy
    def draw(self, x=28, y=28, flip_x=False, flip_y=False):
        img = self.load(self.frame)
        if flip_x != False or flip_y != False:
            img = pg.transform.flip(img,flip_x,flip_y)
        if x != 28 and y != 28:
            img = pg.transform.scale(img,(x,y))
        rect = img.get_rect()
        rect.center = self.x, self.y
        self.windowobject.blit(img, rect)
        if self.equipped_item != None:
            self.draw_item(x, y)
    def get_gun_angle(self,m_x,m_y):
        dx = -(self.x - m_x)
        dy = self.y - m_y
        #print(f"X: {self.x}, Y: {self.y}, m_x: {m_x}, m_y: {m_y}")
        if dx != 0:
            #print(m.degrees(m.atan(dy/dx)))
            return m.degrees(m.atan(dy/dx))
        else:
            return 0
    def draw_item(self, x, y):
        m_x, m_y = pg.mouse.get_pos()
        img = self.load(self.equipped_item.get_name())
        if x != 28 and y != 28:
            img = pg.transform.scale(img,(x,y))
        if -(self.x - m_x) < 0:
            img = pg.transform.flip(img,True,False)
        img = pg.transform.rotate(img,self.get_gun_angle(m_x,m_y))
        rect = img.get_rect()
        rect.center = self.x, self.y
        self.windowobject.blit(img, rect)
