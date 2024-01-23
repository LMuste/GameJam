import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500)) # Setter skjermen til 500x500 piksler.

clock = pygame.time.Clock()

running = True

while running:
    # Avslutter løkken
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fyller skjermen med hvit farge
    screen.fill("white")

    """
    Her skal vi putte spillets logikk, som å tegne figurer og oppdatere posisjonen deres.
    """

    # Oppdaterer hele skjermen
    pygame.display.flip()

    # Forsikrer at spillet kjører i maksimalt 60 FPS.
    clock.tick(60)

# Avslutter spillet
pygame.quit()