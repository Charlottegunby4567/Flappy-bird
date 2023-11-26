# Importer pygame-biblioteket og nødvendige klasser fra andre filer
import pygame
from fugl import Fugl
from rør import Rør
from spill import Spill
from meny import Meny


# Initialiser pygame-biblioteket
pygame.init()


# 1. Oppsett
VINDU_BREDDE = 600
VINDU_HØYDE = 400
FPS = 60
klokke = pygame.time.Clock()


# Opprett spillvinduet
vindu = pygame.display.set_mode((VINDU_BREDDE, VINDU_HØYDE))


# Sett tittelen på vinduet
pygame.display.set_caption("Flappy Bird")


# Bilder av fugl og rør og endrer størrelsen
fugl_bilde = pygame.transform.scale(pygame.image.load('fugl.png'), (80, 80))
rør_bilde = pygame.transform.scale(pygame.image.load('rør.png'), (80, VINDU_HØYDE - 200))

meny = Meny(VINDU_BREDDE, VINDU_HØYDE)

# Sjekk om dette scriptet kjøres direkte og ikke importeres som en modul
if __name__ == "__main__":
    print("Programmet startet!")

# Hovedspill-løkke som kjører kontinuerlig
    while True:
    # Håndterer hendelser (tastetrykk, museklikk, etc.)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:

            # Hvis brukeren lukker vinduet, avslutt pygame og avslutt programmet
                pygame.quit()
                quit()

            # Hvis det er et museklikk
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Hent x- og y-koordinatene til museklikket
                mouseX, mouseY = pygame.mouse.get_pos()
                print(f"Klikket på: ({mouseX}, {mouseY})")
                # Kall håndter_menyklikk-metoden i menyobjektet for å håndtere museklikket
                meny.håndter_menyklikk(mouseX, mouseY)
                

                # Hvis "Start" er valgt i menyen
                if meny.velg_start:
                    # Opprett et nytt Spill-objekt med gitt vindusbredde og -høyde
                    nytt_spill = Spill(VINDU_BREDDE, VINDU_HØYDE)
                    print("Starter spillet...")
    

                    # Prøv å starte spillet, og håndter eventuelle unntak (feil)
                    try:
                        nytt_spill.start(vindu, fugl_bilde, rør_bilde)
                    except Exception as e:
                        # Skriv ut feilmeldingen hvis det oppstår en feil
                        print(f"En feil oppstod: {e}")


                 # Hvis "Avslutt" er valgt i menyen
                elif meny.velg_avslutt:
                    # Avslutt pygame og avslutt programmet
                    pygame.quit()
                    quit()

        # Fyller spillvinduet med en lys blå farge (173, 216, 230)
        vindu.fill((173, 216, 230))

    # tegn menyen
        meny.tegn_meny(vindu)
        pygame.display.update()
        klokke.tick(FPS)  # Begrens oppdateringshastigheten til FPS



