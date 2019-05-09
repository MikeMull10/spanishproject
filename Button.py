import pygame


class Button:
    def __init__(self, win, x, y, txt, function, color, txt_color):
        self.x = x
        self.y = y
        self.win = win
        self.text = txt
        self.function = function
        self.color = color
        self.text_color = txt_color

    def draw(self):
        pygame.draw.rect(self.win, self.color, (self.x, self.y, 150, 50), 0)
        pygame.draw.rect(self.win, [0, 0, 0], (self.x, self.y, 150, 50), 3)
        basic_font = pygame.font.SysFont(None, 20)
        text = basic_font.render(self.text, True, self.text_color)
        textrect = text.get_rect()
        textrect.centerx = self.x + 75
        textrect.centery = self.y + 25
        self.win.blit(text, textrect)

    def clicked(self, mx, my):
        return self.x < mx < self.x + 150 and self.y < my < self.y + 50
