# Importer pygame-biblioteket
import pygame

# Definer Fugl-klassen
class Fugl:
    def __init__(self, x, y, VINDU_HØYDE):
        self.x = x
        self.y = y
        self.fart = 1  # Initialiser fart (gravitasjonseffekt)
        self.VINDU_HØYDE = VINDU_HØYDE   # Lagre vinduhøyden som en instansvariabel

 # Metode for å få fuglen til å hoppe      
    def hopp(self):
    # Sett fart til negativ verdi for å simulerere et hopp
        self.fart = -10 
    
# Metode for å oppdatere fuglens posisjon: fart og gravitasjon
    def oppdater(self):
    # Legg til gravitasjonseffekt
        self.fart += 1
    # Oppdater fuglens posisjon
        self.y += self.fart
    # Begrens fuglens posisjon til å være innenfor vinduet
        self.y = max(0, min(self.VINDU_HØYDE - 30, self.y))
    

# Metode for å tegne fuglen på spillvinduet
    def tegn(self, vindu, fugl_bilde):
        vindu.blit(fugl_bilde, (self.x, self.y))

