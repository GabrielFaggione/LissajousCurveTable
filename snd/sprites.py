# Sprite classes
from settings import *
from random import randint
from math import sin, cos, pi
import pygame as pg

vec = pg.math.Vector2

class Circle():
    def __init__(self, gameSurface, x, y, size):
        self.surface = gameSurface
        self.x = x
        self.y = y
        self.size = size
    
    def draw(self):
        pg.draw.circle(self.surface, WHITE, (self.x, self.y), self.size, 1)
    
    def update(self):
        pass

class CirclePoint():
    def __init__(self, gameSurface, circleReference, speed):
        self.surface = gameSurface
        self.circle = circleReference
        self.angle = 0
        self.x = int(self.circle.size * cos(self.angle)) + self.circle.x
        self.y = int(self.circle.size * sin(self.angle)) + self.circle.y
        self.speed = speed

    def draw(self):
        pg.draw.circle(self.surface, WHITE, (self.x, self.y), 5)
    
    def update(self):
        self.angle += self.speed
        self.x = int(self.circle.size * cos(self.angle)) + self.circle.x
        self.y = int(self.circle.size * sin(self.angle)) + self.circle.y

class PointDrawer():
    def __init__(self, gameSurface, refx, refy):
        self.surface = gameSurface
        self.circleX = refx
        self.circleY = refy
        self.x = self.circleX.x
        self.y = self.circleY.y
        self.points = []
        self.points.append((self.x, self.y))
        self.red = 0
        self.green = 0
        self.blue = 0
    
    def draw(self):
        pg.draw.circle(self.surface, (self.red, self.green, self.blue), (self.x, self.y), 5)
        pg.draw.aalines(self.surface, WHITE, False, self.points, 2)
         
    
    def update(self):
        self.x = self.circleX.x
        self.y = self.circleY.y
        self.points.append((self.x, self.y))
        self.red = randint(0,255)
        self.green = randint(0,255)
        self.blue = randint(0,255)


