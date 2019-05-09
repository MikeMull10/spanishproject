from Button import *


class Setting(Button):
    def __init__(self, win, x, y, txt, function, color, txt_color, selected):
        super().__init__(win, x, y, txt, function, color, txt_color)
        self.selected = selected

    def draw(self):
        color = self.color
        if not self.selected:
            color = [255, 255, 255]
        pygame.draw.rect(self.win, color, (self.x, self.y, 150, 50), 0)
        pygame.draw.rect(self.win, [0, 0, 0], (self.x, self.y, 150, 50), 3)
        basic_font = pygame.font.SysFont(None, 20)
        text = basic_font.render(self.text, True, self.text_color)
        textrect = text.get_rect()
        textrect.centerx = self.x + 75
        textrect.centery = self.y + 25
        self.win.blit(text, textrect)

    def clicked(self, mx, my):
        return self.x < mx < self.x + 150 and self.y < my < self.y + 50
