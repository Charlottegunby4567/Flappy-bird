import pygame

class Fugl:
    def __init__(self, x, y, VINDU_HØYDE):
        self.x = x
        self.y = y
        self.fart = 0
        self.VINDU_HØYDE = VINDU_HØYDE
        
    def hopp(self):
        self.fart = -5
    
    def oppdater(self):
        self.fart += 1
        self.y += self.fart
        self.y = max(0, min(self.VINDU_HØYDE - 30, self.y))
    
    def tegn(self, vindu, fugl_bilde):
        vindu.blit(fugl_bilde, (self.x, self.y))

