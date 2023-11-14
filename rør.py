import pygame
import random

class Rør:
    MELLOMROM = 250     # mellomrom mellom rørene
    
    def __init__(self, x, VINDU_HØYDE):
        self.x = x
        self.høyde = random.randint(50, VINDU_HØYDE - self.MELLOMROM - 50)
        self.passert = False
        self.VINDU_HØYDE = VINDU_HØYDE
    
    def oppdater(self):
        self.x -= 10
    
    def tegn(self, vindu, rør_bilde):
        vindu.blit(rør_bilde, (self.x, 0))
        vindu.blit(pygame.transform.flip(rør_bilde, False, True), (self.x, self.høyde + self.MELLOMROM))
