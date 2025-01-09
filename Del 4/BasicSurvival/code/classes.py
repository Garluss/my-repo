import random
import time
import numpy as np
import pygame as pg
import math as m

class Scene():
    current_scene = None
    def __init__(self, x, y, scene, windowobject, g_size_mod):
        self.x = x
        self.y = y
        self.scene = scene
        self.windowobject = windowobject
        self.mod = g_size_mod
    def load(self):
        Scene.current_scene = self
    def get_col_map(self):
        img = pg.image.load(self.scene)
        img = pg.transform.scale(img,(500*self.mod,500*self.mod))
        return pg.PixelArray(img)
    def draw(self):
        img = pg.image.load(self.scene)
        img = pg.transform.scale(img,(500*self.mod,500*self.mod))
        rect = img.get_rect()
        rect.center = self.x, self.y
        self.windowobject.blit(img, rect)
    def move(self, velx, vely):
        self.x += velx*(-1)
        self.y += vely*(-1)
    def out_of_bounds(self, x, y):
        if x > 500*self.mod or y > 500*self.mod:
            return True
        if x < 0 or y < 0:
            return True
        return False

class Text():
    def __init__(self, text, font, x, y, color, windowobject):
        self.text = text
        self.font = font
        self.color = color
        self.x = x
        self.y = y
        self.windowobject = windowobject
    def set_text(self, text):
        self.text = text
    def draw(self):
        surface = self.font.render(self.text, True, self.color)
        rect = surface.get_rect()
        rect.center = self.x, self.y
        self.windowobject.blit(surface,rect)

class Sprite():
    def __init__(self, x, y, animroot, windowobject, g_size_mod):
        self.x = x
        self.y = y
        self.world_x = 0
        self.world_y = 0
        self.a = animroot
        self.windowobject = windowobject
        self.mod = g_size_mod

    def draw(self):
        img = pg.image.load(self.frame)
        img = pg.transform.scale(img,(28*self.mod,28*self.mod))
        rect = img.get_rect()
        rect.center = self.x, self.y
        self.windowobject.blit(img, rect)
    
    def col_dec(self):
        colmap = Scene.current_scene.get_col_map()
        if colmap[int(self.x+self.current_s_x)][int(self.y+self.current_s_y)] == -16777216:
            return True
        return False

class Entity():
    instances = []
    def __init__(self, speed_x, speed_y, x, y, animroot, windowobject, g_size_mod):
        Entity.instances.append(self)
        self.x = x
        self.y = y
        self.a = animroot
        self.windowobject = windowobject
        self.mod = g_size_mod
        self.s_x = speed_x
        self.s_y = speed_y
        self.frame = "animations/groopie/normal.png"
        self.current_s_x = 0
        self.current_s_y = 0
    def change_speeds(self):
        r_x = (random.randint(-(self.s_x*100),(self.s_x*100))/100)
        r_y = (random.randint(-(self.s_y*100),(self.s_y*100))/100)
        self.current_s_x = r_x
        self.current_s_y = r_y
    def set_path(self, tx, ty):
        v = pg.Vector2(tx-self.x,ty-self.y)
        v = v.normalize()
        self.current_s_x = v.x * self.s_x
        self.current_s_y = v.y * self.s_y
    def move(self):
        self.world_x = self.x + -(Scene.current_scene.x-(750))
        self.world_y = self.y + -(Scene.current_scene.y-(750))
        if self.col_dec() == False:
            self.x += self.current_s_x
            self.y += self.current_s_y
    def draw(self):
        img = pg.image.load(self.frame)
        img = pg.transform.scale(img,(28*self.mod,28*self.mod))
        rect = img.get_rect()
        rect.center = self.x, self.y
        self.windowobject.blit(img, rect)
    def col_dec(self):
        colmap = Scene.current_scene.get_col_map()
        if colmap[int(self.world_x+self.current_s_x)][int(self.world_y+self.current_s_y)] == -16777216:
            return True
        if Scene.current_scene.out_of_bounds(self.world_x+self.current_s_x, self.world_y+self.current_s_y) == True:
            return True 
        return False
    def check_visual(self, target_entity, range):
        t_x = target_entity.x
        t_y = target_entity.y
        v = pg.math.Vector2(t_x-self.x,t_y-self.y)
        if v.length() < range:
            lin = np.linspace(0,v.length(),50)
            if v[1] != 0:
                s = v[0]/v[1]
                for i in lin:
                    colmap = Scene.current_scene.get_col_map()
                    # CHECK THIS
                    # print(i + -(Scene.current_scene.x-(750)), i*s + -(Scene.current_scene.y-(750)))
                    # if colmap[int(i + -(Scene.current_scene.x-(750)))][int(i*s + -(Scene.current_scene.y-(750)))] == -16777216:
                    #     return False
                    return True
                
    def shift(self, velx, vely):
        self.x += velx*(-1)
        self.y += vely*(-1)

class Player(Sprite):
    def __init__(self, speed_x, speed_y, x, y, animroot, windowobject, g_size_mod):
        super().__init__(x, y,  animroot, windowobject, g_size_mod)
        self.is_busy = False
        self.s_x = speed_x
        self.s_y = speed_y
        self.current_s_x = 0
        self.current_s_y = 0
        self.frame = "animations/player/normal.png"
    def is_sprite_busy(self):
        return self.is_busy
    def move(self):
        self.x += self.current_s_x
        self.y += self.current_s_y
    def col_dec(self):
        colmap = Scene.current_scene.get_col_map()
        if colmap[int(self.world_x+self.current_s_x)][int(self.world_y+self.current_s_y)] == -16777216:
            return True
        if Scene.current_scene.out_of_bounds(self.world_x+self.current_s_x, self.world_y+self.current_s_y) == True:
            return True 
        return False
