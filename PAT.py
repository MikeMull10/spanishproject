from pygame.locals import *
from PlayerV2 import *
from Ball import *
from Post import *
from Setting import *
from Draw import *
from Music import *
import time

pygame.init()

width = 1280
height = int(width * 9 / 16)
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pok-A-Tok")
clock = pygame.time.Clock()
stadium = pygame.image.load('Stadium.png')
stadium_rect = stadium.get_rect()


def main():
    s = Sound()
    p1 = Player(win, 200, 500, 1, "right")
    p2 = Player(win, width - 200, 500, 2, "left")
    posts = []
    posts.append(Post(win, 640, 65))
    posts.append(Post(win, 640, 190))
    ball = Ball(win, width / 2, 225)
    ball.start()
    score1, score2 = 0, 0
    running = True
    screen = 0
    frame = 0
    play_to = 5
    buttons = []
    start = Button(win, 565, 200, "EMPEZAR", 1, ORANGE, BLACK)
    instructions = Button(win, 565, 275, "INSTRUCIÓNES", 2, ORANGE, BLACK)
    background = Button(win, 565, 350, "LA HISTORIA", 3, ORANGE, BLACK)
    works_cited = Button(win, 565, 425, "REFERENCIAS", 4, ORANGE, BLACK)
    back = Button(win, 10, 660, "ATRÁS", 0, [255, 255, 255], BLACK)
    yes_1 = Setting(win, 720, 275, "Si", "", ORANGE, BLACK, True)
    no_1 = Setting(win, 900, 275, "No", "", ORANGE, BLACK, False)
    p_1 = Setting(win, 510, 350, "1", "", ORANGE, BLACK, False)
    p_2 = Setting(win, 660, 350, "2", "", ORANGE, BLACK, False)
    p_3 = Setting(win, 810, 350, "3", "", ORANGE, BLACK, False)
    p_4 = Setting(win, 960, 350, "4", "", ORANGE, BLACK, False)
    p_5 = Setting(win, 1110, 350, "5", "", ORANGE, BLACK, True)
    buttons.append(start)
    buttons.append(instructions)
    buttons.append(background)
    buttons.append(works_cited)
    while running:
        clock.tick(15)
        s.play()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            running = False
        pygame.draw.rect(win, [255, 255, 255], [0, 0, width, height], 0)
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        if screen == 5:
            win.blit(stadium, stadium_rect)
            draw_winner(win, score1, play_to, frame, yes_1.selected)
            frame = (frame + 1) % 60
            if frame == 0:
                screen = 0
                score1, score2 = 0, 0
            pygame.display.update()
        elif screen == 6:
            mx, my = pygame.mouse.get_pos()
            draw_title(win, "AJUSTES")
            draw_text(win, "Ganador Morir", 320, 300, 60)
            draw_text(win, "Jugar A...", 260, 375, 60)
            back.draw()
            yes_1.draw()
            no_1.draw()
            p_1.draw()
            p_2.draw()
            p_3.draw()
            p_4.draw()
            p_5.draw()
            if yes_1.clicked(mx, my) and pygame.mouse.get_pressed()[0]:
                yes_1.selected = True
                no_1.selected = False
            elif no_1.clicked(mx, my) and pygame.mouse.get_pressed()[0]:
                yes_1.selected = False
                no_1.selected = True
            if p_1.clicked(mx, my) and pygame.mouse.get_pressed()[0]:
                p_1.selected = True
                p_5.selected = False
                p_2.selected = False
                p_3.selected = False
                p_4.selected = False
            elif p_2.clicked(mx, my) and pygame.mouse.get_pressed()[0]:
                p_2.selected = True
                p_1.selected = False
                p_5.selected = False
                p_3.selected = False
                p_4.selected = False
            elif p_3.clicked(mx, my) and pygame.mouse.get_pressed()[0]:
                p_3.selected = True
                p_1.selected = False
                p_2.selected = False
                p_5.selected = False
                p_4.selected = False
            elif p_4.clicked(mx, my) and pygame.mouse.get_pressed()[0]:
                p_4.selected = True
                p_1.selected = False
                p_2.selected = False
                p_3.selected = False
                p_5.selected = False
            elif p_5.clicked(mx, my) and pygame.mouse.get_pressed()[0]:
                p_5.selected = True
                p_1.selected = False
                p_2.selected = False
                p_3.selected = False
                p_4.selected = False
            if p_1.selected:
                play_to = 1
            elif p_2.selected:
                play_to = 2
            elif p_3.selected:
                play_to = 3
            elif p_4.selected:
                play_to = 4
            else:
                play_to = 5
            if back.clicked(mx, my) and pygame.mouse.get_pressed()[0]:
                screen = 0
            pygame.display.update()
        elif screen == 0:  # Main Screen
            draw_background(win)
            draw_game_title(win)
            draw_subtitle(win, "Un Partido de Los Mayas")
            draw_settings(win)
            mx, my = pygame.mouse.get_pos()
            if mx >= 1240 and my >= 680 and pygame.mouse.get_pressed()[0]:
                screen = 6
            for button in buttons:
                button.draw()
                if button.clicked(mx, my) and pygame.mouse.get_pressed()[0]:
                    screen = button.function
                    break
            pygame.display.update()
        elif screen == 4:  # Works Cited Tab
            draw_title(win, "REFERENCIAS")
            draw_works_cited(win)
            back.draw()
            mx, my = pygame.mouse.get_pos()
            if back.clicked(mx, my) and pygame.mouse.get_pressed()[0]:
                screen = 0
            pygame.display.update()
        elif screen == 2:  # Instructions Tab
            draw_title(win, "INSTRUCIÓNES")
            draw_instructions(win)
            back.draw()
            mx, my = pygame.mouse.get_pos()
            if back.clicked(mx, my) and pygame.mouse.get_pressed()[0]:
                screen = 0
            pygame.display.update()
        elif screen == 3:  # Background Info Tab
            draw_title(win, "LA HISTORIA")
            back.draw()
            draw_history(win)
            mx, my = pygame.mouse.get_pos()
            if back.clicked(mx, my) and pygame.mouse.get_pressed()[0]:
                screen = 0
            pygame.display.update()
        elif screen == 1:
            win.blit(stadium, stadium_rect)
            draw_fps(win, clock)
            draw_scores(win, score1, score2)
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
            p1.draw()
            p1.tick()
            p2.draw()
            p2.tick()
            for post in posts:
                cx, cy = post.collide(ball)
                if cx != 0 or cy != 0:
                    ball.dx = cx
                    ball.dy = cy
            for i in range(10):
                ball.move()
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
                        p1.body_collide(ball, 0)
                        p2.body_collide(ball, 1)
                if 630 <= ball.x <= 650 and 81 + 15 <= ball.y <= 119 + 40:
                    basic_font = pygame.font.SysFont(None, 60)
                    for post in posts:
                        post.draw()
                    if ball.team == 0:
                        score1 += 1
                        text = basic_font.render("¡Jugador 1 anotó!", True, (255, 0, 0))
                    elif ball.team == 1:
                        score2 += 1
                        text = basic_font.render("¡Jugador 2 anotó!", True, (0, 0, 255))
                    if score1 == play_to or score2 == play_to:
                        screen = 5
                    ball.start()
                    p1.reset()
                    p2.reset()
                    pygame.draw.rect(win, BLACK, (624, 65, 32, 125), 0)
                    textrect = text.get_rect()
                    textrect.centerx = 640
                    textrect.centery = 360
                    win.blit(text, textrect)
                    ball.draw()
                    pygame.display.update()
                    time.sleep(2)
            ball.tick()
            ball.draw()
            for post in posts:
                post.draw()
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
                    p1.body_collide(ball, 0)
                    p2.body_collide(ball, 1)
            if 630 <= ball.x <= 650 and 96 <= ball.y <= 159:
                basic_font = pygame.font.SysFont(None, 60)
                if ball.team == 0:
                    score1 += 1
                    text = basic_font.render("¡Jugador 1 anotó!", True, (255, 0, 0))
                elif ball.team == 1:
                    score2 += 1
                    text = basic_font.render("¡Jugador 2 anotó!", True, (0, 0, 255))
                if score1 == play_to or score2 == play_to:
                    screen = 5
                ball.start()
                p1.reset()
                p2.reset()
                pygame.draw.rect(win, BLACK, (624, 65, 32, 125), 0)
                textrect = text.get_rect()
                textrect.centerx = 640
                textrect.centery = 360
                win.blit(text, textrect)
                ball.draw()
                pygame.display.update()
                time.sleep(2)
            pygame.draw.rect(win, BLACK, (624, 65, 32, 125), 0)
            pygame.display.update()
    pygame.quit()


main()
