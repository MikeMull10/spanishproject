import pygame
from math import *


class Post:
    def __init__(self, screen, x, y):
        self.win = screen
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.radius = 16
        self.gravity = .8

    def tick(self):
        self.x += self.dx
        self.y += self.dy
        self.dy += self.gravity
        if self.x <= self.radius or self.x >= 1280 - self.radius:
            self.dx = -self.dx
        if self.y <= self.radius or self.y >= 720 - self.radius:
            self.dy = -self.dy

    def draw(self):
        pygame.draw.circle(self.win, [0, 0, 0], (int(self.x), int(self.y)), self.radius)

    def collide(self, ball):
        cx, cy = 0, 0
        distance = sqrt((self.x - ball.x) ** 2 + (self.y - ball.y) ** 2)
        if distance <= 40:
            dx = self.x - ball.x
            dy = self.y - ball.y
            if dx == 0:
                return 0, 0
            angle = atan(dy / dx)
            if ball.dx > 10:
                cx = cos(angle) * 25
            else:
                cx = cos(angle) * (15 + ball.dx)
            if ball.dy > 10:
                cy = sin(angle) * 25
            else:
                cy = sin(angle) * (15 + ball.dy)
            if ball.x < self.x:
                cx = -abs(cx)
            elif ball.x > self.x:
                cx = abs(cx)
            if ball.y < self.y:
                cy = -abs(cx)
            elif ball.y > self.y:
                cy = abs(cx)
        return cx, cy
