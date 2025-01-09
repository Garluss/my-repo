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

wWidth = 600
wHeight = 600
window = pg.display.set_mode([wWidth, wHeight])


FPS = 60
pressed = 0
tick = 0

score = Score("Your current score is: ",window)
score.set_score(0)
timer = Timer("Time left: ", window)
timer.set_time(10)

contgame = True
while contgame == True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            contgame = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            score.add_score(1)
            pressed = 3
    
    if tick >= 6:
        tick = 0
        timer.tick_time(0.1)
    
    if pressed > 0:
        window.fill((0,255,0))
    else:
        window.fill((255,255,255))
    
    if timer.get_time() == 0.0:
        print(f"Score is {score.get_score()}")
        contgame = False

    score.draw(wWidth/2,wHeight/2)
    timer.draw(wWidth/2,200)
    pg.display.flip()

    pressed -= 1
    tick += 1
    clock.tick(FPS)
pg.quit()