from pygamehelper import *
from pygame import *
from random import randint


grid = 4
size = 500
width = size/grid


class Pic:
    def __init__(self):
        self.Image = "codeday.jpg"
        self.raw = pygame.image.load(self.Image).convert()
        self.picture = pygame.transform.scale(self.raw,(size,size))
        self.w = self.picture.get_width()
        self.h = self.picture.get_height()
        self.l = []       
        self.copy = []
        self.move_count = 0
        for y in range(grid):
            for x in range(grid):
                cropped = pygame.Surface((width, width))
                cropped.blit(self.picture, (0, 0), (x*width, y*width, width-2, width-2))
                self.l.append(cropped)
                self.copy.append(cropped)
        self.blank = pygame.Surface((width,width))
        self.l[len(self.l)-1] = self.blank
        self.copy[len(self.copy)-1] = self.blank        
        
    def piece_pos(self,pos):
        x = (pos[0]/width)+1
        y = pos[1]/width
        piece = y*grid + x         
        return piece

    def move(self,pos=None):
        blank = self.l.index(self.blank)
        piece = self.piece_pos(pos)
        if self.check(piece):            
            a = self.l[piece-1]
            self.l[piece-1] = self.blank
            self.l[blank] = a
            self.move_count += 1
        
    def check(self,i):
        blank = self.l.index(self.blank)+1
        if abs(i-blank) == 1:
            return True
        elif blank + grid == i or blank-grid == i:
            return True
        return False

    def draw(self, screen):
        for y in range(grid):
            for x in range(grid):
                screen.blit(self.l[x+y*grid], [width*x, width*y])
        return screen
    
