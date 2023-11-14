import pygame
from fugl import Fugl
from rør import Rør
from spill import Spill

pygame.init()

# 1. Oppsett
VINDU_BREDDE = 600
VINDU_HØYDE = 400
FPS = 40
klokke = pygame.time.Clock()
vindu = pygame.display.set_mode((VINDU_BREDDE, VINDU_HØYDE))

pygame.display.set_caption("Flappy Bird")


# Bilder av fugl og rør og endrer størrelsen
fugl_bilde = pygame.transform.scale(pygame.image.load('fugl.png'), (80, 80))
rør_bilde = pygame.transform.scale(pygame.image.load('rør.png'), (80, VINDU_HØYDE - 200))

if __name__ == "__main__":
    print("Programmet startet!")
    
    nytt_spill = Spill(VINDU_BREDDE, VINDU_HØYDE)
    
    print("Starter spillet...")
    
    try:
        nytt_spill.start(vindu, fugl_bilde, rør_bilde)
    except Exception as e:
        print(f"En feil oppstod: {e}")


    pygame.display.update()
    klokke.tick(FPS)



