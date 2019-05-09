import pygame


class Sound:
    def __init__(self):
        self.sound = pygame.mixer.Sound("Music.ogg")

    def play(self):
        self.sound.play()

    def stop(self):
        self.sound.stop()
