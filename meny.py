
import pygame

# Definerer en klasse for meny
class Meny:
    def __init__(self, vindu_bredde, vindu_høyde):
        # Initialiserer egenskaper for menyen
        self.vindu_bredde = vindu_bredde
        self.vindu_høyde = vindu_høyde

        # Setter opp fonten for menytekst
        self.meny_font = pygame.font.Font(None, 50)

        # Lager Pygame Surface-objekter for tekstene "Start" og "Avslutt" med hvit farge
        self.start_tekst = self.meny_font.render("Start", True, (255, 255, 255))
        self.avslutt_tekst = self.meny_font.render("Avslutt", True, (255, 255, 255))

        # Lager rektangelobjekter for områdene hvor "Start" og "Avslutt" skal vises på skjermen
        self.start_rektangel = pygame.Rect(vindu_bredde // 2 - 40, vindu_høyde // 2 - 50, 100, 50)
        self.avslutt_rektangel = pygame.Rect(vindu_bredde // 2 - 50, vindu_høyde // 2 + 50, 125, 50)

        # Initialiserer variabler som holder styr på om "Start" eller "Avslutt" er valgt
        self.velg_start = False
        self.velg_avslutt = False



 # Metode for å tegne menyen på skjermen
    def tegn_meny(self, vindu):

    # Tegn en svart firkant rundt "Start" og "Avslutt"
        pygame.draw.rect(vindu, (255, 255, 255), self.start_rektangel, 2)
        pygame.draw.rect(vindu, (255, 255, 255), self.avslutt_rektangel, 2)

        # Fyll rektangelene med farge
        pygame.draw.rect(vindu, (0, 0, 0), self.start_rektangel)
        pygame.draw.rect(vindu, (0, 0, 0), self.avslutt_rektangel)

        # Tegn teksten i midten av rektanglene
        vindu.blit(self.start_tekst, (self.vindu_bredde // 2 - 30, self.vindu_høyde // 2 - 40))
        vindu.blit(self.avslutt_tekst, (self.vindu_bredde // 2 - 50, self.vindu_høyde // 2 + 60))


# Metode for å håndtere museklikk i menyen
    def håndter_menyklikk(self, x, y):
    # Sjekker om museklikket er innenfor "Start"-rektangelet og setter variabelen deretter
        self.velg_start = self.start_rektangel.collidepoint(x, y)
    # Sjekker om museklikket er innenfor "Avslutt"-rektangelet og setter variabelen deretter
        self.velg_avslutt = self.avslutt_rektangel.collidepoint(x, y)
    

