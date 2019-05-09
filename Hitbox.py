import pygame
from math import *


class Hitbox:
    def __init__(self, screen, x, y, r):
        self.x = x
        self.y = y
        self.radius = r
        self.win = screen

    def draw(self):
        pygame.draw.circle(self.win, [0, 0, 0], (int(self.x), int(self.y)), self.radius)

    def collide(self, ball):
        cx, cy = 0, 0
        distance = sqrt((self.x - ball.x)**2 + (self.y - ball.y)**2)
        if distance <= 40:
            dx = self.x - ball.x
            dy = self.y - ball.y
            angle = atan(dy / dx)
            cx = cos(angle) * 30
            cy = sin(angle) * 30
            if ball.x < self.x:
                cx = -abs(cx)
            elif ball.x > self.x:
                cx = abs(cx)
            if ball.y < self.y:
                cy = -abs(cx)
            elif ball.y > self.y:
                cy = abs(cx)
        return cx, cy
