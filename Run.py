import pymunk
import pymunk.util
import pymunk.pygame_util
from pygame.locals import *
from Player import *
from Ball import *
from Button import *
from pymunk import Vec2d
import math, sys, random

space = pymunk.Space()
pygame.init()
width = 1280
height = int(width * 9 / 16)
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pok-A-Tok")
clock = pygame.time.Clock()
draw_options = pymunk.pygame_util.DrawOptions(win)

screen = 0


def update_heads(p1, p2):
    if len(space.bodies) > 4:
        b1 = space.bodies[0]
        b2 = space.bodies[1]
        b3 = space.bodies[2]
        space.bodies.clear()
        space.add(b1)
        space.add(b2)
        space.add(b3)
    mass = 10
    radius = 25
    inertia = pymunk.moment_for_circle(mass, 0, radius, (0, 0))
    body = pymunk.Body(mass, inertia)
    body.position = p1.x, p1.y
    shape = pymunk.Circle(body, radius, (0, 0))
    shape.elasticity = 0.95
    shape.friction = 0
    space.add(body, shape)
    mass = 10
    radius = 25
    inertia = pymunk.moment_for_circle(mass, 0, radius, (0, 0))
    body = pymunk.Body(mass, inertia)
    body.position = p2.x, p2.y
    shape = pymunk.Circle(body, radius, (0, 0))
    shape.elasticity = 0.95
    shape.friction = 0
    space.add(body, shape)


def draw_fps():
    basic_font = pygame.font.SysFont(None, 20)
    text = basic_font.render("FPS: " + str(round(clock.get_fps(), 2)), True, (0, 0, 0), (255, 255, 255))
    textrect = text.get_rect()
    textrect.centerx = 50
    textrect.centery = 20
    win.blit(text, textrect)


def draw_hoop():
    pygame.draw.circle(win, [0, 0, 0], (640, 150), 15)
    pygame.draw.circle(win, [0, 0, 0], (640, 50), 15)
    pygame.draw.rect(win, [0, 0, 0], (625, 50, 30, 100), 0)


def add_ball():
    mass = 10
    radius = 15
    inertia = pymunk.moment_for_circle(mass, 0, radius, (0, 0))
    body = pymunk.Body(mass, inertia)
    x = random.randint(115, 350)
    body.position = x, 400
    shape = pymunk.Circle(body, radius, (0, 0))
    shape.elasticity = 0.95
    shape.friction = 0.9
    space.add(body, shape)
    mass = 10
    inertia = pymunk.moment_for_circle(mass, 0, 10, (0, 0))
    body = pymunk.Body(mass, inertia)
    body.position = 640, 720 - 150
    shape = pymunk.Circle(body, radius, (0, 0))
    shape.elasticity = 0.95
    shape.friction = 0.9
    space.add(body, shape)
    mass = 10
    inertia = pymunk.moment_for_circle(mass, 0, 10, (0, 0))
    body = pymunk.Body(mass, inertia)
    body.position = 640, 720 - 50
    shape = pymunk.Circle(body, radius, (0, 0))
    shape.elasticity = 0.95
    shape.friction = 0.9
    space.add(body, shape)
    body = pymunk.Body(1, 1666)
    body.position = 50, 100
    poly = pymunk.Poly.create_box(body)
    space.add(body, poly)


def game():
    running = True
    add_ball()
    p1 = Player(win, 200, 500, 1, "right")
    p2 = Player(win, width - 200, 500, 2, "left")
    while running:
        clock.tick(15)
        if clock.get_fps() != 0:
            space.step(1 / clock.get_fps())
        pygame.draw.rect(win, [255, 255, 255], [0, 0, width, height], 0)
        draw_fps()
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        space.debug_draw(draw_options)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            p1.move("left")
            p1.facing = "left"
        elif keys[pygame.K_d]:
            p1.move("right")
            p1.facing = "right"
        if keys[pygame.K_w]:
            p1.move("up")
        if keys[pygame.K_LEFT]:
            p2.move("left")
            p2.facing = "left"
        elif keys[pygame.K_RIGHT]:
            p2.move("right")
            p2.facing = "right"
        if keys[pygame.K_UP]:
            p2.move("up")
        if keys[pygame.K_ESCAPE]:
            running = False
        p1.draw()
        p1.tick()
        p2.draw()
        p2.tick()
        draw_hoop()
        #update_heads(p1, p2)
        pygame.display.update()
    pygame.display.quit()


def main():
    running = True
    buttons = []
    start = Button(win, 540, 200, "EMPEZAR", 0)
    instructions = Button(win, 540, 275, "INSTRUCIONES", 1)
    buttons.append(start)
    buttons.append(instructions)
    while running:
        pygame.draw.rect(win, [255, 255, 255], [0, 0, width, height], 0)
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        mx, my = pygame.mouse.get_pos()
        for button in buttons:
            button.draw()
            if button.clicked(mx, my) and pygame.mouse.get_pressed()[0]:
                return
                game()
        pygame.display.update()
    pygame.display.quit()


main()
game()
