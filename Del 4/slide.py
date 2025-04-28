import pygame as pg
clock = pg.time.Clock()

window = pg.display.set_mode((500,500))

def find_avg(list):
    if len(list) < 2:
        return list[0]
    # fortsett her

class Slide():
    def __init__(self, window, x, y, size):
        self.window = window
        self.x = x
        self.y = y
        self.size = size
        self.offset = None
        self.is_attached = False
        self.pos = []
        self.avg = None
        self.v = pg.math.Vector2(0,0)
    def draw(self):
        pg.draw.circle(self.window, (0,0,0), (self.x,self.y), self.size)
    def attach(self,px,py):
        v = pg.math.Vector2((self.x-px,self.y-py))
        if v.length() < self.size:
            self.offset = (self.x-px,self.y-py)
            self.is_attached = True
            if len(self.pos) > 5:
                self.pos.pop(0)
            self.pos.append((self.x,self.y)) # finn average
    def detach(self):
        self.offset = None
        self.is_attached = False
    def move(self,mx,my):
        if self.is_attached == True:
            x = self.x
            y = self.y
            self.x = mx + self.offset[0]
            self.y = my + self.offset[1]

    

slide = Slide(window,200,200,30)

pg.init()

contgame = True
while contgame == True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            contgame = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            slide.attach(event.pos[0],event.pos[1])
        elif event.type == pg.MOUSEBUTTONUP:
            slide.detach()
    window.fill((255,255,255))




    slide.draw()
    mx, my = pg.mouse.get_pos()
    slide.move(mx,my)

    pg.display.flip()
    clock.tick(60)

pg.quit()