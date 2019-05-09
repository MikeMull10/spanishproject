import pygame

ORANGE = [227, 114, 70]
BLACK = [0, 0, 0]
body_red = pygame.image.load("Mayan Body.png")
body_blue = pygame.image.load("Mayan Body Blue.png")
head_red = pygame.image.load("Mayan Head.png")
head_blue = pygame.image.load("Mayan Head Blue.png")
ir_br = body_red.get_rect()
ir_bb = body_blue.get_rect()
ir_hr = head_red.get_rect()
ir_hb = head_blue.get_rect()
x = 600
y = 400
ir_br.centerx = x
ir_br.centery = y
ir_bb.centerx = x
ir_bb.centery = y
ir_hr.centerx = x
ir_hr.centery = y
ir_hb.centerx = x
ir_hb.centery = y
body_x = x
body_y = y
background = pygame.image.load("Mayas.png")
background_rect = background.get_rect()
background_rect.centerx = 640
background_rect.centery = 360
title = pygame.image.load("PokATok.png")
title_rect = title.get_rect()
title_rect.centerx = 640
title_rect.centery = 80
links = []
links.append("(Imagen de Fondo)    https://www.brainpop.com/socialstudies/worldhistory/mayacivilization/")
links.append("(Imagen de Jugadores)    https://www.deviantart.com/nizuma/art/Pok-a-tok-game-196814001")
links.append("(La Historia)    https://mundochapin.com/2013/06/juego-de-pelota-maya/16246/")
links.append("(La Musica)    https://www.youtube.com/watch?v=36Ul4dprTXg")
settings = pygame.image.load("Settings.png")
settings_rect = settings.get_rect()
settings_rect.centerx = 1260
settings_rect.centery = 700
instructions = pygame.image.load("Instructions.png")
instructions_rect = instructions.get_rect()
instructions_rect.centerx = 640
instructions_rect.centery = 360
history = pygame.image.load("History.png")
history_rect = history.get_rect()
