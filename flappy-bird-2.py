import pygame
import random

pygame.init()

VINDU_BREDDE = 600
VINDU_HØYDE = 400
FPS = 40
klokke = pygame.time.Clock()
vindu = pygame.display.set_mode((VINDU_BREDDE, VINDU_HØYDE))
pygame.display.set_caption("Flappy Bird")

# Laster inn bilder av fugl og rør og endrer størrelsen
fugl_bilde = pygame.transform.scale(pygame.image.load('fugl.png'), (80, 80))
rør_bilde = pygame.transform.scale(pygame.image.load('rør.png'), (80, VINDU_HØYDE - 200))

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
        self.y = max(0, min(VINDU_HØYDE - 30, self.y))
    
    def tegn(self):
        vindu.blit(fugl_bilde, (self.x, self.y))

class Rør:
    MELLOMROM = 200
    
    def __init__(self, x):
        self.x = x
        self.høyde = random.randint(50, VINDU_HØYDE - self.MELLOMROM - 50)
        self.passert = False
    
    def oppdater(self):
        self.x -= 5
    
    def tegn(self):
        vindu.blit(rør_bilde, (self.x, 0))
        vindu.blit(pygame.transform.flip(rør_bilde, False, True), (self.x, self.høyde + self.MELLOMROM))

class Spill:
    def __init__(self):
        self.fugl = Fugl(50, VINDU_HØYDE // 2 - 15)
        self.rører = [Rør(VINDU_BREDDE + i * 200) for i in range(3)]
        self.poeng = 0
        
    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    self.fugl.hopp()
            
            self.fugl.oppdater()
            
            for rør in self.rører:
                rør.oppdater()
                if self.fugl.x < rør.x + 60 and self.fugl.x + 40 > rør.x:
                    if self.fugl.y < rør.høyde or self.fugl.y + 30 > rør.høyde + rør.MELLOMROM:
                        print("Spillet er slutt! Poeng: ", self.poeng)
                        pygame.quit()
                        quit()

                if rør.x + 60 < self.fugl.x and not rør.passert:
                    self.poeng += 1
                    rør.passert = True
            
                if rør.x + 60 < self.fugl.x:
                    rør.passert = False

            if self.rører[0].x < -60:
                self.rører.pop(0)
                nytt_rør = Rør(self.rører[-1].x + 200)
                self.rører.append(nytt_rør)
            
            vindu.fill((173, 216, 230))
            self.fugl.tegn()
            for rør in self.rører:
                rør.tegn()

            font = pygame.font.Font(None, 36)
            tekst = font.render(f'Poeng: {self.poeng}', True, (255, 255, 255))
            vindu.blit(tekst, (10, 10))
            pygame.display.update()
            pygame.time.delay(30)

if __name__ == "__main__":
    nytt_spill = Spill()
    nytt_spill.start()

    pygame.display.update()
    klokke.tick(FPS)
