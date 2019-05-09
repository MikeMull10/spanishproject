from Hitbox import *

amt = 20


class Player:
    def __init__(self, screen, x, y, team, facing):
        self.win = screen
        self.x = x
        self.y = y
        self.team = team
        self.facing = facing
        self.timer = 0
        self.left = pygame.image.load('Mayan Left.png')
        self.right = pygame.image.load('Mayan Right.png')
        self.imagerectL = self.left.get_rect()
        self.imagerectR = self.right.get_rect()

        self.canJump = False
        self.falling = False
        self.gravity = 1

        self.dx = 0
        self.dy = 0
        self.maxDY = 10

        self.hit_box = ""

        self.update()

    def draw(self):
        if self.facing == "left":
            self.win.blit(self.left, self.imagerectL)
        else:
            self.win.blit(self.right, self.imagerectR)

    def tick(self):
        self.fall()
        self.y += self.dy
        if self.x < 0:
            self.x = 0
        elif self.x > 1201:
            self.x = 1201
        if self.y < 563:
            self.falling = True
        else:
            self.y = 563
            self.dy = 0
            self.falling = False
            self.canJump = True
        self.update()

    def update(self):
        self.imagerectR.centerx = int(self.x) + int(79 / 2)
        self.imagerectR.centery = int(self.y) + int(157 / 2)
        self.imagerectL.centerx = int(self.x) + int(79 / 2)
        self.imagerectL.centery = int(self.y) + int(157 / 2)

    def move(self, d):
        div = 1.5
        if not self.canJump:
            div = 2
        if d == "left":
            self.x -= amt / div
        elif d == "right":
            self.x += amt / div
        elif d == "up":
            self.jump(20)

    def fall(self):
        if self.falling:
            self.dy += self.gravity
            if self.dy > self.maxDY:
                self.dy = self.maxDY

    def jump(self, jump_height):
        if self.canJump:
            self.dy -= jump_height
            self.canJump = False
