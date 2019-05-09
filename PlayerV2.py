from Hitbox import *
from Body import *

amt = 20


class Player:
    def __init__(self, screen, x, y, team, facing):
        self.startX = x
        self.startY = y
        self.win = screen
        self.x = x
        self.y = y
        self.team = team
        self.facing = facing
        self.timer = 0
        if team == 1:
            self.left = pygame.image.load('Mayan Left Red.png')
            self.right = pygame.image.load('Mayan Right Red.png')
        else:
            self.left = pygame.image.load('Mayan Left Blue.png')
            self.right = pygame.image.load('Mayan Right Blue.png')
        self.imagerectL = self.left.get_rect()
        self.imagerectR = self.right.get_rect()

        self.canJump = False
        self.falling = False
        self.gravity = 1

        self.dy = 0
        self.maxDY = 10

        self.body = ""
        self.hit_box = ""

        self.body_timer = 0

        self.update()

    def reset(self):
        self.dy = 0
        self.canJump = False
        self.falling = False
        self.x = self.startX
        self.y = self.startY

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

        if self.facing == 'left':
            self.hit_box = Hitbox(self.win, self.x + 27, self.y + 25, 25)
            self.body = Body(self.x + 24, self.y + 50, 40, 100)
        elif self.facing == 'right':
            self.hit_box = Hitbox(self.win, self.x + 52, self.y + 25, 25)
            self.body = Body(self.x + 15, self.y + 50, 40, 100)
        # pygame.draw.rect(self.win, [0, 0, 0], (self.body.x, self.body.y, self.body.width, self.body.height), 0)

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

    def collide(self, ball):
        return self.hit_box.collide(ball)

    def body_collide(self, ball, team):
        if self.body.x - 15 <= ball.x <= self.body.x + self.body.width + 15 and self.body.y <= ball.y <= self.body.y + \
                self.body.height + 15 and self.body_timer == 0:
            ball.team = team
            ball.dx = -ball.dx
            ball.dy -= 5
            self.body_timer += 1
        if self.body_timer != 0:
            self.body_timer = (self.body_timer + 1) % 4
