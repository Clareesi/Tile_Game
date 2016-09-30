from pygamehelper import *
from pygame import *
from pic import *
import time

FPS = 20


class Tiles_Game(PygameHelper):
    count = 0
    def __init__(self):
        self.state = "start"
        self.w, self.h = 1100, 500
        self.bkg_color = (0,0,0)
        PygameHelper.__init__(self, size = (self.w, self.h), fill = (self.bkg_color))
        pygame.mixer.music.load("Boston.mp3")
        self.i = Pic()
        self.ms = 0
        self.sec = 0
        self.m = 0
        self.scramble = None
        self.picture = pygame.image.load(self.i.Image).convert()
        self.myfont = pygame.font.SysFont("TimeBurner",100)
        self.myfontsmall = pygame.font.SysFont("TimeBurner", 15)
        pygame.mixer.music.play(-1)
        
    def mouseUp(self, buttons, pos):
        if self.state == "start":
            if buttons == 1:
                self.state = "game"
                self.start_time = time.time()
                self.scramble = True
        elif self.state == "game":         
            if buttons == 1:
                self.scramble = False
                self.i.move(pos)
                
    def update(self):
        possible=[]
        piece = 0
        Tiles_Game.count += 1
        if self.scramble:
            if Tiles_Game.count%2 == 0:
                for i in range(1):
                    blank = self.i.l.index(self.i.blank)
                    if blank<11 and blank>4 and blank%4 !=3 and blank%4!=0:
                        possible = [blank+1,blank-1,blank+4,blank-4]
                    elif blank >11 and blank%4==3:
                        possible = [blank-1,blank-4]
                    elif blank>11 and blank%4==0:
                        possible = [blank+1,blank-4]
                    elif blank<4 and blank%4==3:
                        possible = [blank-1,blank+4]
                    elif blank < 4 and blank%4 == 0:
                        possible = [blank+1, blank+4]
                    elif blank > 11:
                        possible = [blank+1, blank-1, blank-4]
                    elif blank < 4:
                        possible = [blank+1, blank-1, blank+4]
                    elif blank%4==3:
                        possible = [blank-1, blank+4,blank-4]
                    elif blank%4==0:
                        possible = [blank+1, blank+4,blank-4]
                    piece = randint(0,len(possible)-1)
                    if self.i.check(possible[piece]+1):            
                        a = self.i.l[possible[piece]]
                        self.i.l[possible[piece]] = self.i.blank
                        self.i.l[blank] = a          
        else:
            if self.state == "game":
                self.ms += 1
                if self.ms >= 60:
                    self.sec += 1
                    self.ms = 0
                if self.sec >= 60:
                    self.m += 1
                    self.sec = 0
            if self.i.copy == self.i.l and self.i.move_count>3:
                self.state = "end"
                pygame.mixer.music.fadeout(500)   
                
    def draw(self):
        if self.state == "start":
            self.label = self.myfont.render("Tile Game", 0, (255,255,255))
            self.screen.blit(self.label,(self.w/2-self.label.get_width()/2,self.h/2-self.label.get_height()/2))
        elif self.state == "game":
            self.screen.fill(self.bkg_color)
            self.i.draw(self.screen)
            self.screen.blit(self.i.picture, [600,0])
            self.moves = self.myfontsmall.render("Moves:%d" %self.i.move_count, 0, (255,255,255))
            self.screen.blit(self.moves, (550-self.moves.get_width()/2, self.h/2-self.moves.get_height()))
            self.t = self.myfontsmall.render("Time:%d:%d:%d" %(self.m, self.sec, self.ms), 0, (255,255,255))
            self.screen.blit(self.t, (550-self.t.get_width()/2, self.h/2))
        elif self.state == "end":
            self.screen.fill(self.bkg_color)
            self.end_label = self.myfont.render("You Win", 0, (255,255,255))
            self.screen.blit(self.end_label, (self.w/2-self.end_label.get_width()/2, self.h/2-self.end_label.get_height()/2))
            self.screen.blit(self.moves, (550-self.moves.get_width()/2, self.h/4-self.moves.get_height()))
            self.screen.blit(self.t, (550-self.t.get_width()/2, self.h*3/4))

            
        
        
s = Tiles_Game()
s.mainLoop(FPS)