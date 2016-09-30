from pygamehelper import *
from pygame import *
from pygame.locals import *
from math import e, pi, cos, sin, sqrt
from random import uniform
from random import randint
import Grid
FPS = 110
RED = (255,0,0)
BLUE = (0,0,255),
COLORS = [RED, BLUE]
class MineSweeper(PygameHelper):
    def __init__(self,ms = 0,sec = 0,minute = 0,hour = 0,n=0,state = "start"):
        self.state = "start"
        self.sizex = 10
        self.sizey = 10
        self.w, self.h = 1300,600#1915, 1000
        self.bkg_color =(0,0,0)#COLORS[randint(0,len(COLORS))]
        PygameHelper.__init__(self, size=(self.w, self.h), fill=(self.bkg_color))
        self.grid = Grid.Grid(self.sizex,self.sizey)
        self.myfont = pygame.font.SysFont("TimeBurner", 75)
        self.myfont1 = pygame.font.SysFont("TimeBurner", 30)

    def update(self):
        if self.state == "game":
            if self.grid.check():
                self.state = "end1"
            if self.grid.over == True:
                self.state = "end"
        
    def keyUp(self,key):
        pass
    def mouseUp(self, button, pos):
        if self.state == "start":
            if button == 1:
                if pos[0] >290 and pos[0]<290+61 and pos[1] >400 and pos[1]<440:
                    self.state = "game"
                if pos[0] >590 and pos[0]<590+101 and pos[1] >400 and pos[1]<440:
                    self.grid1 = Grid.Grid(16,16)
                    self.grid = self.grid1
                    self.state = "game"
                if pos[0] >890 and pos[0]<890+63 and pos[1] >400 and pos[1]<440:
                    print True
                    self.grid1 = Grid.Grid(30,16)
                    self.grid = self.grid1
                    self.state = "game"
                
        elif self.state == "game":
            if self.grid.num_col == 10 or self.grid.num_col == 16:
                if button == 1:
                    x = pos[0]-300
                    y = pos[1]
                    p = [x,y]
                    self.grid.reveal(p)
                elif button == 3:
                    x = pos[0]-300
                    y = pos[1]
                    p = [x,y]
                    self.grid.flag(p)
                elif button == 2:
                    self.grid.reset()
            else:
                if button == 1:
                    self.grid.reveal(pos)
                elif button == 3:
                    self.grid.flag(pos)
        elif self.state == "end" or self.state == "end1":
            if button == 1:
                self.grid.reset()
                self.state = "game"
    def draw(self):
        if self.state == "start":
            self.screen.fill((0,0,0))
            self.label = self.myfont.render("Minesweeper", 0, (255,0,0))
            self.screen.blit(self.label,(self.w/2-self.label.get_width()/2,self.h/2-self.label.get_height()/2))
            self.easy = self.myfont1.render("Easy",0,(255,255,255))
            self.screen.blit(self.easy, (290, 400))
            self.medium = self.myfont1.render("Medium", 0,(255,255,255))
            self.screen.blit(self.medium, (590,400))
            self.hard = self.myfont1.render("Hard", 0, (255,255,255))
            self.screen.blit(self.hard, (890,400))
        elif self.state == "game":
            self.screen.fill(self.bkg_color)
            self.grid.draw(self.screen)
        elif self.state == "end":
            self.screen.fill((0,0,0))
            self.label = self.myfont.render("YOU LOSE", 0, (255,0,0))
            self.label2 = self.myfont1.render("click anywhere to try again",0,(255,255,255))
            self.screen.blit(self.label,(self.w/2-self.label.get_width()/2,self.h/2-self.label.get_height()/2))
            self.screen.blit(self.label2, (self.w/2-self.label.get_width()/2,400))
        elif self.state == "end1":
            self.screen.fill((0,0,0))
            self.label = self.myfont.render("Congratulations", 0, (255,255,255))
            self.screen.blit(self.label,(self.w/2-self.label.get_width()/2,self.h/2-self.label.get_height()/2))
            
s = MineSweeper()
s.mainLoop(FPS)
  