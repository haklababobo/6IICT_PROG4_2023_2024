import pygame, random
from paas_oef_2 import FruitSpel

# Zet Pygame klaar.
pygame.init()
kleur_achtergrond = (0,0,0)
breedte, hoogte = 800, 600 
screen = pygame.display.set_mode((breedte, hoogte))
klok = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 48)
spel = FruitSpel()

running, kan_springen = True, False
while running:
    # Stel spel in op 30 FPS.
    klok.tick(30)
    pygame.event.pump()

    "ACTIE 1: interactie speler."
    for event in pygame.event.get():  
        if event.type == pygame.QUIT: 
            running = False   

    muis_klik = pygame.mouse.get_pressed()
    muis_pos  = pygame.mouse.get_pos()
    spel.klikken(muis_klik[0],muis_pos)


    "ACTIE 2: spel-staat wijzigen. "
    if random.random() > 0.95:
        spel.maak_fruit((breedte,hoogte),(random.randint(0,255),random.randint(0,255),random.randint(0,255)))

    spel.beweeg_fruiten()
    spel.reset_kan_klikken(muis_klik[0])

    "ACTIE 3: teken op scherm."
    screen.fill(kleur_achtergrond) # Reset scherm
    spel.teken_fruiten(screen)
    spel.teken_score(screen,font)
    pygame.display.flip() # Toon scherm aan speler.