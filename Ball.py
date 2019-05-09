import pygame
from random import *
from math import *


class Ball:
    def __init__(self, screen, x, y):
        self.win = screen
        self.startX = x
        self.startY = y
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.radius = 15
        self.gravity = .8
        self.fell = False
        self.team = None

    def move(self):
        self.x += self.dx / 10
        self.y += self.dy / 10

    def tick(self):
        self.dy += self.gravity
        if self.x <= self.radius:
            self.dx = -self.dx
            self.x = 15
        elif self.x >= 1280 - self.radius:
            self.dx = -self.dx
            self.x = 1265
        if self.y <= self.radius:
            self.dy = -self.dy
            self.y = 15
        elif self.y >= 720 - self.radius:
            self.dy = -self.dy * 4 / 5
            self.y = 720 - self.radius
            self.fell = True

    def draw(self):
        pygame.draw.circle(self.win, [64, 64, 64], (int(self.x), int(self.y)), self.radius)
        if self.team == 0:
            pygame.draw.circle(self.win, [255, 0, 0], (int(self.x), int(self.y)), self.radius, 2)
        elif self.team == 1:
            pygame.draw.circle(self.win, [0, 0, 255], (int(self.x), int(self.y)), self.radius, 2)

    def start(self):
        self.x = self.startX
        self.y = self.startY
        self.team = None
        angle = randint(0, 314) + 113
        self.dx = cos(radians(angle)) * 10
        self.dy = sin(radians(angle)) * 10
