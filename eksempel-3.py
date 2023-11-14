import pygame
import random

pygame.init()

BREDDE = 600
HOYDE = 600
FPS = 40
vindu = pygame.display.set_mode((BREDDE, HOYDE))
klokke = pygame.time.Clock()
pygame.display.set_caption("Flappy Bird")

overskrift_font = pygame.font.SysFont("Arial", 32)
overskrift_surface = overskrift_font.render("Flappy Bird", True, "black")

fugl_bilde = pygame.image.load("fugl.png")
fugl_BREDDE, fugl_HOYDE = 50, 50
fugl_x, fugl_y = 50, BREDDE // 2 - fugl_HOYDE // 2
fugl_fart = 5
tyngdekraft = 1
hopp_styrke = 15

rør_bilde = pygame.image.load("rør.png")
rør_bredde, rør_høyde = 50, random.randint(100, 300)
rør_x = BREDDE
rør_fart = 5

poeng = 0
poeng_font = pygame.font.SysFont("Arial", 32)

def tegn_fugl(x, y):
    vindu.blit(fugl_bilde, (x, y))

def tegn_rør(x, høyde):
    vindu.blit(rør_bilde, (x, 0))
    vindu.blit(pygame.transform.flip(rør_bilde, False, True), (x, høyde + 150))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
    
    tastatur = pygame.key.get_pressed()
    if tastatur[pygame.K_UP] and fugl_y > 0:
        fugl_y -= hopp_styrke
    if tastatur[pygame.K_DOWN] and fugl_y < HOYDE - fugl_HOYDE:
        fugl_y += fugl_fart

    fugl_y += tyngdekraft
    rør_x -= rør_fart
    
    if rør_x < -rør_bredde:
        rør_x = BREDDE
        rør_høyde = random.randint(100, 300)
        poeng += 1  # Øker poengtellingen når røret passerer fra venstre til høyre
    
    # Kollisjon med rør
    if fugl_x < rør_x + rør_bredde and fugl_x + fugl_BREDDE > rør_x:
        if fugl_y < rør_høyde or fugl_y + fugl_HOYDE > rør_høyde + 150:
            print("Spillet er slutt! Poeng:", poeng)
            pygame.quit()
            raise SystemExit

    # Oppdaterer skjermen
    vindu.fill("light blue")
    vindu.blit(overskrift_surface, (10, 10))
    poeng_surface = poeng_font.render("Poeng: " + str(poeng), True, "black")
    vindu.blit(poeng_surface, (390, 10))
    tegn_rør(rør_x, rør_høyde)
    tegn_fugl(fugl_x, fugl_y)
    
    pygame.display.update()
    klokke.tick(FPS)
