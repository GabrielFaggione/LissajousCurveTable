
import pygame as pg
from settings import *
from sprites import *

class Game:
    def __init__(self):
        # initialize game window, etc
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH,HEIGHT), pg.FULLSCREEN)
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
    
    def new(self):
        # start a new game
        circleSize = int((WIDTH/(NUMCIRCLES+1)/2) - PADDING)
        edgePadding = circleSize
        speed = 0.01
        self.all_sprites = []
        self.pointDrawer = []
        self.pointCirclesX = []
        self.pointCirclesY = []
        for i in range(1, (NUMCIRCLES + 1)): # - gerador dos circle
            cx = Circle(self.screen, (edgePadding + (i*circleSize*2) + i*PADDING*2), circleSize + PADDING, circleSize)
            cpx = CirclePoint(self.screen, cx, speed)
            self.all_sprites.append(cx)
            self.all_sprites.append(cpx)
            self.pointCirclesX.append(cpx)

            cy = Circle(self.screen, circleSize + PADDING, (edgePadding + (i*circleSize*2) + i*PADDING*2), circleSize)
            cpy = CirclePoint(self.screen, cy, speed)
            self.all_sprites.append(cy)
            self.all_sprites.append(cpy)
            self.pointCirclesY.append(cpy)

            speed += 0.01
        
        for x in range(0,len(self.pointCirclesX)):
            for y in range(0,len(self.pointCirclesY)):
                cd = PointDrawer(self.screen, self.pointCirclesX[x], self.pointCirclesY[y])
                self.all_sprites.append(cd)
                self.pointDrawer.append(cd)
        self.run()
    
    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
    
    def update(self):
        for i in self.all_sprites:
            i.update()
        if self.pointCirclesX[0].angle >= 6:
            self.pointCirclesX[0].angle -= 6
            for cd in self.pointDrawer:
                cd.points = [cd.points[-1], (cd.x, cd.y)]
    
    def events(self):
        # Game loop - Events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing: self.playing = False
                self.running = False

    def draw(self):
        #Game Loop - Draw
        self.screen.fill(BLACK)
        for i in self.all_sprites:
            i.draw()
        pg.display.flip()
    
    def show_start_screen(self):
        # game splash/start screen
        pass
    
    def show_go_screen(self):
        pass


game = Game()
game.show_start_screen()
while game.running:
    game.new()
    game.show_go_screen()
pg.quit()


