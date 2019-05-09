from pygame.locals import *
from PlayerV2 import *
from Ball import *
from Post import *
from Button import *
import time

pygame.init()

width = 1280
height = int(width * 9 / 16)
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pok-A-Tok")
clock = pygame.time.Clock()
stadium = pygame.image.load('Stadium.png')
stadium_rect = stadium.get_rect()


def draw_fps(clock):
    basic_font = pygame.font.SysFont(None, 20)
    text = basic_font.render("FPS: " + str(round(clock.get_fps(), 2)), True, (0, 0, 0))
    textrect = text.get_rect()
    textrect.centerx = 50
    textrect.centery = 20
    win.blit(text, textrect)


def draw_scores(s1, s2):
    basic_font = pygame.font.SysFont(None, 30)
    text = basic_font.render("Jugador 1: " + str(s1), True, (255, 0, 0))
    textrect = text.get_rect()
    textrect.centerx = 320
    textrect.centery = 20
    win.blit(text, textrect)
    text = basic_font.render("Jugador 2: " + str(s2), True, (0, 0, 255))
    textrect = text.get_rect()
    textrect.centerx = 960
    textrect.centery = 20
    win.blit(text, textrect)


def instruc():
    running = True
    back = Button(win, 10, 650, "BACK", 0)
    while running:
        pygame.draw.rect(win, [255, 255, 255], [0, 0, width, height], 0)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                running = False
        mx, my = pygame.mouse.get_pos()
        if back.clicked(mx, my) and pygame.mouse.get_pressed()[0]:
            menu()
        pygame.display.update()
    pygame.quit()


def menu():
    running = True
    buttons = []
    start = Button(win, 540, 200, "EMPEZAR", 1)
    instructions = Button(win, 540, 275, "INSTRUCIONES", 2)
    buttons.append(start)
    buttons.append(instructions)
    while running:
        pygame.draw.rect(win, [255, 255, 255], [0, 0, width, height], 0)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                running = False
        mx, my = pygame.mouse.get_pos()
        for button in buttons:
            button.draw()
            if button.clicked(mx, my) and pygame.mouse.get_pressed()[0]:
                if button.function == 0:
                    game()
                elif button.function == 1:
                    instruc()
                pygame.quit()
        pygame.display.update()
    pygame.quit()


def game():
    p1 = Player(win, 200, 500, 1, "right")
    p2 = Player(win, width - 200, 500, 2, "left")
    posts = []
    posts.append(Post(win, 640, 50))
    posts.append(Post(win, 640, 175))
    ball = Ball(win, width / 2, 200)
    ball.start()
    score1, score2 = 0, 0
    running = True
    while running:
        clock.tick(15)
        pygame.draw.rect(win, [255, 255, 255], [0, 0, width, height], 0)
        win.blit(stadium, stadium_rect)
        draw_fps()
        draw_scores(score1, score2)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return
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
        dx, dy = p1.collide(ball)
        if dx != 0 or dy != 0:
            ball.dx = dx
            ball.dy = dy
            ball.team = 0
        else:
            dx, dy = p2.collide(ball)
            if dx != 0 or dy != 0:
                ball.dx = dx
                ball.dy = dy
                ball.team = 1
            else:
                p1.body_collide(ball)
                p2.body_collide(ball)
        p1.draw()
        p1.tick()
        p2.draw()
        p2.tick()
        ball.tick()
        ball.draw()
        for post in posts:
            post.draw()
            cx, cy = post.collide(ball)
            if cx != 0 or cy != 0:
                ball.dx = cx
                ball.dy = cy
        if 630 <= ball.x <= 650 and 81 <= ball.y <= 119 + 25:
            basic_font = pygame.font.SysFont(None, 60)
            if ball.team == 0:
                score1 += 1
                text = basic_font.render("¡Jugador 1 anotó!", True, (255, 0, 0))
            elif ball.team == 1:
                score2 += 1
                text = basic_font.render("¡Jugador 2 anotó!", True, (0, 0, 255))
            ball.start()
            p1.reset()
            p2.reset()
            pygame.draw.rect(win, [0, 0, 0], (624, 50, 32, 125), 0)
            textrect = text.get_rect()
            textrect.centerx = 640
            textrect.centery = 360
            win.blit(text, textrect)
            pygame.display.update()
            time.sleep(2)
        pygame.draw.rect(win, [0, 0, 0], (640 - 16, 50, 32, 125), 0)
        pygame.display.update()
    pygame.quit()


while True:
    menu()
