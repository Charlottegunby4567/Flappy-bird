import pygame
from fugl import Fugl
from rør import Rør

class Spill:
    def __init__(self, VINDU_BREDDE, VINDU_HØYDE):
        self.fugl = Fugl(50, VINDU_HØYDE // 2 - 15, VINDU_HØYDE)
        self.rører = [Rør(VINDU_BREDDE + i * 200, VINDU_HØYDE) for i in range(3)]
        self.poeng = 0
        self.VINDU_HØYDE = VINDU_HØYDE  # Lagre VINDU_HØYDE som en instansvariabel
    
    def start(self, vindu, fugl_bilde, rør_bilde):

        # Oppdaterer spill:
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

                if (
                    rør.x < self.fugl.x + 40 < rør.x + 60
                    and not (rør.høyde < self.fugl.y < rør.høyde + rør.MELLOMROM)
                ):
                    print("Spillet er slutt! Poeng: ", self.poeng)
                    pygame.quit()
                    quit()

                if rør.x + 60 < self.fugl.x and not rør.passert:
                    self.poeng = 0
                    rør.passert = True

                if rør.x + 60 < self.fugl.x:
                    rør.passert = False

            if self.rører[0].x < -60:
                self.rører.pop(0)
                nytt_rør = Rør(self.rører[-1].x + 200, self.VINDU_HØYDE)  # Bruk VINDU_HØYDE fra instansen
                self.rører.append(nytt_rør)
            
            vindu.fill((173, 216, 230))
            self.fugl.tegn(vindu, fugl_bilde)
            for rør in self.rører:
                rør.tegn(vindu, rør_bilde)
        
            font = pygame.font.Font(None, 36)
            tekst = font.render(f'Poeng: {self.poeng}', True, (255, 255, 255))
            vindu.blit(tekst, (10, 10))
            pygame.display.update()
            pygame.time.delay(30)
