import os
import random
import pygame as pg
clock = pg.time.Clock()

pg.init()

font = pg.font.SysFont("Arial", 24)

class Text():
    def __init__(self, text, windowobject):
        self.text = text
        self.windowobject = windowobject
    def draw(self, x, y):
        surface = font.render(self.text, True, (0,0,0))
        rect = surface.get_rect()
        rect.center = x, y
        self.windowobject.blit(surface,rect)
class Score(Text):
    def __init__(self, text, windowbject):
        super().__init__(text,windowbject)
        self.score = 0
    def set_score(self, score):
        self.score = score
    def get_score(self):
        return self.score
    def add_score(self, add):
        self.score = self.score + add
    def draw(self, x, y):
        score_text = self.text + str(self.score)
        surface = font.render(score_text, True, (0,0,0))
        rect = surface.get_rect()
        rect.center = x, y
        self.windowobject.blit(surface,rect)
class Timer(Text):
    def __init__(self, text, windowobject):
        super().__init__(text,windowobject)
        self.time = 0
    def tick_time(self,t):
        self.time = round(self.time - t,1)
    def set_time(self, time):
        self.time = time
    def get_time(self):
        return self.time
    def draw(self, x, y):
        time_text = self.text + str(self.time)
        surface = font.render(time_text, True, (0,0,0))
        rect = surface.get_rect()
        rect.center = x, y
        self.windowobject.blit(surface,rect)
class Target():
    def __init__(self, size_x, size_y, x, y, windowobject):
        self.size_x = size_x
        self.size_y = size_y
        self.x = x
        self.y = y
        self.windowobject = windowobject
    def draw(self):
        surface = pg.Surface((self.size_x,self.size_y))
        surface.fill((0,0,0))
        rect = surface.get_rect()
        rect.center = self.x, self.y
        self.windowobject.blit(surface,rect)
    def get_size_x(self):
        return self.size_x
    def get_size_y(self):
        return self.size_y
    def set_size_x(self, x):
        self.size_x = x
    def set_size_y(self,y):
        self.size_y = y
    def set_x(self,x):
        self.x = x
    def set_y(self,y):
        self.y = y
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def is_within(self, x, y):
        if x > (self.x - self.size_x/2) and x < (self.x + self.size_x/2):
            if y > (self.y - self.size_y/2) and y < (self.y + self.size_y/2):
                return True
        return False


wWidth = 600
wHeight = 600
r_y = 300
r_x = 300
window = pg.display.set_mode([wWidth, wHeight])


FPS = 60
pressed = 0
tick = 0
end = 0
s = 0
tick_end = False

score = Score("Your current score is: ",window)
score.set_score(0)
timer = Timer("Time left: ", window)
timer.set_time(10)

r_h = 50
r_w = 50
target = Target(r_w,r_h,r_x,r_y,window)

file_path = os.path.dirname(__file__) + "\highscore.txt"

f = open(file_path, "a")
f.close()

contgame = True
while contgame == True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            contgame = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            mx, my = pg.mouse.get_pos()
            if target.is_within(mx,my) == True:
                score.add_score(1)
                pressed = 3
    if tick >= 6:
        tick = 0
        s += 0.1
        timer.tick_time(0.1)

    
    if end > 0:
        window.fill((0,0,0))
    else:
        if pressed > 0:
            window.fill((0,255,0))
        else:
            window.fill((255,255,255))
    
    if timer.get_time() == 0.0 and end == 0:
        print(f"Score is {score.get_score()}")
        tick_end = True
        m = open(file_path, 'r')
        hs = m.read()
        m.close()
        if hs != "":
            if score.get_score() > int(hs):
                print("New highscore!")
                m = open(file_path,'w')
                m.write(str(score.get_score()))
                m.close()
        else:
            m = open(file_path,'w')
            m.write(str(score.get_score()))
            m.close()
    
    if s >= 2.0:
        s = 0
        r_h = random.randint(30,100)
        r_w = random.randint(30,100)
        r_y = random.randint(int(target.get_size_y()/2),window.get_height())
        r_x = random.randint(int(target.get_size_x()/2),window.get_width())

    target.set_size_x(r_w)
    target.set_size_y(r_h)
    target.set_x(r_x)
    target.set_y(r_y)
    target.draw()
    score.draw(wWidth/2,wHeight/2)
    timer.draw(wWidth/2,200)
    pg.display.flip()

    pressed -= 1
    tick += 1
    if tick_end == True:
        end += 1
        if end >= 3*60:
            tick_end = False
            end = 0
            score.set_score(0)
            timer.set_time(10)
            r_y = wHeight/2
            r_x = wWidth/2
            r_h = 50
            r_w = 50
    clock.tick(FPS)
pg.quit()