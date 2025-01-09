import math as m
import pygame as pg
from pygame.locals import (K_UP, K_DOWN,K_w,K_s)
pg.init()

wWidth = 1000
wHeight = 500
window = pg.display.set_mode([wWidth, wHeight])

font = pg.font.SysFont("Arial", 24)

def find_distance(obj1, obj2):
    squaredXDistance = (obj1.x - obj2.x)**2
    squaredYDistance = (obj1.y - obj2.y)**2
    return m.sqrt(squaredXDistance + squaredYDistance)

class Ball():
    def __init__(self, x, y, velocity_x, velocity_y, radius, windowobject):
        self.x = x
        self.y = y
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.radius = radius
        self.windowobject = windowobject
    
    def draw(self):
        pg.draw.circle(self.windowobject, (0,0,0), (self.x, self.y), self.radius)
    
    def is_touching(self):
        if (self.x - self.radius) <= 0:
            return 1
        elif (self.x + self.radius) >= self.windowobject.get_width():
            return 1
        elif (self.y - self.radius) <= 0:
            return 2
        elif (self.y + self.radius) >= self.windowobject.get_height():
            return 2
        elif (self.x + self.radius) >= racketR.get_x() and (self.y - self.radius) <= (racketR.get_y() + racketR.get_height()) and (self.y + self.radius) >= racketR.get_y():
            return 1
        elif (self.x - self.radius) <= (racketL.get_x()+15) and (self.y - self.radius) <= (racketL.get_y() + racketL.get_height()) and (self.y + self.radius) >= racketL.get_y():
            return 1
        else:
            return False
    
    def move(self):
        if self.is_touching() == 1:
            self.velocity_x = -self.velocity_x
        if self.is_touching() == 2:
            self.velocity_y = -self.velocity_y
        self.x = self.x + self.velocity_x
        self.y = self.y + self.velocity_y

class Racket():
    def __init__(self, x, y, height, windowobject):
        self.x = x
        self.y = y
        self.windowobject = windowobject
        self.height = height
    
    def draw(self):
        pg.draw.rect(self.windowobject, (0,0,0), pg.Rect(self.x,self.y,15,self.height))
    
    def get_y(self):
        return self.y
    
    def get_x(self):
        return self.x
    
    def get_height(self):
        return self.height
    
    def is_touching_border(self):
        if self.y <= 0 or (self.y + self.height) >= self.windowobject.get_height():
            return 1
        elif self.y >= 0:
            return 2
        else:
            return False

    # def move(self):
    #     if self.is_touching_border() == 2: 
    #         self.y = self.y + self.speed
    #     else:
    #         self.y = self.y

racketL = Racket(20, 50, 150, window)
racketR = Racket(wWidth-40, 50, 150, window)
ball = Ball(250, 250, 0.4, 0, 20, window)
ball.velocity_y = 0.3


contgame = True
while contgame == True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            contgame = False
    
    pressed_keys = pg.key.get_pressed()

    if pressed_keys[K_DOWN]:
        racketL.y += 0.1
    if pressed_keys[K_UP]:
        racketL.y += -0.1
    if pressed_keys[K_s]:
        racketR.y += 0.1
    if pressed_keys[K_w]:
        racketR.y += -0.1
    
    window.fill((255,255,255))

    ball.draw()
    ball.move()

    racketL.draw()
    racketR.draw()

    pg.display.flip()
    
pg.quit()
