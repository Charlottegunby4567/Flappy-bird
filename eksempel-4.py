import pygame
import random

# Initialiserer pygame
pygame.init()

# Definerer vindusstørrelse
VINDU_BREDDE = 600
VINDU_HØYDE = 400
FPS = 40
klokke = pygame.time.Clock()
vindu = pygame.display.set_mode((VINDU_BREDDE, VINDU_HØYDE))
pygame.display.set_caption("Flappy Bird")

# Laster inn bilder
fugl_bilde = pygame.image.load("fugl.png")
rør_bilde = pygame.image.load("rør.png")

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
        vindu.blit(fugl_bilde, (self.x, self.y))

# Rørklasse
class Rør:
    def __init__(self, x, høyde):
        self.x = x
        self.høyde = høyde
    
    def oppdater(self):
        self.x -= 5
    
    def tegn(self):
        vindu.blit(rør_bilde, (self.x, 0))
        vindu.blit(pygame.transform.flip(rør_bilde, False, True), (self.x, self.høyde + 150))

# Spillklasse
class Spill:
    def __init__(self):
        self.fugl = Fugl(50, VINDU_HØYDE // 2 - 25)
        self.rører = [Rør(VINDU_BREDDE, random.randint(50, VINDU_HØYDE - 200)) for _ in range(2)]
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
            
            # Oppdaterer rører og sjekker kollisjon
            for rør in self.rører:
                rør.oppdater()
                if self.fugl.x < rør.x + 50 and self.fugl.x + 50 > rør.x:
                    if self.fugl.y < rør.høyde or self.fugl.y + 50 > rør.høyde + 150:
                        print("Spillet er slutt! Poeng: ", self.poeng)
                        pygame.quit()
                        quit()
                # Sjekker om rør er passert fuglen, øker poeng hvis det er tilfelle
                if rør.x + 50 < self.fugl.x and not rør.passert:
                    self.poeng += 1
                    rør.passert = True
                # Oppdaterer rør-passeringstatus
                if rør.x + 50 < self.fugl.x:
                    rør.passert = False
            # Legger til nye rører når de gamle er passert
            if self.rører[0].x < -50:
                self.rører.pop(0)
                nytt_rør = Rør(VINDU_BREDDE, random.randint(50, VINDU_HØYDE - 200))
                self.rører.append(nytt_rør)
            
            # Tegner alt på skjermen
            vindu.fill((0, 0, 0))
            self.fugl.tegn()
            for rør in self.rører:
                rør.tegn()
            # Tegner poengtelling på skjermen
            font = pygame.font.Font(None, 36)
            tekst = font.render(f'Poeng: {self.poeng}', True, (255, 255, 255))
            vindu.blit(tekst, (10, 10))
            pygame.display.update()
            
            # Legger til pause for å gjøre spillet spillbart
            pygame.time.delay(30)

# Starter spillet
if __name__ == "__main__":
    nytt_spill = Spill()
    nytt_spill.start()
