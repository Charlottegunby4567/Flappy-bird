import pygame
import random

# Initialiserer pygame
pygame.init()

# Definerer farger
HVIT = (255, 255, 255)

# Definerer vindusstørrelse
VINDU_BREDDE = 600
VINDU_HØYDE = 400
FPS = 40
klokke = pygame.time.Clock()
vindu = pygame.display.set_mode((VINDU_BREDDE, VINDU_HØYDE))
pygame.display.set_caption("Flappy Bird")


# Fuglklasse
class Fugl:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.fart = 0
        
    def hopp(self):
        self.fart = -10
    
    def oppdater(self):
        self.fart += 1
        self.y += self.fart
        # Begrenser bevegelse til å være innenfor vinduet
        self.y = max(0, min(VINDU_HØYDE - 50, self.y))
    
    def tegn(self):
        pygame.draw.rect(vindu, HVIT, (self.x, self.y, 50, 50))

# Rørklasse
class Rør:
    def __init__(self, x, høyde):
        self.x = x
        self.høyde = høyde
        self.passert = False
    
    def oppdater(self):
        self.x -= 5
    
    def tegn(self):
        pygame.draw.rect(vindu, HVIT, (self.x, 0, 50, self.høyde))
        pygame.draw.rect(vindu, HVIT, (self.x, self.høyde + 150, 50, VINDU_HØYDE - self.høyde - 150))

# Spillklasse
class Spill:
    def __init__(self):
        self.fugl = Fugl(50, VINDU_HØYDE // 2 - 25)
        self.rør = Rør(VINDU_BREDDE, random.randint(50, VINDU_HØYDE - 200))
        self.poeng = 0
    
    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                # Spilleren kan hoppe ved å trykke opp-pilen
                if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    self.fugl.hopp()
            
            self.fugl.oppdater()
            self.rør.oppdater()
            
            # Sjekker kollisjon med rør
            if self.fugl.x < self.rør.x + 50 and self.fugl.x + 50 > self.rør.x:
                if self.fugl.y < self.rør.høyde or self.fugl.y + 50 > self.rør.høyde + 150:
                    print("Spillet er slutt! Poeng: ", self.poeng)
                    pygame.quit()
                    quit()
            
            # Sjekker om røret er passert fuglen, øker poeng hvis det er tilfelle
            if self.rør.x < self.fugl.x and not self.rør.passert:
                self.poeng += 1
                self.rør.passert = True
            
            # Oppdaterer rør-passeringstatus
            if self.rør.x + 50 < self.fugl.x:
                self.rør.passert = False
            
            # Tegner alt på skjermen
            vindu.fill((0, 0, 0))
            self.fugl.tegn()
            self.rør.tegn()
            # Tegner poengtelling på skjermen
            font = pygame.font.Font(None, 36)
            tekst = font.render(f'Poeng: {self.poeng}', True, HVIT)
            vindu.blit(tekst, (10, 10))
            pygame.display.update()
            
            # Legger til pause for å gjøre spillet spillbart
            pygame.time.delay(30)

# Starter spillet
if __name__ == "__main__":
    nytt_spill = Spill()
    nytt_spill.start()


pygame.display.flip()
klokke.tick(FPS)
