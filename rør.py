# Importer pygame-biblioteket og random-modulen
import pygame
import random

# Definer Rør-klassen
class Rør:

# Avstand mellom rørene
    MELLOMROM = 200  
    
# Konstruktør for å initialisere røret med en x-posisjon og høyde
    def __init__(self, x, VINDU_HØYDE):
        self.x = x

    # Velg en tilfeldig høyde for røret
        self.høyde = random.randint(50, VINDU_HØYDE - self.MELLOMROM - 50)
        self.passert = False        # Flagget som indikerer om fuglen har passert dette røret
        self.VINDU_HØYDE = VINDU_HØYDE      # Lagre vinduhøyden som en instansvariabel
        self.passert = False
    
 # Metode for å oppdatere rørets posisjon
    def oppdater(self):
    # Flytt røret mot venstre med en konstant hastighet
        self.x -= 7


# Metode for å tegne røret på spillvinduet
    def tegn(self, vindu, rør_bilde):

     # Tegn det øvre røret ved posisjon (self.x, 0)
        vindu.blit(rør_bilde, (self.x, 0))
    # Tegn det nedre røret ved posisjon (self.x, self.høyde + MELLOMROM)
        vindu.blit(pygame.transform.flip(rør_bilde, False, True), (self.x, self.høyde + self.MELLOMROM))
