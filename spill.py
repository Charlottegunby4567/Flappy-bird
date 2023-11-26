# Importerer pygame - biblioteket og nødvendige klasser fra andre filer
import pygame  
from fugl import Fugl
from rør import Rør
from meny import Meny

 # Definerer spill-klassen
class Spill:           

    # Initialiser spillobjekter: fugl, rører, poeng og vinduhøyde
    def __init__(self, VINDU_BREDDE, VINDU_HØYDE):      
        self.fugl = Fugl(50, VINDU_HØYDE // 2 - 15, VINDU_HØYDE)
        self.rører = [Rør(VINDU_BREDDE + i * 200, VINDU_HØYDE) for i in range(3)]
        self.poeng = 0
    # Lagre VINDU_HØYDE som en instansvariabel
        self.VINDU_HØYDE = VINDU_HØYDE 

    def avslutt_spill(self):
        print("Fuglen traff et rør!! Spillet er slutt! Poeng: ", self.poeng)
        self.avslutt_spill()

    # Hovedløkke for å oppdatere spillet
    def start(self, vindu, fugl_bilde, rør_bilde):      

        # Oppdaterer spill:
        # Håndterer hendelser
        while True:  

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.avslutt_spill()

            # sjekker for tastetrykk (hopp)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_UP: 
                    self.fugl.hopp()


            # Oppdaterer fuglens posisjon
            self.fugl.oppdater()        
            
            # Oppdaterer rørene og sjekk kollisjon med fuglen
            for rør in self.rører:      
                rør.oppdater()

            # Sjekker kollisjon med rørene
                if (
                    rør.x < self.fugl.x + 40 < rør.x + 50
                    and (self.fugl.y < rør.høyde or self.fugl.y > rør.høyde + rør.MELLOMROM)
                ):
                    self.avslutt_spill()
            
                # Sjekker om fuglen har passert et rørpar
                if rør.x + 60 < self.fugl.x and not rør.passert:
                 # Sørg for at poengene bare øker når fuglen passerer et nytt rørpar
                    if all(r.passert for r in self.rører[self.rører.index(rør) - 1:self.rører.index(rør) + 1]):
                        self.poeng += 1
                        rør.passert = True
            # rør.x + 60 < self.fugl.x: Dette betyr at hvis x-koordinatet til røret (pluss en viss avstand på 60 piksler, 
            # sannsynligvis bredden på røret) er mindre enn x-koordinatet til fuglen, vil betingelsen være sann. 
            # Dette sjekker om fuglen har passert røret.
            # not rør.passert: Dette betyr at hvis passert-attributtet til røret er False, vil betingelsen være sann. 
            # Dette sjekker om røret ikke har blitt passert tidligere.
            # Hvis begge disse betingelsene er sanne, vil koden inne i blokken bli utført:

            # self.poeng += 1: Dette øker poengsummen med 1. Det antyder at fuglen har passert et rørpar, og derfor øker spillerens poengsum.
            # rør.passert = True: Dette setter passert-attributtet til røret til True. 
            # Dette gjør at programmet vet at fuglen allerede har passert dette rørparet, og poengene ikke skal økes igjen når fuglen beveger seg forbi dette røret.
                    

            # Nullstill passert-status når røret er bak fuglen
                if self.rører[0].x + 60 < self.fugl.x:
                    self.rører[0].passert = False


            # Fjerner det første røret i listen hvis det er utenfor skjermen
            if self.rører[0].x < -60:
                self.rører.pop(0)
                nytt_rør = Rør(self.rører[-1].x + 400, self.VINDU_HØYDE)  # Bruk VINDU_HØYDE fra instansen
                self.rører.append(nytt_rør)
            
            
            # Tegner spillvinduet
            vindu.fill((173, 216, 230))
            self.fugl.tegn(vindu, fugl_bilde)
            for rør in self.rører:
                rør.tegn(vindu, rør_bilde)
            
            
            # Viser poengene på skjermen
            font = pygame.font.Font(None, 36)
            tekst = font.render(f'Poeng: {self.poeng}', True, (255, 255, 255))
            vindu.blit(tekst, (10, 10))

            # Oppdaterer vinduet og legger til en forsinkelse
            pygame.display.update()
            pygame.time.delay(30)

