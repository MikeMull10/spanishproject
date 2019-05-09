from Variables import *


def draw_winner(win, p1, score, frame, morir):
    basic_font = pygame.font.SysFont(None, 80)
    if p1 >= score:
        winner = 1
        r = 255
        b = 0
    else:
        winner = 2
        r = 0
        b = 255
        win.blit(body_blue, ir_bb)
        win.blit(head_blue, ir_hb)
    text = basic_font.render("¡Jugador %s gana!" % winner, True, (r, 0, b))
    textrect = text.get_rect()
    textrect.centerx = 640
    textrect.centery = 180
    win.blit(text, textrect)
    if winner == 1:
        try:
            if morir:
                win.blit(body_red, ir_br)
                win.blit(head_red, ir_hr)
            else:
                win.blit(body_blue, ir_bb)
                win.blit(head_blue, ir_hb)
        except:
            return
    elif winner == 2:
        try:
            if morir:
                win.blit(body_blue, ir_bb)
                win.blit(head_blue, ir_hb)
            else:
                win.blit(body_red, ir_br)
                win.blit(head_red, ir_hr)
        except:
            return
    if frame <= 20:
        body_x = x
        body_y = y
    else:
        body_y = (frame - 20) ** 2 + 400
        body_x = 10 * (frame - 20) + 600
    ir_hr.centerx = body_x
    ir_hr.centery = body_y
    ir_hb.centerx = body_x
    ir_hb.centery = body_y


def draw_fps(win, clock):
    basic_font = pygame.font.SysFont(None, 20)
    text = basic_font.render("FPS: " + str(round(clock.get_fps(), 2)), True, BLACK)
    textrect = text.get_rect()
    textrect.centerx = 50
    textrect.centery = 20
    win.blit(text, textrect)


def draw_scores(win, s1, s2):
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


def draw_title(win, title):
    basic_font = pygame.font.SysFont(None, 80)
    text = basic_font.render(title, True, ORANGE)
    textrect = text.get_rect()
    textrect.centerx = 640
    textrect.centery = 50
    win.blit(text, textrect)


def draw_background(win):
    win.blit(background, background_rect)


def draw_game_title(win):
    win.blit(title, title_rect)


def draw_works_cited(win):
    y = 200
    for link in links:
        basic_font = pygame.font.SysFont(None, 30)
        text = basic_font.render(link, True, BLACK)
        textrect = text.get_rect()
        textrect.centerx = 640
        textrect.centery = y
        win.blit(text, textrect)
        y += 50


def draw_subtitle(win, sub_title):
    basic_font = pygame.font.SysFont(None, 25)
    text = basic_font.render(sub_title, True, BLACK)
    textrect = text.get_rect()
    textrect.centerx = 640
    textrect.centery = 175
    win.blit(text, textrect)


def draw_settings(win):
    win.blit(settings, settings_rect)


def draw_text(win, text, c_x, c_y, size):
    basic_font = pygame.font.SysFont(None, size)
    text = basic_font.render(text, True, BLACK)
    text_rect = text.get_rect()
    text_rect.centerx = c_x
    text_rect.centery = c_y
    win.blit(text, text_rect)


def draw_instructions(win):
    win.blit(instructions, instructions_rect)


def draw_history(win):
    win.blit(history, history_rect)
